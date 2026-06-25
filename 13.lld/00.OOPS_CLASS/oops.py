class Student:
    # Constructor
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def study(self):
        print("Studying....")


s1 = Student(name="Alice", age=28)
s2 = Student(name="Bob", age=29)

print(s1.name, s2.name)


s1.study()
