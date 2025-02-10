#1
n = float(input("Enter a number: "))
print(round(n, 2))

#2
a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))
print(max(a,b,c))
print(min(a,b,c))

#3
a = float(input())
m = int(a*1000)
cm = int(a*100000)
print(m,'metres',cm,'centimeters')

#4
a = int(input())
b = int(input())
print(int(a/b))
print(a%b)

#5
a = float(input())
b = (9/5*a)+32
print(b)

#6
a=int(input())
print(a%10)

#7
a = int(input())
if a % 2 == 0:
    print("even")
else:
    print("odd")