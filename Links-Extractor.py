import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

cntxt = ssl.create_default_context()
cntxt.check_hostname = False
cntxt.verify_mode = ssl.CERT_NONE


url = input("Enter an address: ")
html = urllib.request.urlopen(url, context=cntxt).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get("href", None))