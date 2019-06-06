#this program will calculate if a student has passed taking into account 2 applied tests and attendance in class
print("this program will calculate if a student has passed")

student  = input("insert the name of the student: ")
test1    = float(input("Now, insert the grade of the student in the first test: \n"))
test2    = float(input("Now, insert the grade of the student in the second test: \n"))
absences = int(input("Now, insert the total absences of the student: \n"))

attend = (20-absences)/20 #student's presence in the classes
average = (test1+test2)/2 #student's average accordingly to 2 applied tests

if attend <= 0.7 and average > 6.0:
    print("The student",student,"has been reproved by absences, with the total presence of:",attend,"and final grade of:",average)

if average < 6.0 and attend >= 0.7:
    print("The student",student,"has been reproved by grades, with the final grade of:",average,"and",attend,"total presence.")

if attend <= 0.7 and average < 6.0:
    print("The student",student,"has been reproved by grades and absences, with the final grade of:",average,"and",attend,"total presence.")

if average > 6.0 and attend >= 0.7:
    print("The student",student,"has passed with the final grade of:",average,"and",attend,"total presence.")
