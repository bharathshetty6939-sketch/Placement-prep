data=[64, 25, 12, 22, 11]
for i in range(len(data)):
    min_indx=i
    for j in range(i+1,len(data)):
        if data[j]<data[min_indx]:
            min_indx=j
        data[i],data[min_indx]=data[min_indx],data[i]
print("The sorted data is",data)
