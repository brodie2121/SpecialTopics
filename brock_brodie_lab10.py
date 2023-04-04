
class SimpleCounter:
    def __init__(self, firstnum):
        self.__count = firstnum

    def increment(self):
        self.__count += 1

    def clear(self):
        self.__count = 0

    def get_value(self):
        return self.__count

    def decrement(self):
        pass


class AdvancedCounter(SimpleCounter):
    def __init__(self, num):
        SimpleCounter.__init__(self, num)

    def increment(self):
        SimpleCounter.increment(self)
        SimpleCounter.increment(self)

    def decrement(self):
        num = SimpleCounter.get_value(self) - 1
        SimpleCounter.__init__(self, num)


def main():
    num1 = SimpleCounter(10)
    num2 = AdvancedCounter(10)

    num1.increment()
    num2.increment()
    print("After incrementing SimpleCounter object value :", num1.get_value())
    print("After incrementing AdvancedCounter object value :", num2.get_value())

    num1.decrement()
    num2.decrement()
    print("\nAfter decrementing SimpleCounter object value :", num1.get_value())
    print("After decrementing AdvancedCounter object value :", num2.get_value())

    num1.clear()
    num2.clear()
    print("\nAfter clearing SimpleCounter object value :", num1.get_value())
    print("After clearing AdvancedCounter object value :", num2.get_value())


main()
