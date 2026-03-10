def get_unique_no():
    unique_no=[]
    n=[1, 2, 3, 2, 1, 5]
    for x in n:
      if n.count(x)==1:
         unique_no.append(x)
    return sum(unique_no)
         
print("Sum of unique no is",get_unique_no())

