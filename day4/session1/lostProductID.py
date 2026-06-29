products=input("enter the product").split()
all_ids=set(products)
duplicates=set()
for id in products:
    if products.count(id)>1:
        duplicates.add(id)
lost_ids=all_ids-duplicates
print("lost ",lost_ids)