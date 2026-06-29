n=int(input("Sample Input: "))
if n<=100:
    print(n*1.50)
elif 200>=n>100:
    print(150+(n-100)*2.50)
else:
    print(400+(n-200)*4)
    

