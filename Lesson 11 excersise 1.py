class Student():
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def greet(self):
        string_skills = ""
        for item in self.skills:
            string_skills += '\n'+item
            
        print(f"Hello, I'm {self.name}. My favourite subjects are: {string_skills}")

# objects creation:
ivan = Student("Ivan Ivanov", ["maths", "phisics"])
alex = Student("Alex Petrov", ["arts", "music"])
maria = Student("Maria Popova", ["chemistry", "biology"])

# use objects:
ivan.greet()
alex.greet()
maria.greet()
