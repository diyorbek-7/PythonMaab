
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats(universities):
    num = [i[1] for i in universities]
    tui = [i[2] for i in universities]
    return num, tui
def mean(a):
    return sum(a) / len(a)
def median(a):
    b = sorted(a)
    if len(b)%2 == 0:
        return b[len(b)//2]+b[len(b)//2-1]
    else:
        return b[len(b)//2]
e,f = enrollment_stats(universities)
v = sum(e)
w = sum(f)
print(f'Total students: {v}')
print(f'Total tution:{w}')
print(f'Student mean:{round(mean(e),2)}')
print(f'Student median:{median(e)}')
print(f'Tution mean:{round(mean(f),2)}')
print(f'Tution median:{median(f)}')