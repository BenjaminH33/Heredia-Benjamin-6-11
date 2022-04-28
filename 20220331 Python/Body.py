import requests
 
url = "http://www.boredapi.com/api/activity?type=recreational&#39;"
 
r = requests.get(url)
data = r.text
print(data)

import os
file = open("archivo1.txt", "w")
file.write("activity:Create a personal website,type:recreational,participants:1,price:0.1,link:,key:3141417,accessibility:0.12")
file.close()



