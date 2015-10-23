#! /usr/bin/python
# coding=utf-8

import requests
import json
import subprocess

r = requests.get("https://ws.ovh.com/dedicated/r2/ws.dispatcher/getAvailability2")

rawData = json.loads(r.text)

answer_dic = rawData['answer']
availability_list = answer_dic['availability']

sendEmail=False
for server_dic in availability_list:
	for key, value in server_dic.iteritems():
		if key=="reference":
			if value=="150sk10":
				metaZones_list = server_dic['metaZones']
				for metaZones_dic in metaZones_list:
					for key, value in metaZones_dic.iteritems():
						if key=="availability":
							if value != "unknown":
								print "Disponible"
								sendEmail=True
							else:
								print "Indisponible"
				zones_list = server_dic['zones']
				for zones_dic in zones_list:
					for key, value in zones_dic.iteritems():
						if key=="availability":
							if value != "unknown":
								print "Disponible"
								sendEmail=True
							else:
								print "Indisponible"

if sendEmail == True:
	subprocess.call(["/home/ighi/Kimsufi/send-email.sh"])
