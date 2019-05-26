#this program will calculate if a student has passed 
print("this program will calculate if a student has passed")

student  = input("insert the name of the student: ")
test1    = float(input("Now, insert the grade of the student in the first test: \n"))
test2    = float(input("Now, insert the grade of the student in the second test: \n"))
absences = int(input("Now, insert the total absences of the student: \n"))

totalAb = (20-absences)/20
average = (test1+test2)/2

if totalAb >= 0.7 and average > 6.0:
    print("The student",student,"has been reproved by absences, with the total absences of:",totalAb,"and final grade of:",average)

if average < 6.0 and totalAb < 0.7:
    print("The student",student,"has been reproved by grades, with the final grade of:",average,"and",totalAb,"absences")

if totalAb > 0.7 and average < 6.0:
    print("The student",student,"has been reproved by grades and absences, with the final grade of:",average,"and",totalAb)

if average > 6.0 and totalAb < 0.7:
    print("The student",student,"has passed with the final grade of:",average,"and",totalAb,"total absences")