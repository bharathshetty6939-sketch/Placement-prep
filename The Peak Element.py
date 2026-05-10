data = list(map(int, input("Enter numbers separated by space: ").split()))
low = 0
high = len(data) - 1 
while low < high:
    mid = (low + high) // 2
    if data[mid] < data[mid + 1]:
        low = mid + 1 
    else:
        high = mid    
print("Peak element data is:", data[low])