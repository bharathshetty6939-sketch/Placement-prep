nums = [10, 20, 30, 40, 50, 60, 70]
n=int(input("Enter the numbers whos index to be searched:"))
low=0
high=len(nums)-1
found=False
while low<=high:
    mid=(low+high)//2
    if nums[mid]==n:
        print(f"number{n} is at  the index :{mid}")
        found=True
        break
    elif nums[mid]<n:
        low = mid + 1  
    else:
        high = mid - 1 
if not found:
    print("number does not exist")

