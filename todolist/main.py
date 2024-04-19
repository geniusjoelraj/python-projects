class Dog():
    def __init__(self, name, age=1):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name, "barked")

    def get_age(self):
        print(self.age)

tim = Dog("Tim")
bob = Dog("Bob", 100)
bob.get_age()
