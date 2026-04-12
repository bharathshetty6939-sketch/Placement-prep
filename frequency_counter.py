word = "engineering"
count={}
for char in word:
    if char in count:
        count[char]+=1
    else:
        count[char]=1;
print("Character frequency",count)