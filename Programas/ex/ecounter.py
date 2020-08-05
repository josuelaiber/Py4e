name = input ('Enter File:')
count=dict()
fh=open(name)
for line in fh:
    words=line.strip()
    if words.startswith('From:'):
        word=words.split()
        key=word[1]
        count[key]=count.get(key,0)+1
bigcount=None
bigEmail=None
for w,c in count.items():
    if bigcount is None or c>bigcount:
        bigEmail= w
        bigcount = c
print(bigEmail,bigcount)
