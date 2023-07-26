# N1 - Follow convention
class Base:
    def __init__(self):
        self.__name = "tommy"

    def __skill(self):
        return "Program REST API..."


class Derived(Base):
    def __init__(self):
        super().__init__()

    def _shot(self):
        print(self.__name)
        return "Sniper level shooting..."


base = Base()
print(base.__name)  # raises AttributeError


derived = Derived()
print(derived.__name)  # raises AttributeError
print(derived._shot())  # raises AttributeError


# N2 - Break Convention -> access and modify private members from outside
class Break:
    def __init__(self):
        self.__name = "I am private attribute..."

    def __show_private(self):
        return "I am private method..."


a = Break()
print(Break.__dict__.keys())

# just access private attributes and methods
print(a._Break__show_private())
print(a._Break__name)

# access and modify private attributes
a._Break__name = "I am modified..."
print(a._Break__name)
