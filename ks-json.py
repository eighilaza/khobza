#! /usr/bin/python
# coding=utf-8

import requests
import json

r = requests.get("https://ws.ovh.com/dedicated/r2/ws.dispatcher/getAvailability2")

rawData = json.loads(r.text)
print(rawData)
for row in rawData:
	if row['reference'] == "sk1"
