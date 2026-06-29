products=eval(input("enetr the the dictionary :"))
choice=input("KEY/PRICE")
def get_value(item):
    return item[1]

if choice=="KEY":
    sorted_dict=dict(sorted(products.items()))
    print("Sorted Dictionary: ",sorted_dict)
elif choice=="PRICE":
    sorted_dict=(dict(sorted(products.items(),key=get_value)))    
    print=(sorted_dict)
else:
    print("Invalid Choice")