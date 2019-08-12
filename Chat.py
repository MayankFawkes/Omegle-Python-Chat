import json
import requests
import time
class sendnow():
	def __init__(self):
		data=json.loads(open("key.json").read())
		self.server=data["server"]
		self.headers={
			"Origin": "https://www.omegle.com",
			"Referer": "https://www.omegle.com/",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
		}
		self.url="https://{}.omegle.com/send".format(self.server)
		self.data={}
		self.data["id"]=data["id"]
	def send(self,message):
		if message=="exit":
			self.url="https://{}.omegle.com/disconnect".format(self.server)
			r=requests.post(self.url,headers=self.headers,data=self.data)
			if r.text == "win":
				print("[{}] Disconnect".format(time.strftime("%d-%b %I:%M:%S %p")))
		else:
			self.data["msg"]=message
			r=requests.post(self.url,headers=self.headers,data=self.data)
			if r.text == "win":
				print("[{}]Sended: {}".format(time.strftime("%d-%b %I:%M:%S %p"),message))
if __name__ == '__main__':
	while True:
		mes=input("Type: ")
		app=sendnow()
		app.send(message=mes)