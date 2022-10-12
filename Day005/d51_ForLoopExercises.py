#-----5.1 Average Height------------#
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
stud_heights_total = 0
for m in student_heights:
  stud_heights_total += m

ave_stud_height = round(stud_heights_total / len(student_heights))
print(ave_stud_height)

#-----5.2 Highest Score------------#
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0
for h in student_scores:
    if h > highest_score:
        highest_score = h
    
print(f"The highest score in the class is: {highest_score}")


#adding 2+4+6+8...+98+100
total = 0
for i in range (2,101, 2):
  total += i

print(total)

#-----5.4 FizzBuzz------------#
#Write your code below this row 👇
msg1 = "Fizz"
msg2 = "Buzz"
msg3 = msg1 + msg2 

for i in range(1,101):
    if i % 3 == 0 and i%5 == 0:
        print(msg3)
    elif i % 3 == 0:
        print(msg1)
    elif i % 5 == 0:
        print(msg2)
    else:
        print(i)