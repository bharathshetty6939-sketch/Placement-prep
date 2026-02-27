n=int(input("Enter the number of server that you want to check:"))
for i in range (1,n+1):
    if(i%2==0):
      print(f" Server {i} : STATUS ONLINE (Secured).....")
    else:
      print(f" Server {i}: STATUS OFFLINE (Needs Check) ❌....")


