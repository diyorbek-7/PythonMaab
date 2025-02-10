#1
a = input('name:')
b = int(input('birth year:'))
print(2024-b)



#3
a = input()
print(len(a))
print(a.upper())
print(a.lower())

#4
a = input()
if a==a[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#55
a= input()
count1=0
count2=0
for i in a:
    if i=='a'or i=='i'or i=='e' or i == 'o' or i == 'u' or i == 'A' or i == 'I' or i == 'E' or i == 'O' or i == 'U':
        count1+=1
    else:
        count2+=1
print('vovels:',count1,'consonants:',count2)

#6
a = input()
b = input()
if a in b:
    print(f"{a} is in {b}")
else:
    print(f"{a} is not in {b}")

#7
a = input('Input sentence:')
b = input('replace:')
c = input('with:')
print(a.replace(b,c))

#8
a = input()
print(a[0],a[-1])

#9
a = input()
print(a[::-1])

#10
a = input()
print(len(a.split()))

#11
a = input()
for i in a:
    if i >= '0' and i <= '9':
        print("yes")
        break
else:
    print("no")

#12
a=input()
words = a.split()
b = ','.join(words)
print(b)

#13
a = input()
print(a.replace(' ', ''))

#14
a = input()
b = input()
print('equal'if a == b else 'not equal')

#15
a = input()
result = ''
for i in a.split():
    result += i[0]
print(result.upper())


#16
str = input()
char =input()
for i in str:
    if i == char:
        str1 = str.replace(i,'')
print(str1)

#17
str = input()
for i in str:
    if  i=='a'or i=='i'or i=='e' or i == 'o' or i == 'u' or i == 'A' or i == 'I' or i == 'E' or i == 'O' or i == 'U':
        str=str.replace(i,'*')
print(str)

#18
str = input()
print(str.split()[0],str.split()[-1])


