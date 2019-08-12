import requests
import time
from time import sleep
import json
import random
class omegle():
	def __init__(self,server):
		self.server=server
		if old=="yes":
			self.headers={
			"Origin": "https://www.omegle.com",
			"Referer": "https://www.omegle.com/",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
			}
			self.id=json.loads(open("key.json").read())
		if old=="no":
			url='https://{}.omegle.com/start?caps=recaptcha2&firstevents=1&spid=&randid=TG2AKZQA&topics=["friends"]&lang=en'.format(self.server)
			self.headers={
				"Origin": "https://www.omegle.com",
				"Referer": "https://www.omegle.com/",
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
			}
			data={
				"caps": "recaptcha2",
				"firstevents": 1,
				"spid": "",
				"randid": "TG2AKZQA",
				"topics": '["friends"]',
				"lang": "en"
			}
			r=requests.post(url,headers=self.headers,data=data)
			#print(r.json())
			self.id=r.json()["clientID"]
	def Connect(self):
		data1={}
		dumb={}
		data1["id"]=self.id
		dumb["id"]=self.id
		dumb["server"]=self.server
		if self.id:
			print("CONNECTED")
		with open("key.json","w") as f:
			json.dump(dumb, f)
		web="https://{}.omegle.com/events".format(self.server)
		running = True
		while running:
			r=requests.post(web,headers=self.headers,data=data1)
			data=json.loads(r.text)
			try:
				for n in data:
					if n[0] == "typing":
						print("[{}]Stranger: Typing".format(time.strftime("%d-%b %I:%M:%S %p")))
						sleep(2)
					if n[0] == "stoppedTyping":
						continue
						sleep(2)
					if n[0] == "gotMessage":
						print("[{}]Stranger: {}".format(time.strftime("%d-%b %I:%M:%S %p"),n[1]))
						sleep(2)
					if n[0] == "strangerDisconnected":
						print("[{}]Stranger: Disconnected".format(time.strftime("%d-%b %I:%M:%S %p")))
						running = False
					else:
						continue
						sleep(2)
			except:
				s=1
		print("==================================")
if __name__ == '__main__':
	servers = ["front1", "front2", "front3", "front4","front5", "front6", "front7", "front8","front9", "front10", "front11", "front12","front13", "front14", "front15", "front16","front17", "front18", "front19", "front20","front21", "front22", "front23", "front24","front25", "front26", "front27", "front28","front29", "front30", "front31", "front32"]
	server=random.choice(servers)
	while True:
		if input("Type Y or N: ").lower()[0] =="y":
			if input("Type Old or New: ").lower()[0] =="o":
				old="yes"
				om=omegle(server=server)
				om.Connect()
			else:
				old="no"
				om=omegle(server=server)
				om.Connect()
		else:
			break