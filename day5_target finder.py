secret_id=int(6);
n=int(input("Enter the Secret ID (From 1 to 20):"))
for i in range(1,n+1):
    print(f"Scanning System ID: {i}...")
    if(secret_id==i):
       print("TARGET LOCATED! Security protocol initiated. ")
       break;

