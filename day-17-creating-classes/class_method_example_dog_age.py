#class_method_example_dog_age
class Dog:
    def __init__(self, name):
        self.name = name
        self.age = 0

    def birthday(self):
        self.age += 1

dog1 = Dog("Bruno")
print(dog1.age)   # Should print 0

dog1.birthday()
print(dog1.age)   # Should print 1

dog1.birthday()
print(dog1.age)   # Should print 2
