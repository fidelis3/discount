def calculate_discount(price,discount_percent):
    if discount_percent>=20:
       discounted_price=price-(price*(discount_percent/100))
       return discounted_price
    else:
        return price
original_price=float(input("enter the original price of item:"))
discount_percentage=float(input("enter the discount percentage:"))
final_price=calculate_discount(original_price,discount_percentage)
if final_price==original_price:
    print(f"no discount applied.Final price:")
else:
    print(f"final price after applying{discount_percentage}% discount:${final_price}")
    


