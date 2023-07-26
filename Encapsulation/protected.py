class Base:
    def __init__(self):
        self._name = "tommy"

    def _skill(self):
        return "Program REST API..."


class Derived(Base):
    def __init__(self):
        super().__init__()

    def _shot(self):
        self._name = "michale scold"
        return "Sniper level shooting..."


base_object = Derived()
base_object._name = "john"  # can be modified from outside
print(base_object._name)  # can be accessed from outside

derived_object = Derived()
derived_object._name = "arthur"  # can be modified from outside
print(derived_object._name)  # can be accessed from outside

derived_object._shot()  # can be modified by subclass
print(derived_object._name)  # can be accessed from outside

