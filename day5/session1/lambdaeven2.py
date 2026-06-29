number=list(map(int,input("enter the digit").split()))
even=list(filter(lambda x:x%2==0,number))
print(even)