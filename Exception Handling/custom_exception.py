# N1 example without built-in message:
class LowAgeError(Exception):
    pass


def func_1(age: int):
    if age < 18:
        raise LowAgeError
    return age


try:
    result_1 = func_1(age=15)
except LowAgeError:
    print("Low Age Error!!!")
else:
    print(result_1)


# N2 example with built-in message:
class WrongNameError(Exception):
    def __init__(self, name, message="Wrong Name Error!!!"):
        self.name = name
        self.message = message
        super().__init__(self.message)


def func_2(name: str):
    if name != "Nata":
        raise WrongNameError(name=name)


result_2 = func_2("Nika")
print(result_2)
