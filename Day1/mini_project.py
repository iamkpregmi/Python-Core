#Write a python program for the generate bill according to dynamic products
rate_list = {
    'mac_book_air': 60000,
    'ipad': 34000,
    'iphone13': 43000,
    'iphone14': 55000,
    'iphone15': 80000
}
gst = int(18) #GST 18% fixed
order_list = {}

while True:
    search_product = input("Enter product name: ")
    qty = int(input('Quantity: '))
    if search_product in rate_list:
        rate = rate_list[search_product]
        sub_total = rate * qty
        order_list[search_product] = sub_total
    else:
        print("Product not found.")

    is_continue = input("Do You want to continue(Y/N): ")
    if is_continue=='n' or is_continue == 'N':
        break


sub_total = 0
print("----------------------------------------------")
print("                Your order list               ")
print("----------------------------------------------")

for item in order_list:
    print(item,":",order_list[item])
    sub_total += order_list[item]
total = sub_total+((sub_total*gst)/100)

print("----------------------------------------------")
print("Sub Total: ",sub_total, ", Total Price", total)
print("----------------------------------------------")


