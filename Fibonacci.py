n=[]
a,b=0,1
for _ in range(10):
    n.append(a)
    a,b=b,a+b
print("Fibonacci number is",n)


