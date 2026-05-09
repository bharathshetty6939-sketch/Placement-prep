def reverse_list(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
data=[1,2,3,4,5]
k=int(input("Enter the steps:"))
n=len(data)
reverse_list(data,0,n-k-1)
reverse_list(data,n-k,n-1)
reverse_list(data,0,n-1)
print("Array after rotation is:",data)