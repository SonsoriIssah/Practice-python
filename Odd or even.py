val = int(input('Enter a valber: '))
check = int(input('Enter a valber as dividend: '))

if val%2 == 0:
    print(True)
else:
    print(False)

if val%4 == 0:
    print(f'{val} is a multiple of 4')




if val%check == 0:
    print(f'{val} is divided evenly by {check}')

else:
    print(f'{val} is not divided evenly by {check}')