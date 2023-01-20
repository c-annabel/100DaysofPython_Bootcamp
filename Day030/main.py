# #FileNotFound
# with open("a_file.txt") as file:
#     file.read()
#
# #KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]
#
# #Index Error
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]
#
# #TypeError
# text = "abc"
# print(text + 5)
#-----------------------------------------------------#
# try:    Something that might cause an exception
# except: Do this if there was an exception
# else:   Do this if there were no exceptions
# finally:Do this no matter what happens
#-----------------------------------------------------#
#
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sdfefa"]) #it will fail and go to except if not specified.
#
# except FileNotFoundError:
#     #print("There was an error")
#     file = open("a_file.txt", "w") #if not existed, it creates.
#     file.write("Something")
#
# # except KeyError:
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
#
# else: #if all tries suceeded.
#     content = file.read()
#     print(content)
#
# finally:
#     # file.close()
#     # print("File was closed.")
#     raise KeyError #self-raised error
#     raise TypeError("message locates") #raise error and message

height = float(input("Height: "))
weight = int(input("Weight:"))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

