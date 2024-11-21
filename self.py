class student:
    name="Rishik"
    grade=12
    def intro(self):
        print("Hello I am a student")
    def detail(self):
        print(f'I am {self.name}')
        print(f'I am in grade {self.grade}')
obj =student()
obj.intro()
obj.detail()