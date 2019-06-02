#imports
import requests
from urllib.request import Request, urlopen
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

#var initialization
index=0

#we have to use the following method to avoid problems with the cookies and CAPATCHA. Otherwise we could just get the info with BeatifulSoup HTML Parser
req = Request('https://www.hltv.org/results', headers={'User-Agent': 'Chrome/74'})
web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')
while index < len (webpage):
    index=print(webpage.find('result-con'))
    if index == -1:
            break
    print('result-con found at', index)
    index =+10  # +10 due to the length of results-con

#print(webpage)


file =open("HLTVResults.txt", "w",encoding="utf-8")
file.write(str(webpage))
file.close()

#https://github.com/leokassio/Data-Collecting/blob/master/hltv-crawler.py


