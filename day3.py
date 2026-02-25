#---2026 placement eligibility check bot
print("=============================================================================")
print("Dream company eligibility test")
print("=============================================================================")
name=input("Enter your name:")
cgpa=float(input("Enter your cgpa:"))
Backlogs=int(input("Enter the no of active backlogs:"))
HR_rank=int(input("Enter your hackerrank rank(out of 100):"))
if cgpa>=7.5 and Backlogs==0 and HR_rank>=70:
        print(f"Congrats {name} your eligible for your super dream company")
elif cgpa>=6 and Backlogs==0 and HR_rank>=50:
        print(f"congrats {name} your eligible for  your dream company")
else:
    print(f"sorry {name} you have to work hard to get your dream company")

print("=============================================================================")