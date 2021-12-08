import requests
import json 
import config


class dns:

	api_token: str
	email : str
	zoneid : str
	dnsrecords : json

	def __init__(self, API_TOKEN: str, EMAIL: str, ZONE_ID: str):
		self.api_token = API_TOKEN 
		self.email = EMAIL
		self.zoneid = ZONE_ID
	
	def get_dnsrecords(self) -> None:
		dnsrec = requests.get("https://api.cloudflare.com/client/v4/zones/"+ self.zoneid +"/dns_records", headers={
			"X-Auth-Email" : self.email,
			"X-Auth-Key" : self.api_token,
			"Content-Type" : "application/json"
			})
		self.dnsrecords = json.loads(dnsrec.text)

	def print_dnsrecords(self) -> None:
		print("ZONES AVAILABLE")
		for i in self.dnsrecords["result"]:
			print("----------------")
			print("ID: "+ i["id"])
			print("ZONE NAME: " + i["zone_name"])
			print("NAME: " + i["name"])
			print("TYPE: " + i["type"])
			print("CONTENT: "+ i["content"])
	
	def dns_update(self, name: str=config.DOMAIN) -> bool:

		id=""
		type : str
		ttl : int
		proxied : bool

		for i in self.dnsrecords["result"]:
			if i["name"] == name:
				id = i["id"]
				type = i["type"]
				ttl = i["ttl"]
				proxied = i["proxied"]
		
		if id=="":
			raise Exception("DNS RECORD DOES NOT EXISTS.")
		
		upddns= requests.put("https://api.cloudflare.com/client/v4/zones/"+self.zoneid+"/dns_records/"+id,
		headers={
		"X-Auth-Email": self.email,
		"X-Auth-Key" : self.api_token,
		"Content-Type" : "application/json"
		}, data=json.dumps({"type":type, "name": config.DOMAIN,"content":config.IP, "ttl":ttl,"proxied": proxied}, indent=4))

		return bool(json.loads(upddns.text)["success"])
			


if __name__ == "__main__":
	dnsrecord = dns(config.API_TOKEN, config.EMAIL, config.ZONE_ID)
	
	dnsrecord.get_dnsrecords()
	
	# UNCOMMENT THIS LINE TO CHECK NAMES OF DNS RECORDS
	# dnsrecord.print_dnsrecords()
	
	if dnsrecord.dns_update():
		print("Success")


