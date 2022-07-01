# Loops
fruits = ["Apple","Orange","Pear"]
for fruit in fruits:
    print(fruit)


student_heights = input("List of student heights :").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
print(sum(student_heights))
print("Average height: ",sum(student_heights)/len(student_heights))


student_scores = input("List of student scores :").split()
print(max(student_scores))
print(min(student_scores))
highest_score = 0
for student_score in student_scores:
    if student_score > highest_score:
        highest_score = student_score
print(f"The highest score is {highest_score}")


# Range
for number in range(1,11,2): # Rango de 1 a 10 con saltos de 2
    print(number)

total = 0
for number in range(1,101):
    total += number
print(total)

total = 0
for number in range(2,101,2):
    total += number
print(total)
total2 = 0
for number in range(1,101):
    if number % 2 == 0:
        total2 += number
print(total2)
# En ambos casos da el mismo resultado pero en el primero el loop es mucho mas eficiente















