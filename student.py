class Student:
    school = "AkiraChix"
    def __init__(self,full_name,age,country):
        self.name = full_name
        self.age = age
        self.country =country

    def greeting(self):
        return f"Hello {self.name} from {self.country}, welcome to {self.school}."

    def full_name(self):
        return f"{self.name}"

    def year_of_birth(self):
        year = 2022 - self.age
        return f"{year}"

    def initials(self):
        empty = ""
        full_name = self.name.split()
        for letter in full_name:
         empty += letter[0]
        return empty
 