import json
import urllib.request, urllib.parse, urllib.error


url = input('Enter location: ')
n=list()
uh = urllib.request.urlopen(url)
data = uh.read()
info = json.loads(data)
for u in info['comments']:
    n.append(u['count'])
print(sum(n))
