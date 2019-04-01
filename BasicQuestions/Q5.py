# python 3

number = int(input("Enter any number: "))

# prime number is always greater than 1
if number > 2:
    for i in range(3, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
        else:
            print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")
