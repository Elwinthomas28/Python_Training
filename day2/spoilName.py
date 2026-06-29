name=input("enter the name")
mid=len(name)//2
firstpart=name[:mid]
secpart=name[mid:]
revfirstpart=firstpart[::-1]
revsecpart=secpart[::-1]
result=revfirstpart+revsecpart
print(result)

