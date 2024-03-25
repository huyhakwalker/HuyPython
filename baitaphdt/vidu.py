class student:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade
    def print_info(self):
        print("ID: " + self.id)
        print("Name: " + self.name)
        print("Grade: " + str(self.grade))


s1 = student("63130514", "Huy", 8)
s1.print_info()
