class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count +=1
        return cls.count


print(Counter.increment())
print(Counter.increment())
print(Counter.increment())