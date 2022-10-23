#Write your code below this line 👇
def prime_checker(number):
    if   number % 2 != 0 and \
         number % 3 != 0:
        print("It's a prime number.")
    else: print("It's not a prime number.")

# #Second ways to solve this problem
#     is_prime=True
#     for i in range(2,number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("first")
#     else: print("second")
        
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
