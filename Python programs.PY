#Variable input method 
#name = "vidhi" 'declaring the values in the variable
# name = input("What is your name?")
# print(name)   'user needs to input the values
# name = input("what is your name?")
# length = (len(name))
# print(length)

#-----------------------------------------------------------------------------
#swapping the value of variables.
# a = input("enter the value of a:")
# b = input("enter the value of b:")

# c = a
# a = b
# b = c

# print("a:"+a)
# print("b:"+b)
#------------------------------------------------------------------------------


#----------------------------------- project 1 day 1---------------------------
# print("WELCOME to the band name generator!")
# city = input("Enter the city name you grew up in:\n")
# pet_name = input("Enter your pet name:\n")
# print("your bandname could be:"+ city +" "+pet_name)
#-------------------------------------------------------------------------------


# -----------------------------------# day 2 practice 1------------------------
# two_digit_number = input("Type a two digit number: ")
# # print(type(two_digit_number))
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
# # print(type(first_digit))
# # print(type(second_digit))
# result = int(first_digit) + int(second_digit)
# print(result)
#-------------------------------------------------------------------------------


# -----------------------------------#BMI CALCULATOR 2.2------------------------
# height = input("enter your height: ")
# weight = input("enter your weight: ")

# # print(type(height))
# # print(type(weight))

# weight_new = int(weight)
# height_new = float(height)
# # print(type(BMI))
# BMI = weight_new/height_new ** 2
# BMI = weight_new /(height_new * height_new)
# BMI_new = int(BMI)
# print(BMI_new)


# # 🚨 Don't change the code below 👇
# height = input("enter your height in m : ")
# weight = input("enter your weight in kg : ")
# # 🚨 Don't change the code above 👆

# # print(type(height))
# # print(type(weight))

# # weight_new = int(weight)
# # height_new = float(height)
# # print(type(BMI))
# # BMI = weight_new/height_new * height_new

# BMI = int(weight) /float(height)** 2
# BMI_new = int(BMI)
# print(BMI_new)
#------------------------------------------------------------------------------------


#------------------------------------LIFE IN WEEKS-------------------

# age = input("What is your current age?")
# x = 365
# y = 52
# z = 12

# # print(type(X))
# # print(type(Y))
# # print(type(Z))

# days_left   = (90-int(age))*x 
# weeks_left  = (90-int(age))*y
# months_left = (90-int(age))*z 

# print(f"You have {days_left} days,{weeks_left}weeks, and {months_left} months left.")
#---------------------------------------------------------------------------------------



#-------------------------------------TIP CALCULATOR----------------------

# print("Welcome to the tip calculator!")
# total_bill = input("What was the total bill? $")
# tip_input = input("How much tip would you like to give? 10, 12, or 15?")
# your_tip= float(tip_input) / 100
# final_tip = float(total_bill) * (1.00 + your_tip)
# no_people = input("How many people to split the bill?")
# bill_per_person = final_tip / float(no_people)
# result = round(bill_per_person, 2)
# result = "{:.2f}".format(bill_per_person)
# print("Each person should pay:$",result)

#----------------------------------------------------------------------------

# # if condition:
#     Statement
# else Condition:
#    Statement

#-----------------------------rollercoaster check-------------------------------------
# print("Welcome to the rollercoaster!")
# height = int(input("what is your height in cm?"))
# if height >= 120:
#     print("you can ride the Rollercoaster.")
#     age = int(input('what is your age?'))
#     if  age < 12:
#         bill = 5
#         print("you have to pay 5$.")
#     elif  age <= 18:
#         bill = 7
#         print("you have to pay 7$.")
#     elif age >=45 and age <= 55:
#         bill = 0
#         print("you have to pay 0$.") 
#     else:
#         bill = 8
#         print("you have to pay 12$.")
#     want_photo = input("do you want to take photo?Y or N.")
#     if want_photo == "Y":
#         bill += 3
#     print(f"your final bill is {bill}")
    
# else:
#     print("sorry, you have to grow your height befor you can ride the Rollercoaster.")
#-----------------------------------------------------------------------------------------



#---------------------------BMI-------------------------------------------------------
# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# # print(type(height))
# # print(type(weight))

# # weight_new = int(weight)
# # height_new = float(height)
# # print(type(BMI))
# # BMI = weight_new/height_new * height_new

