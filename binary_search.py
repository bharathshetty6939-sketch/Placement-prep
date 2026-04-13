usn = [101, 202, 303, 404, 505]
n = int(input("Enter the USN to be searched: "))

low = 0
high = len(usn) - 1
found = False

while low <= high:
    mid = (low + high) // 2  
    
    if usn[mid] == n:
        print(f"USN {n} exists at index {mid}")
        found = True
        break
    elif usn[mid] < n:
        low = mid + 1  
    else:
        high = mid - 1 

if not found:
    print("USN does not exist")