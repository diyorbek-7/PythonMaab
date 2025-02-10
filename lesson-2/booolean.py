#1
a = input('Enter name: ')
b = input('Enter password: ')
if a and b:
    print('yes')
else :
    print('no')

#2
a = input()
b = input()
if a == b:
    print("yes")

#3
a = int(input())
if a % 2 ==0:
    print("even")
else:
    print("odd")

#4
a = int(input())
b = int(input())
c = int(input())
if a != b and a != c and b != c:
    print("different")

# 5
a = input()
b = input()
print('yes' if len(a)==len(b) else 'no')

#6
a = int(input())
print('divisable' if a%3==0 and a%5==0 else 'not divisable')


#7
a = int(input())
b = int(input())
print('yes' if a+b>50.8 else 'no')
print('YES' if a<20 and a>10 and b<20 and b>10 else 'no')