# BMI = round(weight /height** 2)
# # BMI_new = int(BMI)
# # print(BMI)
# if BMI < 18.5:
#     print(f'Your BMI is {BMI},you are underweight')
# elif BMI < 25:
#     print(f'Your BMI is {BMI},you have a normal weight.')
# elif BMI < 30:
#      print(f'Your BMI is {BMI},you are slightly overweight.')
# elif BMI < 35:
#      print(f'Your BMI is {BMI},you are obese')
# else:
#      print(f'Your BMI is {BMI}, you are clinically obese')

#---------------------------------------------------------------------------------  

#--------------------------------------leap year----------------------------------
# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("not leap year")
#---------------------------pizza order -------------------------------------------------------

# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# large_pizza  =  25
# medium_pizza =  20
# small_pizza  =  15
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill+= 20
# else:
#     bill+= 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"your final bill is: ${bill}.")
#----------------------------------------------------------------------------------------------       

#---------------------------------------------love calculator-------------------------------------------------------
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

#Write your code below this line 👇

# LOWERCASE CONVERSION
# print(name1.lower())
# print(name2.lower())

# (name1.lower())
# (name2.lower())
# "angela".count("a")

#LOVE
# lower_case_name = name1.lower()
# love_name1 = (lower_case_name.count(f"l")+lower_case_name.count(f"o")+lower_case_name.count(f"v")+lower_case_name.count(f"e"))

# lower_case_name2 = name2.lower() 
# love_name2 = (lower_case_name2.count(f"l")+lower_case_name2.count(f"o")+lower_case_name2.count(f"v")+lower_case_name2.count(f"e"))     
# love_score = love_name1 + love_name2
# # print(love_score)

# #TRUE
# lower_case_name = name1.lower()
# true_name1 = (lower_case_name.count(f"t")+lower_case_name.count(f"r")+lower_case_name.count(f"u")+lower_case_name.count(f"e"))

# lower_case_name2 = name2.lower()
# true_name2 = (lower_case_name2.count(f"t")+lower_case_name2.count(f"r")+lower_case_name2.count(f"u")+lower_case_name2.count(f"e"))     
# true_score = true_name1 + true_name2
# # print(true_score)

# final_score = (f"{true_score}{love_score}")
# new_final_score = int(final_score)
# if new_final_score <= 10 or new_final_score >=90:
#     print(f"your score is {new_final_score}, you go together like coke and mentos.")
# elif new_final_score >=40 and new_final_score <= 50:
#     print(f"your score is {new_final_score}, you are alright together.")
# else:
#     print(f"Your score is {new_final_score}.")
# --------------------------------------------------------------------------------------------------------------------------------------------


# day-3 project -------------------------treasure island----------------------------

# '''Treasure Island
# Instructions
# Make your own "Choose Your Own Adventure" game. Use conditionals such as if, else, and elif statements to lay out the logic and the story's path in your program.

# To write your code according to my story, you can use this flow chart from draw.io to help you.

# However, I think the fun part is writing your own story 😊

# 🧞‍♂️ 🐊 🧙‍♂️ 🧟 🧚‍♂️ 🧝‍♂️ 🥷 🤖 👽 🙀

# That said if you'd like to continue with my example, feel free to use the text snippets below...

# Text Snippets from my example
# 'You're at a crossroad. Where do you want to go? Type "left" or "right"'
# 'You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
# "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
# "It's a room full of fire. Game Over."
# "You found the treasure! You Win!"
# "You enter a room of beasts. Game Over."
# "You chose a door that doesn't exist. Game Over."
# "You get attacked by an angry trout. Game Over."
# "You fell into a hole. Game Over."
# Escaping Characters
# If you want to use multiple sets of quotes inside a single string, you might have to "escape" some of them using the backslash \. You can see this in my first sentence: 'You're at a crossroad...'. More on escaping characters here.

# Extensions
# Have a think about how you might write your program to make a player's answers less case-sensitive. In other words, your code should work regardless of whether your user answers "left" or "Left".

