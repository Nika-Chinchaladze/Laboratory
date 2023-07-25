"""
# everything is object, because they have type and, they are created somehow.

# class defines the rules for object, how it can be created and what will be its
attributes and methods --> abilities.

# metaclass defines the rules for class.

# when we create common class everything is placed into metaclass that
 creates class and returns object that represents the class.

# by using metaclass, we can put some restrictions target class or modify it, based on our requirements.
like as we changed all attributes and methods from lower into upper case, we can apply some constraints -
how class should be created -> if they must have or mustn't have some attribute or method - and, only when
the class will meet the requirements, then it will be created and represented as object -> we can control
this entire process.
"""


# ================================= create classes by using -> type ================================= #
class Male:
    def __init__(self):
        self.gender = "male"

    def skill(self):
        return "Can Programming"


def my_age(self):
    self.age = 26
    return self.age


def addition(self, num1: int, num2: int):
    return num1 + num2


Person = type("Person", (Male,), {"name": "tommy", "surname": "shelby", "my_age": my_age, "addition": addition})
my_person = Person()
my_person.job = "Python Developer"

print(my_person.name)
print(my_person.job)
print(my_person.my_age())
print(my_person.addition(15, 25))
print(my_person.gender)
print(my_person.skill())


# ================================= create our custom metaclass ================================= #
class CustomMetaClass(type):
    def __new__(self, class_name, bases, attrs):
        my_attrs = {}
        for key, value in attrs.items():
            if key.startswith("__"):
                my_attrs[key] = value
            else:
                my_attrs[key.upper()] = value
        print(my_attrs)
        return type(class_name, bases, my_attrs)


class TargetClass(metaclass=CustomMetaClass):
    x = 10
    y = "name"

    def skill(self):
        return "Machine learning"


target_object = TargetClass()
print(target_object.X)
print(target_object.SKILL())

