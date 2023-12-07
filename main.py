class Student:
    count = 0
    def __init__(self, name="No Name", height=160):
        self.height = height
        self.name = name
        Student.count += 1

    def print(self):
        print(f"Я студент {self.name}.")
        print(f"Мой рост {self.height} см")


print(Student.count)
student = Student("Vitalik",170)
student.print()

student = Student(height=150)
student1 = Student(height=180)
student2 = Student(height=165)
print(student.height)
print(student1.height)
print(student2.height)
print(student2.count)