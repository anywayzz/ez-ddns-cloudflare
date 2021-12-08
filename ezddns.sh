#!/bin/bash

rm -rf /opt/ezddns_cloudflare/

mkdir /opt/ezddns_cloudflare
scp -r src/* /opt/ezddns_cloudflare/

if ! command -v crontab &> /dev/null
then
    echo "cronjob could not be found, install cronjob."
    exit
fi

crontab /opt/ezddns_cloudflare/cron.jobs

echo "Success!"