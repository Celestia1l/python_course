class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
        return cls.count

    def increment_2(self):
        self.count += 1
        return self.count


count_1 = Counter()
print(Counter.increment())
print(Counter.increment())
print(count_1.increment_2())
print(Counter.increment())
print(count_1.increment_2())

# C:\Users\konok\PycharmProjects\111111\.venv\Scripts\python.exe "C:\Users\konok\python_course\class Counter.py"
# 1
# 2
# 3
# 3
# 4