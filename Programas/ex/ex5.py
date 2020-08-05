import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET



url = input('Enter location: ')

uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
num=list()
counts = tree.findall('.//count')
for item in counts:
    n=int(item.text)
    num.append(n)
print(sum(num))
