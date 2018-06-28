'''Output numbers from 1 to x. If the number is divisible by 3, replace it with “Fizz”. If it is divisible by 5,
replace it with “Buzz”. If it is divisible by 3 and 5 replace it with “FizzBuzz”.'''

#check on the range of values x can be e.g. negative?
for number in range(1, 20):
    if number % 3 == 0  and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)