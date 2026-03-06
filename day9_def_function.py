def get_stats(numbers):
    if not numbers:
        return 0,0
    lowest=min(numbers)
    highest=max(numbers)
    return lowest,highest
my_data=[10,23,3,56]
low,high=get_stats(my_data)

print(f"the lowest number is: {low}\nand highest number is:{high}")