
print('Enter a temperature in degrees F:')
def convert_cel_to_far(a):
    return round(a * 1.8 + 32,2)
def convert_far_to_cel(a):
    return round((a - 32)/ 1.8,2)
t1 = float(input())
print(f"{t1} degrees in F = {convert_far_to_cel(t1)} degress in C")
print('Enter a temperature in degrees C:')
t2 = float(input())
print(f"{t2} degrees C = {convert_cel_to_far(t2)} degrees F")


