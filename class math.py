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

    @staticmethod
    def division(*args) -> float:
        s = args[0]
        for i in args:
            s /= i
        return s * args[0]

    print(division(100, 50, 2))

    @staticmethod
    def subtraction(*args) -> float:
        s = args[0]
        for i in args:
            s -= i
        return s + args[0]

    print(subtraction(100, 50, 25, 5))

    @staticmethod
    def factorial(s) -> float:
        q = 1
        for i in range(1, s):
            s *= i
        return s

    print(factorial(5))

