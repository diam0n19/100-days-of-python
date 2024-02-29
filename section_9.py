# name_book = {"name_one":"Baboon",                      #--------> dictionary is {key:value}
#              "name_two":"lulu",
#              "name_three":"baldilocks"}

# # print (name_book["name_three"])                #-------> retrieving from dictionary
# name_book["name_four"] = "shuhmee"               #------> adding into a list
# print (name_book)

# empty_dictionary = {}      #-----------> creating a empty dictionary

# name_book = {}             #this is wiping a dictionary

# name_book["name_one"] = "tricia"       #------> this is editing a existing value in a dictionary

# for name in name_book:
#     print (name)                 #------> this only prints the key
#     print (name_book[name])      #------> this prints the value

# student_scores = {"Harry":81,
#                   "Ron":78,
#                   "Hermione":99,
#                   "Draco":74,
#                   "Neville":62}

# student_grades = {}
# for student in student_scores:
#     score = student_scores[student]
#     if score>90:
#         student_grades[student] = "Outstanding"
#     elif score >80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# print (student_grades)

# capitals = {"China":"BeiJing",         #-------> nesting in a dictionary
#             "USA":"Washington"}

# travel_love = {"names":["baboon","ape","alem","lulu"]}        #------> nesting a list inside a dictionary

# nesting_list = ["A","B",["C","D"]]

# nesting_dict = {"France":{"cities":["Paris","Lillie","Dijon"]},
#                 "Germany": ["Berlin","Hamburg","Stuttgart"]}

def bid():
    bidding_dict = {}
    contin = True
    while contin:
        name = input("What is your name: ")
        bidding = int(input("Your bidding price: "))
        bidding_dict[name] = bidding
        yesno = input("Anyone else wants to bid? Type \"yes\" or \"no\" : ").lower()
        if yesno == "no":
            contin = False
    high = 0
    for name in bidding_dict:
        if bidding_dict[name] > high:
            high = bidding_dict[name]    
    for key in bidding_dict:
        if bidding_dict[key] == high:
            print (f"{key} has the highest bid of {bidding_dict[key]}")

bid()


