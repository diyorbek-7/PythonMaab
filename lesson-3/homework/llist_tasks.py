#1
# list1 = [1,2,3,4]
# print(len(list1))
#2
# list1={1,2,3,4,5}
# suml = 0
# for i in list1:
#     suml += i
# print(suml)
#3
# list1 = [1, 2, 3]
# maxl = list1[0]
# for i in list1:
#     if i > maxl:
#         maxl = i
# print(maxl)
#4
# list1 = [1, 2, 3]
# minl = list1[0]
# for i in list1:
#     if i < minl:
#         minl = i
# print(minl)
#5
# list1 = [1, 2, 3]
# print(4 in list1)
#6
# list1 = [1,2,3]
# print(list1[0])
from operator import index

#7
# list1 = [1,2,3]
# print(list1[-1])

#8
# list1 = [1,2,3,4,5,6,7]
# newlist = list1[:3]
# print(newlist)
#9
# list1 = [1, 2, 3]
# newlist = list1[::-1]
# print(list1)
# print(newlist)

#10
# list1 = [1, 2, 3,8,4,7]
# newlist = sorted(list1)
# print(newlist)

#11
# list1 = [1, 2, 3,3,3,3,4,5,5,6,6]
# list2 = list(set(list1))
# print(list2)

#12
# list1 = [1, 2, 3]
# list1.insert(1, 4)
# print(list1)
#13
# list1 = [1, 2, 3]
# print(list1.index(2))

#14

# list1 = []
# print(len(list1))

#15
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# count = 0
# for i in list1:
#     if i %2 == 0:
#         count += 1
# print(count)
#16
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# count = 0
# for i in list1:
#     if i %2 != 0:
#         count += 1
# print(count)

#17
# list1 = [6, 7, 8, 9, 10]
# list2 = [1, 2, 3, 4, 5]
# print(list1 + list2)
#18
# list1 = [[1,2,3],[4,5,6],[7,8,9]]
# print([1,2,3] in list1)
#19
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list1[0] = 2
# print(list1)

#20
# list1 = [1, 2, 3, 4, 5,5,5,5,6,6,6,6,4,4]
# print(sorted(set(list1))[-2])
#21
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sorted(set(list1))[1])

#22
# list1=[1,2,3,4,5,6,7,8,9]
# list2 = []
# for i in list1:
#     if i%2==0:
#         list2.append(i)
# print(list2)

#23
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = []
# for i in list1:
#     if i %2!=0:
#         list2.append(i)
# print(list2)

#24
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(len(list1))

#25
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = len(list1)
# m = n//2
# print(list1[m] if n % 2==0 else list1[m-1],list1[m])

#27
# list1 = [[1,2,3],[4,5,6],[7,8,9]]
# sublist = list1[0]
# m = sublist[0]
# for i in sublist:
#     if i > m:
#         m = i
# print(m)

#28
# list1 = [[1, 2, 3],[ 4, 5, 6],[ 7, 8, 9, 10]]
# sublist = list1[0]
# m = sublist[0]
# for i in sublist:
#     if i < m:
#         m = i
# print(m)

#29
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list1[0]=None
# print(list1)
#30
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list1 == sorted(list1))


# #31
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# m = 3
# new_list = []
# for i in list1:
#     for _ in range(m):
#         new_list.append(i)
# print(new_list)

#32
# list1 = [1,2,5,4,6,8,5,3]
# list2 = [2,9,5,9,5,]
# print(sorted(set(list1) | set(list2)))

#33
# list1 = [1,2,3,4,4,5,6,8,4,5,69,4]
# el = 4
# ind = []
# for i in range (len(list1)):
#     if list1[i] == el:
#         ind.append(i)
# print(ind)

#34
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = 2
# rlist = list1[-k:] + list1[:-k]
# print(rlist)
#35
# list1 = list(range(2,45,4))
# print(list1)

# #36
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum = 0
# for i in list1:
#     if i > 0:
#         sum += i
# print(sum)


#37
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum = 0
# for i in list1:
#     if i < 0:
#         sum += i
# print(sum)

#38
# list1 = [1,2,3,4,5,5,3,2,1]
# print(list1==list1[::-1])

# #39
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = 4
# nestedsub=[]
# sub = []
# for i in list1:
#     sub.append(i)
#     if len(sub) == n:
#         nestedsub.append(sub)
#         sub = []
# if sub:
#     nestedsub.append(sub)
# print(nestedsub)

#40
# list1 = [1, 2,2,2, 3, 4, 1,5,5,5, 6, 7,7,7,7, 8, 9, 10]
# newlist = []
# for i in list1:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)















