import requests

y = requests.get("https://www.py4e.com/code3/geodata.zip")
print(y.content)