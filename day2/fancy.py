num=input()
increasing=True
decreasing=True
for i in range(len(num)-1):
    if int(num[i+1])!= int(num[i])+1:
        increasing=False
    if int(num[i+1])!= int(num[i])-1:
        decreasing=False
if increasing:
    print('inc fancy')
elif decreasing:
    print('dec fan')
else:
    print('not fancy')