a=float(input("Enter the first value:"))
b=float(input("Enter the second value:"))
op=input("Enter the operator:")

if(op=="+"):
    print(f"Result of {a} {op} {b} is:",a+b)
elif(op=="-"):
    print(f"Result of {a} {op} {b} is:",a-b)
elif(op=="*"):
    print(f"Result of {a} {op} {b} is:",a*b)
elif(op=="/"):
    if(b==0):
        print("Alert :values cannot be divided by 0")
    else:
        print(f"Result of {a} {op} {b} is:",a/b)
elif(op=="//"):
    if(b==0):
        print("Alert :values cannot be // by 0")
    else:
        print(f"Result of {a} {op} {b} is:",a//b)



