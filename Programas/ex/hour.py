name = input('Enter File:')
fh=open(name)
hour=dict()
lst=list()
for line in fh:
    words=line.strip()
    if  '@' in words and '2008' in words and 'From' in words :
        k=words.split()
        hourk=k[5]
        k=hourk.split(':')
        time=k[0]
        hour[time]=hour.get(time,0)+1
for v, k in hour.items():
    lst.append((v,k))
lst=sorted(lst)
for v in lst:
    (i,j)=v
    print(i, j)
