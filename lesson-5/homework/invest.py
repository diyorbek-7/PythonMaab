
def invest(amount, rate, years):
    return float(round(amount * (1 + rate)**years,2))
a = float(input())
b = float(input())
c = int(input())
invest(a, b, c)
for i in range(1,c+1):
    print(f"year {i}: {invest(a,b,i)}")