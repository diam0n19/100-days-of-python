# def greet():
#     print ("Baboon")
#     print ("Is")
#     print ("A Animal")

# greet()

# def greet_name(name):        #-------> inside the () is called a argument
#     print (f"Baboon is {name}")
#     print ("monkey is " + name)

# greet_name("jonathan")

# def greet_names(name, location):         #-------> multiple inputs
#     print (f"Hello {name}")
#     print (f"what is it like in {location}")

# greet_names("Baboon", "Wuhan")
# import math
# def paint_calc(height, width, cover):
#     num_cans = math.ceil((height * width)/cover)
#     print(f"You need {num_cans} cans")
# test_h = int(input())
# test_w = int(input())
# coverage = 5

# paint_calc(height = test_h, width = test_w, cover = coverage)

# def prime_checker(num):
#     prime = True
#     for i in range(2, num):
#         if num % i ==0:
#             prime = False
#     if prime:
#         print (f"{num} is a prime number")
#     else:
#         print (f"{num} is not a prime number")

# n = int(input())
# prime_checker(num = n)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(plain_text, shift_amount, cipher_direction):
#     end_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         if cipher_direction == "encode":
#             new_position = position + shift_amount
#         else:
#             new_position = position - shift_amount
#         end_text += alphabet[new_position]
#     print (f"{cipher_direction}d message is \"{end_text}\"")

# encrypt(plain_text=text, shift_amount=shift, cipher_direction=direction)
