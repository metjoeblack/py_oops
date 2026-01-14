
class Catcher:
    def __getattr__(self, attr_name):
        print(f'Get attribute {attr_name}')

    def __setattr__(self, attr_name, value):
        print(f'Set attribute {attr_name}')

    @staticmethod
    def main():
        x = Catcher()
        print(x.job)
        print(x.name)
        print(x.age)
        x.pay = 20_000
        print(x.pay)
        print(x.__dict__)


class AnotherCatcher:
    def __getattribute__(self, attr_name):
        print(f'Get attribute {attr_name}')

    @staticmethod
    def main():
        x = AnotherCatcher()
        print(x.job)
        print(x.name)
        print(x.age)
        x.pay = 20_000
        print(x.pay)
        print(x.__dict__)


class Wrapper:
    def __init__(self, another_obj):
        self.wrapped = another_obj

    def __getattr__(self, attr_name):
        print(f'Trace: attribute {attr_name}')
        return getattr(self.wrapped, attr_name)

    @staticmethod
    def main():
        x = Wrapper([1, 2, 3])
        x.append(4)
        print(x.wrapped)


if __name__ == '__main__':
    # Catcher.main()
    Wrapper.main()
