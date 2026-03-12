def digit_root(n):
    while n>9:
        sum_digits=0
        while n>0:
            sum_digits +=n % 10
            n =n // 10
        n=sum_digits
    return n
print("The digit root is",digit_root(987))