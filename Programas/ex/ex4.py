import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')

countmax=int(input('Enter count:'))
position=int(input('Enter position:'))
# Retrieve all of the anchor tags
i=0

while i<countmax:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    lst=list()
    for tag in tags:
        lst.append(tag.get('href', None))
    print(lst[position-1])
    url=lst[position-1]
    i=i+1
