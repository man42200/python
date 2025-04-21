students = []
num_students = int(input("Enter the number of students: "))
for _ in range(num_students):
	student = tuple(input("Enter roll no, age, name: ").split())
	students.append(student)

roll_nos = [student[0] for student in students]
names = [student[2] for student in students]
ages = [student[1] for student in students]

print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)