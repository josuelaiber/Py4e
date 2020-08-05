import re
name = input('Enter File:')
fh=open(name)
num=list()
for line in fh:
    line = line.rstrip()
    stuff=re.findall('([0-9]+)',line)
    if not stuff: continue
    for i in range(len(stuff)):
        n=float(stuff[i])
        num.append(n)
print(sum(num))
