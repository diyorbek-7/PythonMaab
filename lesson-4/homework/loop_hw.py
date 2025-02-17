import random
#1
list1 = [1, 1, 2]
list2 = [2, 3, 4]
l = []
for i in list1:
    if i  not in list2:
        l.append(i)
for i in list2:
    if i not in list1:
        l.append(i)
print(l)

##2
n=int(input("n="))
for i in range(n):
    if i <n:
        print(i**2)

#3
txt = 'abcabcdabcdeabcdefabcdefg'
b = 'aeiou'
count = 0
ans = ''
for i in range(len(txt)):
    count += 1
    ans += txt[i]
    if i != len(txt) - 1 and count>=3 and txt[i] not in b:
        b += txt[i]
        ans += '-'
        count = 0
print(ans)



#4
while True:
    att = 10
    an = {'Y', 'YES', 'y', 'yes', 'ok'}
    a = random.randint(1, 100)
    while att>0:
        n = int(input())
        if n>a:
            print('Too high')
        elif n<a:
            print('Too low')
        else:
            print('You guessed it right!')
            break

        att = att-1
    if att == 0:
        print('Lost!,wanna again?')
    else:
        print('Wanna play again?')
    answer = input('want to play again? ')
    if answer not in an:
        print('THanks for playing')
        break


#5
while True:
    print('Enter password:')
    password = input()
    upper = False

    for i in password:
        if i>='A' and i<='Z':
            upper = True
            break
    if len(password)<8:
        print('Password is too short')
    elif not upper:
        print('must contain an upper letter')
    else:
        print('Password is strong')
        break

#6
for i in range(2,100):
    isPrime = True
    for j in range(2,i):
       if i % j == 0:
           isPrime = False
           break
    if isPrime:
        print(i)



