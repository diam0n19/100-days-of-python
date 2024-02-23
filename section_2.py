#print ("Hello"[0])     #[0] is subscripting, which gives us the letter at index 0      # the space between also counts as a index

#integers are whole numbers, float are decimals, and boolean is True or False

#print ("123 + 345") gives us "123345" but print (123 + 345) gives us the actual sum

#print (80 + float(100.5))

# number = input("Give me a two digit number: ")

# value = (int(number[0]) + int(number[1]))

# print (value)

#print (4 ** 4) ----> 4^4

#print (3*3+3/3-3) ---> 7             (3*(3+3)/3-3) -----> 3

# weight = int(input("What is your weight?"))
# height = float(input("What is your height?"))

# bmi = (weight / (height**2))

# print (int(bmi))

# int turns float into a whole number                     # print(round(8/3)) round it down or up          (round(8/3 , 2) round it two the second decimal

#print(8//3) this is floor division, which gives us the whole number instead of remainders

# score += 1 -----> score = score + 1
# score -= 1
# score *= 1
# score /= 1

#f-string ----> print(f"your score is {score}") ----> automatically converts everything inside the string into a string

# age = int(input ("How old are you: "))

# remain = (90 - age)

# x = (remain*52)

# print (f"You have {x} weeks left.")

# bill = float(input("What was the total bill?"))
# tip = int(input("What percentage of tip would you like to give? 10%, 12%, or 15%?"))
# perc = tip / 100
# people = int(input("How many people are splitting the bill?"))
# split_bill = ((bill + (bill*perc))/people)
# final = "{:.2f}".format(split_bill) #------> "{:.2f}".format() leaves us the decimal points.

# #final = round(split_bill, 2) ----> does not include 0


# print (f"Each person has to pay ${final}.")

# test = 69.214151

# test = "{:.3f}".format(test)

# print(test)