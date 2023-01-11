#Keyword list/tuple/range/string

numbers = [1,2,3]
#Method 1
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

#Method 2: keyword list method
new_list = [n+1 for n in numbers]

print(new_list)

#Practice 01:
name = "Angela"
new_list = [letter for letter in name]
print(new_list)

#Practice 02:
range_list = [num * 2 for num in range(1,5)]
print(range_list)

range_list1 = [num * 2 for num in range(1,5) if num != 2]
print(range_list1)

names = ["Alex", "Beth", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]

#practice 03:
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.

with open("file1.txt") as data1_file:
    data1 = data1_file.readlines()
    list1 = []
    # for row in data1:
    #     stripped_row = row.strip("\n")
    #     list1.append(stripped_row)

with open("file2.txt") as data2_file:
    data2 = data2_file.readlines()
    list2 = []
    # for row in data2:
    #     stripped_row = row.strip("\n")
    #     list2.append(stripped_row)

# result = [int(num) for num in list1 if num in list2]
result = [int(num) for num in data1 if num in data2]

print(result)