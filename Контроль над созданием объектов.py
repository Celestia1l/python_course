class ControlledCreation:
    _instance_count = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance_count < 2:
            cls._instance_count += 1
            return super().__new__(cls)
        else:
            return False

    def __init__(self, value):
        self.value = value


obj1 = ControlledCreation(10)
print(obj1.value)

obj2 = ControlledCreation(20)
print(obj2.value)

obj3 = ControlledCreation(30)
print(obj3)