# You can also add your own ASCII art. Just remember to add three single quotes ''' '''at the start and at the end of your artwork to turn it into a multi-line string.'''

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 
# cross_way = input('''You're at a crossroad. Where do you want to go? Type "left"  or "right".''')
# if cross_way == "left":
#     cross_way.lower()
#     wait_swim = input('''you've come to a lake. there is an island in the middle of the lake. type "wait" to wait to wait for a boat. type "swim"to swim across.''')
#     if wait_swim == "wait":
#         wait_swim.lower()
#         which_door =input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose.")
#         if which_door == "red":
#             which_door.lower()
#             print("burned by fire.Game over")
#         elif which_door == "blue":
#             print("eaten by beasts.Game over")
#         elif which_door == "yellow":
#             print("You win.")
#         else:
#             print("Game Over.")
#     else:
#         print("Attack by crocodile. Game Over.")
# else:
#     print("fall into a hole. game over.")

#------------------------------------------


# import random

# random_int = random.randint(1,5)
# print(random_int)


# random_float=random.random()*5
# print(random_float)

# Instructions
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

# When you run the code, just use a random number as the seed. e.g. 67346 It doesn't matter what you chose, 
# it's only for our testing code to check your work.

# There are many ways of doing this. But to practice what we learnt in the last lesson,
#  you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

# e.g. 1 means Heads 0 means Tails

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
# import random
# 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
# print("Toss the coin.")

# head_tails = random.randint(0,1)
# if head_tails == 1:
#     print("Heads")
# else:
#     print("Tails")


#------------------------------------------list--------------------------------------------------------
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# states_of_america.append("alexendra")
# print(states_of_america)
# states_of_america.sort()  

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

#--------------------------------------------------------------------------------------------------------
# Import the random module here
# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# rand_list = random.randrange(len(names))
# #random.randrange() method is used to generate a random number in a given range, we can specify the range to be 0 to the length of the list, and get the index, and then the corresponding value.
# rand_name = names[rand_list]
# print(rand_name+" is going to buy the meal today!")

#------------------------------------------------------------------------------------------------------------------

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[0][1])


#-------------------------------------------------------------------------------------------------------------------

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# # digit_ij = [int(x) for x in str(position)]
# # digit_ij[0][1]= 'x'
# # position1 = int(input("Where do you want to put the treasure? "))
# # position2 = int(input("Where do you want to put the treasure? "))
# position1 = int(position[0])
# position2 = int(position[1])
# position_int = int(position)
# map[position2-1][position1-1]='X'
#   or
# map[int(position.split(',')[0])][int(position.split(',')[1])]='x'
# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")
#-------------------------------------------------------------------------------------------------------------------

# -------------------------------------------rock paper and scissors -----------------------------------------------
# import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# #Write your code below this line 👇
# rsp_list = [rock,paper,scissors]
# Rsp = int(input("what do you choose? 0 for rock, 1 for paper or 2 for scissors: "))
# if(Rsp==0):
#     print(rock)
# elif(Rsp==1):
#     print(paper)
# else:
#     print(rsp_list[Rsp])
# print("\ncomputer chose:\n")
# random_choice= random.randint(0,2)
# computer = rsp_list[random_choice]
# print(computer)
# if Rsp == 0 and random_choice == 2:
#     print("YOU WIN.")
# elif Rsp == 1 and random_choice == 0:
#     print("YOU WIN.")
# elif Rsp == 2 and random_choice == 1:
#     print("YOU WIN.")
# elif Rsp == random_choice:
#     print("its a draw.")
# else:
#     print("YOU LOSE.")
#-------------------------------------------------------------------------------------------------------------------

# fruits = ["Banana","orange","mango","bluberry"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit+" shake")
# print(fruits)
            
#-------------------------------------------------------------------------------------------------------------------
# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇
# total = n + 1
# # print(total)
# ans = 0
# for values in student_heights:
#     ans = ans + values
#     # print(ans)
# div = ans / total
# print(round(div))   
#-------------------------------------------------------------------------------------------------------

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# j = 0 
# for i in student_scores:
#     if i > j:
#         j = i  
# print(f"The highest score in the class is: {j}")

#-------------------------------------------------------------------------------------------------------
#Write your code below this row 👇
# str1 = 'Fizz'
# str2 = 'Buzz'
# str3 = 'FizzBuzz'
# for numbers in range(1, 101):
#     if numbers % 3 == 0 and numbers % 5 == 0:
#         print(str3)
#     elif numbers % 3 == 0:
#         print(str1)
#     elif numbers % 5 == 0:
#         print(str2)
#     else:
#         print(numbers)
#-------------------------------------------------------------------------------------------------------