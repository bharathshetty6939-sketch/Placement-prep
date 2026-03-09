n=[4, 16, 25, 33, 49, 9]
result=[]
for num in n:
    if num>10:
        root=num**0.5
        if root.is_integer():
         result.append(num)
print(result)
