n=float(input('enter the mm of the rain :'))
if n<1:
    print('No Rain')
elif n<5:
    print('Light Rain')
elif n<10:
    print('Moderate Rain')
else:
    print('Heavy Rain')