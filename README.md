<img src="https://repository-images.githubusercontent.com/436395134/1459feb6-1236-4896-be70-779cf08288db">

# EZ DDNS CLOUDFLARE

![](https://img.shields.io/badge/Support-Linux-lightgrey) ![](https://img.shields.io/badge/Python->3.0-green)

This script aims to make the <b>dynamic ip</b> of your local server, <b>public</b>. It does this by regularly updating cloudflare's dns record. Basically, your domain will always be updated every IP change.

---

## Prerequisites

- An account on [Cloudflare](https://cloudflare.com).<br>
- At least 1 DNS record setup on cloudflare<br>
- Crontab installed

### Effects

Your domain will point to the public address of the machine in which you execute this script.

## Configuration

Clone this repository

```sh
git clone https://github.com/anywayzz/ez-ddns-cloudflare
```

Open `config.py` and set

```py
API_TOKEN = " { YOUR API TOKEN } "
ZONE_ID = 	" { YOUR ZONE ID } "
EMAIL = 	" { YOUR CLOOUDFLARE EMAIL } "
DOMAIN = 	[" { THE DOMAIN/S TO BE UPDATED } "]
```

if you don't know your API TOKEN check [here](https://support.cloudflare.com/hc/en-us/articles/200167836-Managing-API-Tokens-and-Keys#12345680).<br>
if you don't know your ZONE ID check [here](https://community.cloudflare.com/t/where-to-find-zone-id/132913).

Finally start the script:

```sh
chmod +x ezddns.sh;
./ezddns.sh
```
