import random
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:           #--------> for loop
#     print(fruit)
#     print(fruit + " Pie")      

# student_height = input("This is a string").split(" ")
# student_height = ["156", "178", "165", "171", "187"]
# for i in range (0, len(student_height)):
#     student_height[i] = int(student_height[i])
# total = 0
# for height in student_height:
#     total += height
# average = total//len(student_height)
# average = round(average)

# print(f"Total height is {total}\nnumber of students is {len(student_height)}\naverage height is {average}")

# student_scores = ["78","65","89","86","55","91","64","89"]
# for i in range (0, len(student_scores)):
#     student_scores[i] = int(student_scores[i])
# highscore = 0
# for score in student_scores:
#     if score > highscore:
#         highscore = score
# print (highscore)
                                                                    #start  #stop  #step
# for number in range(1,11,2):      #-------add a extra number         #(1,    11,     2) 
#     print(number)

# total = 0
# for num in range(1,101):
#     total += num
# print(total)

# totaleven = 0
# for numb in range(0,11,2):
#     totaleven += numb
# print (totaleven)

# for num in range(1,101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# nums = ["0","1","2","3","4","5","6","7","8","9"]
# special = ["!","@","$","#","%","&","*","(",")","+"]
# print("Welcome to the PyPassword Generator!")
# letters = int(input("How many Letters would you like in your password?\n")) #4
# symbols = int(input("How many Symbols would you like?\n")) #4
# numbers = int(input("How many Numbers would you like?\n")) #4

# password = ""
# for let in range(1,letters+1):
#     password += random.choice(alphabets)
# for sym in range(1,symbols+1):
#     password += random.choice(special)                  #----------> random.choice() chooses a random value
# for num in range (1,numbers+1):
#     password += random.choice(nums)                     
# password = ''.join(random.sample(password,len(password)))        #''.join(random.sample(,len())))    randomize the values
# print(password)















