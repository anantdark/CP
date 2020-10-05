n = int(input('Enter any value to check if it is even/odd'))
if n%2==0:
    print('Number is even')
else:
    print('number is odd')

n = int(input('Enter any value to check if prime'))
if n==2:
    print('The number is prime')
else:
    for i in range(2, n):
        if n%i == 0:
            print('The number is not prime')
            break
        elif n%i !=0:
            print('The number is prime')
            break

n=int(input("Enter number to check if it is a palindrome:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

num = int(input('Enter number to check for armstrong'))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print('Number is an armstrong number')
else:
    print('Number is not an armstrong number')


#CoDeD By AnAnT