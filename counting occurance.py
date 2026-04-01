data = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count={}
for x in data:
    if x in count:
        count[x]+=1;
    else:
        count[x]=1;
print(count)
