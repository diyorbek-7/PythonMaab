t1=(1,2,3,4,4,5,6,8,4,5,6)
t2 = (1,2,4,5,4,5,6,5,8,4,5,3,1,1)

#1
e = 4
print(t1.count(e))

# #2
m = t1[0]
for i in t1:
    if i > m:
        m = i
print(m)
#3
m = t1[0]
for i in t1:
    if i < m:
        m = i
print(m)

#4
e = 1
print(e in t1)

#5
print(t1[0] if t1 else "empty")

#6
print(t1[-1] if t1 else "empty")

#7
print(len(t1))

#8
t = tuple(t1[:3])
print(t)

#9
t = t1+t2
print(t)

#10
print(t1 if t1 else "Empty")

#11
e = 4
ind = []
for i in range (len(t1)):
    if t1[i] == e:
        ind.append(i)
print(ind)

#12
increasing = sorted(set(t1))
print(increasing[-2] if len(increasing) > 1 else "no 2nd largest")

#13
dec = sorted(set(t1))
print(dec[2] if len(dec) >=2 else "no 2nd smallest")

#14
t = (1,)
print(len(t))
print(type(t))

#15
list1 = [1,2,3,4,5,6,8,4,5,3,1,1]
t = tuple(list1)
print(t)

#16
m = sorted(set(t1))
print(m == t1)

#17
t = ((1,2,3),(4,5,6),(7,8,9))
t12 = t [1]
m = t12[0]
for i in t12:
    if i > m:
        m = i
print(m)

#18
t = ((1,2,3),(4,5,6),(7,8,9))
t12 = t[0]
g = t12[0]
for i in t12:
    if i < g:
        g = i
print(g)

#19
t = 5
for i in range(len(t1)):
    if t1[i] == t:
        print(t1[:i]+t2[:i])
        break

#20
#-


#21
n = 2
l = []
for i in t1:
    for j in range(n):
        l.append(i)
t = tuple(l)
print(t)

#22
n = 1
m = 11
l = []
for i in range(n,m+1):
    l.append(i)
t = tuple(l)
print(t)

#23
l = t1[::-1]
print(l)

#24

t = (1,2,3,4,3,2,1)
print(t[::]==t[::-1])

#25
l = []
for i in  t1:
    if i not in l:
        l.append(i)
t = tuple(l)
print(t)


