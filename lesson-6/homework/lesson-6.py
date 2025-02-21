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

#Emoloyee Records Manager
with open('employees.txt',mode='a') as f:
    id = int(input('Enter employee ID: '))
    name = input('Enter employee name: ')
    position = input('Enter employee position: ')
    salary = int(input('Enter employee salary: '))
    f.write(f'{id},{name},{position},{salary}\n')
f.close()

####Menu Options


#Functional Requirements
#1
with open('employees.txt',mode='a') as f:
    id = int(input('Enter employee ID: '))
    name = input('Enter employee name: ')
    position = input('Enter employee position: ')
    salary = int(input('Enter employee salary: '))
    f.write(f'{id},{name},{position},{salary}\n')
f.close()

#2
with open('employees.txt', 'r') as file:
    print(file.read())

#3
def search_emp(id):
    with open('employees.txt', 'r') as file:
        for line in file:
            if line.split(',')[0]==id:
                print('employee found:\n',line)
            return
    print('employee not found')
id = input('Enter Employee ID: ')
search_emp(id)

#4
def update_info(id,name,position,salary):
    with open('employees.txt',mode='r') as f:
        lines = f.readlines()
    employee_found=False
    for i,line in enumerate(lines):
        if line.split(',')[0]==id:
            lines[i] = f'{id},{nname},{nposition},{nsalary}'
            employee_found=True
            break
    if employee_found:
        with open('employees.txt',mode='w') as f:
            f.writelines(lines)
        print('Employee updated successfully')
    else:
        print('Employee not found')




id=input('enter employee id:')
nname=input('enter employee name:')
nposition=input('enter employee position:')
nsalary=input('enter employee salary:')

update_info(id,nname,nposition,nsalary)


#5
def delete_employee(id):
    with open('employees.txt', 'r') as f:
        lines = f.readlines()
        updated_lines = [line for line in lines if not line.startswith(id + ',')]
    if len(updated_lines)<len(lines):
        with open('employees.txt', 'w') as f:
            f.writelines(updated_lines)
            print('Employee has been deleted')
    else:
        print('Employee not found')

id = input('Enter employee id: ')
delete_employee(id)


# Word frequency counter
#2
from collections import Counter
with open('sample.txt', 'r') as f:
    words = f.read().lower().strip().split()
word_counts = Counter(words)

#3
totalwords = sum(word_counts.values())
most = word_counts.most_common(5)
print(f'total words:', totalwords)
for i,j in most:
    print(i,':', j)

with open('word_count_report.txt', 'w') as f:
    f.write(f"Total words: {totalwords}\n")
    f.write('5 most common: ')
    for word, count in most:
        f.write(f"{word}: {count}\n")




