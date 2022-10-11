#randomisation

import random
import a2my_module

#int
random_integer = random.randint(1,10)
print(random_integer)

print(a2my_module.pi)

#float (0.00 - 0.999.. not include 1.00)
random_float = random.random()
print(random_float)

# generate float between 1- more, use multiplication
more = random_float * 5 # 0.0000.. - 4.9999... 

#===================#
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇

random_number = random.randint(0,1)
if random_number == 1:
    print("Heads")
else: print("Tails")