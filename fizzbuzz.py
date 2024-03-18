#Write your code below this row 👇
str1 = 'Fizz'
str2 = 'Buzz'
str3 = 'FizzBuzz'
n = input("Input: n = ")
n = int(n)
for numbers in range(n):
    if numbers % 3 == 0 and numbers % 5 == 0:
        numbers = print(str3)
    elif numbers % 3 == 0:
        numbers = print(str1)
    elif numbers % 5 == 0:
        numbers = print(str2)
    else:
        print(numbers)