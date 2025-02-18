#zero check decorator
def check(func):
    def wrapper(a,b):
        if b == 0 :
            return 'Denominator can\'t be zero'
        else:
            return func(a,b)
    return wrapper
@check
def div(a,b):
    return a/b
print(div(2,3))


#Emoloyee Records manager
with open('employees.txt',mode='a') as f:
    id = int(input('Enter employee ID: '))
    name = input('Enter employee name: ')
    position = input('Enter employee position: ')
    salary = int(input('Enter employee salary: '))
    f.write(f'{id},{name},{position},{salary}\n')
f.close()

#