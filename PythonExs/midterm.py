# This program creates a gradebook for students 
# There are students, marks, grades, computations, averages, and weighted averages

# Part 1: create 3 dictionaries.
# Part 2: add names, marks.

from functools import total_ordering


jamal = {
    "name" : "Jamal",
    "homework" : [90.0, 97.0, 75.0, 92.0],
    "quizzes" : [88.0, 40.0, 94.0],
    "tests" : [75.0, 90.0]
}

leo = {
    "name": "Leo",
    "homework" : [100.0, 92.0, 98.0, 100.0],
    "quizzes" : [82.0, 83.0, 91.0],
    "tests" : [89.0, 97.0]
}

aaliyah = {
    "name" : "Aaliyah",
    "homework" : [0.0, 87.0, 75.0, 22.0],
    "quizzes" : [0.0, 75.0, 78.0],
    "tests" : [100.0, 100.0]
}

# Part 3: make a list
students = [jamal, leo, aaliyah]

cases = ["homework", "quizzes", "tests"]

w_calc = [0.10, 0.30, 0.60]

all_average = 0.0

# Part 4: Print out the grades

print ("\nStudents' Grades\n".upper())

for student in students:
    print (student["name"].upper())
    print ("Homework")
    print (student["homework"])
    print ("Quizzes")
    print (student["quizzes"])
    print ("Tests")
    print (student["tests"], "\n")

# Part 5: Compute the averages.


def average(numbers):
    total = sum(numbers)
    temp = float(total) / len(numbers)
    return temp


print ("Students\' Averages\n".upper())


for c in cases:
    cc = c.upper()
    print (cc)
    for student in students:
        numbers = student[c]
        calc = round(average(numbers),1)
        print (student["name"])
        print (calc)
    print ("")

# Part 6: Compute weighted averages.


def w_average(marks):

    w_calc = [0.10, 0.30, 0.60]
    s_calc = 0
    w = 0
    while w < len(w_calc):
        s_calc += w_calc[w] * marks[w]
        w += 1
    return s_calc

def get_letter_grade(score):

    if score >= 90:
        return "A\n"
    elif score >= 80:
        return "B\n"
    elif score >= 70:
        return "C\n"
    elif score >= 60:
        return "D\n"
    else:
        return "F\n"

def get_class_average(ind):
    class_total = round(ind / len(students), 1)
    return class_total

print ("Students\' Weighted average".upper()) 

print ("Formative Learning [Homeworks, Quizzes, Tests]: ["+str(float(w_calc[0])*100)+", "+str(float(w_calc[1])*100)+", "+str(float(w_calc[2])*100)+"]\n")

print 
for student in students:
    print (student["name"].upper() + "\'s marks are:".upper())
    l_calc = []
    for c in cases:    
        numbers = student[c]
        calc = round(average(numbers),1)
        l_calc.append(calc)
    print (l_calc)
    print("For a weighted average of")
    ind_average = round(w_average(l_calc),1)
    print (ind_average)
    print("Standing for a:")
    print (get_letter_grade(ind_average))
    all_average += ind_average

print("Finally, The class average is:".upper())

print(get_class_average(all_average))