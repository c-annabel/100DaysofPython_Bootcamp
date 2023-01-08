with open("my_file.txt") as file: #no need to close again, in case forget -> read only mode
# file = open("my_file.txt")
    contents = file.read()
    print(contents)
# file.close()

# if it's not existed, it will create one.
with open("new_file.txt", mode='w') as file: #clear & rewrite
    file.write("New text.")

with open("my_file.txt", mode='a') as file: #Append
    file.write("\nNew text.")