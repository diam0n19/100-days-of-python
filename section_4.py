import random  #-----------> random is a module within python, we can make our own module and import it.

# random_integer = random.randint(1, 10) #----------> this gives us a random integer, e.g 1 to 10
# print(random_integer)
# random_float = random.random() * 5 #---------> this gives us a random float between 0 to 5
# print(random_float)

# headtail = random.randint(0, 1)
# if headtail == 0:
#     print("Tails")
# else:
#     print("Heads")

#a list in python is indicated by [], while a dict. is {}

# name = ["alem", "alan", "bab", "baboon", "fiona", "moose", "bald", "shmee", "vajaya", "tricia", "zhu"]

# # name[1] = "alemu"     #-------> this changes the value of the specific list number

# name.append("monk")     #---------> append adds a value into the list

#name.extend(["lulu, "jeff"])     #-------> this adds onto and extends the current list

# print (name[1])  #--------> remember the list starts at 0, and negative numbers go from last to first

# numofnames = len(name)

# person = random.randint(0, numofnames - 1)     #-------> remember to subtract 1

# print ((name[person]) + " is going to pay for our food")

# phone = ["iphone", "samsung", "oppo", "huawei"]                   
# countries = ["us", "china", "russia", "japan"]

# country_phone = [phone, countries]                      #----------> this is called a nested list

# print (country_phone)

# print (country_phone[1][1])     #------> this would give us the value 'china' [list] [value]

# line_1 = ["A1", "B1", "C1"]
# line_2 = ["A2", "B2", "C2"]
# line_3 = ["A3", "B3", "C3"]
# num_map = [line_1, line_2, line_3]
# print ("pick a spot")
# place = input("where do you want to place your number? ")
# letter = place[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# num_index = int(place[1]) - 1
# num_map[num_index][letter_index] = "X"

# print (f"{line_1}\n{line_2}\n{line_3}")

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

# player = int(input("Type \"0\" for rock, \"1\" for paper, or \"2\" for scissors: "))
# pc = random.randint(0, 2)

# if player == 0:
#     print (f"You choose rock\n{rock}")
#     if pc == 2:
#         print (f"PC choose scissors\n{scissors}You Won!")
#     elif pc == 1:
#         print (f"PC choose paper\n{paper}You Lost!")
#     else:
#         print (f"PC choose rock\n{rock}Its a Tie!")
# elif player == 1:
#     print (f"You choose paper\n{paper}")
#     if pc == 2:
#         print (f"PC choose scissors\n{scissors}You Lost!")
#     elif pc == 1:
#         print (f"PC choose paper\n{paper}Its a Tie!")
#     else:
#         print (f"PC choose rock\n{rock}You Win!")
# else:
#     print (f"You choose scissors\n{scissors}")
#     if pc == 2:
#         print (f"PC choose scissors\n{scissors}Its a Tie!")
#     elif pc == 1:
#         print (f"PC choose paper\n{paper}You Win!")
#     else:
#         print (f"PC choose rock\n{rock}You Lost!")
