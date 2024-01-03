print("=======================Computer Bazar====================")
print("1. Dell (Rs:20000)  2.Toshba (Rs:30000)  3.Mac (Rs:50000)")
print("=========================================================")
product_name=''
quantity=0
dell_price=0
toshba_price=0
mac_price=0
option = int(input("Enter your option: "))
if option == 1:
    quantity = int(input("Enter quantity: "))
    product_name = "Dell"
    dell_price = quantity*20000
elif option == 2:
    quantity = int(input("Enter quantity: "))
    product_name = "Toshba"
    toshba_price = quantity*30000
elif option == 3:
    quantity = int(input("Enter quantity: "))
    product_name = "Mac"
    mac_price = quantity*50000
else:
    print("Invalid option")
    exit()

print("=============Delivery Option================")
print("1. Home Delivery (Rs:100)  2. Self Pickup (Rs:0)")

delivery_price=0
delivery_option = int(input("Enter delivery option: "))
if delivery_option == 1:
    delivery_price = 1000


print("=========== Packing Option ================")
print("1. Plastic (Rs:500)  2. Bag (Rs:2000)  3.Gift Box (Rs:5000)  4.None")
packing_price=0
packing_option = int(input("Enter packing option: "))
if packing_option==1:
    packing_price = 500
elif packing_option==2:
    packing_price = 2000
elif packing_option==3:
    packing_price = 5000
else:
    packing_price = 0

total = dell_price+toshba_price+mac_price
tax_amount=0

print("=========== Address ================")
print("1. Kathmandu (Tax:13%)  2. Lalitpur (Tax:0)  3.Bhaktapur (Tax:0) ")
tax_option = int(input("Enter tax option: "))
if tax_option==1:
    tax_amount = total*0.13

grand_total = total+tax_amount+delivery_price+packing_price

print("=============Invoice================")
print("Product Name: ",product_name)
print("Quantity: ",quantity)
print("Total: ",total)
print("Tax Amount: ",tax_amount)
print("Delivery Price: ",delivery_price)
print("Packing Price: ",packing_price)
print("Grand Total: ",grand_total)
print("====================================")