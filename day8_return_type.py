def get_final_price(price,discount_percentage):
    discount_amount=(price*discount_percentage)/100
    final_price=(price-discount_amount)
    return final_price
price=float(input("Enter the price:"))
discount_percentage=float(input("Enter the discount percentage:"))
deal_price=get_final_price(price,discount_percentage)
print(f"The original price of laptop is {price} the deal price is {deal_price} ")