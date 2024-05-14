class Math:
    @staticmethod
    def multiplication(*args) -> float:
        s = 1
        for i in args:
            s *= i
        return s

    @staticmethod
    def addition(*args) -> float:
        s = 0
        for i in args:
            s += i
        return s

match_1 = Math
print(match_1.addition(5,10,20))
print(match_1.multiplication(5,10,20))
