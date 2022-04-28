import requests

URL = 'http://www.boredapi.com/api/activity?type=recreational&#39;'
data = requests.get(URL)
data = data.text

with open ('archivo2.txt', "w") as f:
    f.write(data)


