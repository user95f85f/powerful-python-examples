#!/usr/bin/python3

#python3 getyoutube.py > a.txt
import requests
myResponse = requests.get("https://www.youtube.com")
print(myResponse.text)
