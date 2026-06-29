n=int(input("input"))
square=n*n
digits=len(str(n))
right=square%(10**digits)
left=square//(10**digits)
if left+right==n:
    print("keorekar num")
else:
    print("not keprekar")
    