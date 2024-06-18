class IntegerOnly:
    def __new__(cls, value):
        if isinstance(value, int):
            return super().__new__(cls)
        else:
            return False

    def __init__(self, value):
        self.value = value


obj1 = IntegerOnly(10)
print(obj1.value)

obj2 = IntegerOnly(3.14)
print(obj2)
