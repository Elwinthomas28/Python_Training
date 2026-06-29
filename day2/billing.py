n=int(input("enter the number of ticket"))
p=200
st=input("student y/n :")
if st=="y":
    if n<15:
        print(n*p*95/100)
        print("student discount")
    else:
        print(n*p*75/100)
        print("25% discount")
else:
    if n<15:
        print(n*p)
        print("no discount")
    else:
        print(n*p*80/100)
    