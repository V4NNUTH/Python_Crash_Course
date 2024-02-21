class Dog:

    def __init__(self, name, age):
        """Initialize name and age attribute"""
        self.name= name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog('kiki',6)
your_dog = Dog('lulu',9)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} year old.")
my_dog.sit()
my_dog.roll_over()
print("\n")
print(f"My dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} year old.")
your_dog.sit()
your_dog.roll_over()