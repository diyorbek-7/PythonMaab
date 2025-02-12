d1 = {'v2':'k1','v1':'k2','v3':'k3'}
d2 = {'a1':'b1','a2':'b2','a3':'b3'}
d3 = {1:1,2:2,3:3}
k ='v1'
#1
k = "v1"
if k in d1:
    print(d1[k])
else:
    "not found"

#2

#3
print(len(d1))
l = list(d1.keys())
print(l)

#4
print(bool(k in d1))



#5
l = list(d1.values())
print(l)

#6
d = dict(d1 | d2)
print(d)

# #7
if k in d1:
    d1.pop(k)
    print('removed')
else:
    print('not found')
print(d1)

#8
d = dict()
print(type(d))

#9
if d1:
    print('not empty')
else:
    print('empty')

#10
if k in d1:
    p = (k,d1[k])
    print(p)
else:
    print('no key')

# #11
d1[k] = 'c1'
print(d1)

#12
c = list(d1.values()).count("k1")
print(c)

#13
k = {}
for  n,m in d1.items():
    k[m]=n
print(k)

#14
a = 'k2'
l = []
for n,m in d1.items():
    if m==a:
        l.append(n)
print(l)

#15
l=[1,2,3,4,5]
l2=[1,2,3,4,5]
d = dict()
for i in range(len(l)):
    d[l[i]]=l2[i]
print(d)

#16
for i in d1.keys():
    if type(i)==dict:
        print(True)
        break
else:
        print(False)

#17
d = {1: 'v', 2: 'v', 3: {'v1':'k1','v2':'k2','v3':'k3'}}
n = d[3]['v1']
print(n)

#18
k = 'v1'

if k in d1 :
        v = d1[k]
else:
        v = 'default'
print(v)

#19
c = len(set(d1.values()))
print(c)

#20
d = dict(sorted(d1.items()))
print(d)

#21


#22
filtr = {}
for k,v in d3.items():
    if v > 2:
        filtr[k] = v
print(filtr)

#23
for i in d1:
    if i in d2:
        print(True)
    else:
        print(False)

#24
t = ((1,'a'),(2,'b'),(3,'c'))
d = {}
for i,j in t:
    d[i] = j
print(d)

#25
for i,j in d1:
    pair = (i,j)
    break
print(pair)

