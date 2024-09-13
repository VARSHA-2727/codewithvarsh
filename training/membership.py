coupon_codes={"new50":0.3,"diwali23":0.2,"dasara49":0.7}
product_p={"laptop":50000,"watch":3000,"tab":20000}
prod=input("enter the product:")
cc=input("enter the coupon_code")
if prod in product_p:
    if cc in coupon_codes:
        final_price=product_p[prod]*(1-coupon_codes[cc])
    else:
       final_price=product_p[prod]
    print("final price=",final_price)
else:
    print("no such product exists")
    