# > < >= <= == !=

# '%' modulo, which gives the remainder after division

# number = int(input("Give me a number: "))

# if number % 2 == 0:
#     print("Your number is even")
# else:
#     print("Your number is odd")

# print ("Welcome to the Carnival!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride the roller coaster!")
#     age = int(input("How old are you? "))
#     if age <= 12:
#         print ("Please pay $7.")
#     elif age >= 45 and age <= 55:
#         print ("You can ride for free")
#     elif age >= 18:               #---------------> this serves as a continuation
#         print ("please pay $12.")
#     else:
#         print ("please pay $9.")
# else:
#     print("You're not tall enough")

# weight = int(input("what is your weight in kg? "))
# height = float(input("your height in meters? "))
# bmi = (weight/(height**2))
# bmi = round(bmi, 2)
# if bmi<18.5:
#     print (f"your bmi is {bmi}, You are underwight")
# elif bmi<25:
#     print(f"your bmi is {bmi}, You are normal weight")
# elif bmi<30:
#     print(f"your bmi is {bmi}, You are slightly overweight")
# elif bmi<35:
#     print(f"your bmi is {bmi}, You are obese")
# else:
#     print(f"your bmi is {bmi}, You are clinically obese")

# year = int(input("Give me a year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year %400 == 0:
#             print("Leap Year")
#         else:
#             print("Not A leap Year")
#     else:
#         print("Leap Year")        
# else:
#     print("Not A Leap Year")        

# s:15 m:20 l: 25     pep s:2 pep m or l:3 cheese: 1
# print ("Welcome to Python Pizza!")
# size = input("What size pizza would you like? S, M, or L ")
# pepperoni = input("Do you want pepperoni? Y or N ")
# cheese = input("Would you like extra cheese? Y or N ")
# total = 0
# if size == "S":
#     total += 15
#     if pepperoni == "Y":
#         total += 2
#         if cheese == "Y":
#             total += 1
#             print (f"Your total is ${total}.")
#         else:
#             print (f"Your total is ${total}.")
#     else:
#         print(f"Your total is ${total}.")
# elif size == "M":
#     total += 20
#     if pepperoni == "Y":
#         total += 3
#         if cheese == "Y":
#             total += 1
#             print (f"Your total is ${total}.")
#         else:
#             print (f"Your total is ${total}.")
#     else:
#         print(f"Your total is ${total}.")
# elif size == "L":
#     total += 25
#     if pepperoni == "Y":
#         total += 3
#         if cheese == "Y":
#             total += 1
#             print (f"Your total is ${total}.")
#         else:
#             print (f"Your total is ${total}.")
#     else:
#         print(f"Your total is ${total}.")


# print ("Welcome to Python Pizza!")
# size = input("What size pizza would you like? S, M, or L ")
# pepperoni = input("Do you want pepperoni? Y or N ")
# cheese = input("Would you like extra cheese? Y or N ")
# total = 0
# if size == "S":
#     total += 15
# elif size == "M":
#     total += 20
# else:
#     total += 25
# if size == "S":
#     if pepperoni == "Y":
#         total += 2
#     else:
#         total += 3
# if cheese == "Y":
#     total += 1
# print (f"Your total is ${total}.")

# name_1 = input("name1: ")
# name_2 = input("name2: ")
# combine_name = (name_1 + name_2)
# lower_name = combine_name.lower()
# lett = 0
# lt = 0
# letters = {"t","r","u","e"}
# for let in lower_name:
#     if let in letters:
#         lett +=1
# love = {"l","o","v","e"}
# for ltt in lower_name:
#     if ltt in love:
#         lt += 1
# combine = (str(lett) + str(lt))
# combine = int(combine)

# if combine <10 or combine >90:
#     print(f"Good, Your score is {combine}")
# elif combine >= 40 and combine <= 50:
#     print(f"Decent, Your score is {combine}")
# else:
#     print(f"Your score is {combine}")

# print ("Welcome to Treasure Island.\nYour mission is to find the hidden treasure.")
# start = input("would you like to begin the treasure hunt? \"Yes\" or \"No\" ")
# start = start.lower()
# if start == "yes":
#     one = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" ")
#     one = one.lower()
#     if one == "left":
#         island = input("You've reached an island full of snakes, would you like to \"swim\" or \"wait\"? ")
#         island = island.lower()
#         if island == "swim":
#             door = input("You've swam into a island with three colored doors, \"Red\", \"Green\", or \"Blue\", which would you like to open? ")
#             door = door.lower()
#             if door == "green":
#                 print("Congrats! You've found the treasure.")
#             elif door == "red":
#                 print ("A baboon ate you alive")
#             else:
#                 print("You opened a door full of bombs")
#         else:
#             print("The snakes ate you alive")
#     else:
#         print("You got hit by a tsunami")
# else:
#     print("Nice Sailing")











