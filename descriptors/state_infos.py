

class DescState:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print(f'{self.__class__.__name__}: get')
        return self.value * 10

    def __set__(self, instance, value):
        print(f'{self.__class__.__name__}: set')
        self.value = value


class CalcAttrs:
    x = DescState(2)
    y = 3
    
    def __init__(self):
        self.z = 4

    @staticmethod
    def main():
        obj = CalcAttrs()
        print(obj.x, obj.y, obj.z)
        print(obj.__dict__)

        obj.x = 5
        CalcAttrs.y = 6
        obj.z = 7
        print(obj.x, obj.y, obj.z)



class InstanceState:
    def __get__(self, instance, owner):
        print(f'get attribute')
        return getattr(instance, '_x') * 10

    def __set__(self, instance, value):
        print(f'set attribute')
        instance._x = value


class CalcAttrs2:
    x = InstanceState()
    y = 3

    def __init__(self):
        self._x = 2
        self.z = 4

    @staticmethod
    def main():
        obj = CalcAttrs2()
        print(obj.x, obj.y, obj.z)
        print(obj.__dict__)

        obj.x = 5
        CalcAttrs2.y = 6
        obj.z = 7
        print(obj.x, obj.y, obj.z)
        print(obj.__dict__)





class Client:

    class DescBoth:
        def __init__(self, data):
            self.data = data

        def __get__(self, instance, owner):
            return (
                f'Desc data = {self.data!r}, '
                f'client data = {instance.data!r}'
            )

        def __set__(self, instance, value):
            instance.data = value

    managed_data = DescBoth('hack')

    def __init__(self, data):
        self.data = data

    @staticmethod
    def main():
        i = Client('code')
        print(i.managed_data)
        print(i.__dict__)
        print([x for x in dir(i) if not x.startswith('__')])

        i.managed_data = "HACK"
        print(i.managed_data)
        print(i.__dict__)
        print(getattr(i, 'data'))
        print(getattr(i, 'managed_data'))


if __name__ == '__main__':
    # CalcAttrs.main()
    # CalcAttrs2.main()
    Client.main()
    pass


