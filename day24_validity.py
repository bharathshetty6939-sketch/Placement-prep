N=int(input("Enter the no of phone no:"))
for _ in range(N):
    number=input()
    if number[0] in ['7','8','9'] and len(number)==10 and number.isdigit():
       print("Yes")
    else:
        print("No")

2