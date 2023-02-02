# students = ("Adri", "Jan", "Aleix", "David", "Marta")

# students.sort(reverse=True)
# sorted_students = sorted(students, reverse=True)

# for i in sorted_students:
#     print(i)

students = [("Adri", "A", 15),
            ("Aleix", "D", 35),
            ("Jan", "C", 25),
            ("David", "B", 42),
            ("Marta", "F", 16)]


def name(names): return names[0]
def grade(grades): return grades[1]
def age(ages): return ages[2]


students.sort(key=name)

for i in students:
    print(i)
