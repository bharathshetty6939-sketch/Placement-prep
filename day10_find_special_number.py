def get_special_number():
    result=[]
    for i in range(1,101):
        if i%7==0 and i%5!=0:
            result.append(i)
    return result
final_list=get_special_number()
print(f"the length of the list is {len(final_list)}")
print(f"numbers of list is :{final_list}")
