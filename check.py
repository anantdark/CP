age = int(input('Enter your age'))
if age >7 and age < 80:
    print('You are welcome')
    if age >18:
        print('You are eligible to apply')
    elif age == 18:
        print('Prove your identity.')
    else:
        print('You are not eligible to apply.')
elif age >=80:
    print('Sorry you are too old')
else:
    print('Sorry you are too young.')

#CoDeD By AnAnT