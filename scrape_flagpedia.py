#!/usr/bin/env python3 

import subprocess as sb
import requests as r
from bs4 import BeautifulSoup
import time 

quality_code = "flags/w1160/"
url = "https://flagpedia.net/index"
dw_url = "https://flagpedia.net/data/" + quality_code

rq = r.get(url).text

soup = BeautifulSoup(rq, 'html.parser')

for picture in soup.find_all("picture"):
	flag_code = picture.source.get("srcset")[16:18]

	#print("wget "+str(dw_url)+str(flag_code)+".png")
	sb.run(["wget", str(dw_url)+str(flag_code)+".png" ])
    time.sleep(0.5) 
