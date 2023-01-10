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

#Practice:
name = "Angela"
new_list = [letter for letter in name]
print(new_list)