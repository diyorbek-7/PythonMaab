def c(sr,sp):
    while True:
        yield sr
        sr+=sp
a = c(1,2)
for _ in a:
    print(next(a))