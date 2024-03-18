#Write your code below this row 👇
even = 0
for numbers in range(1,101):
#for numbers in range(2, 101, 2)
    if(numbers %2== 0):
        even = numbers + even
print(even)