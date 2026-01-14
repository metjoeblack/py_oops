

class AttrSquare:
    def __init__(self, value):
        self.value = value

    # def __getattr__(self, attr_name):
    #     if attr_name == 'x':
    #         return self.value ** 2
    #     else:
    #         raise AttributeError(attr_name)

    def __getattribute__(self, attr_name):
        # print(f"get attr: {attr_name}")
        if attr_name == 'x':
            return self.value ** 2
        else:
            return super().__getattribute__(attr_name)
        # return object.__getattribute__(self, 'value') ** 2

    def __setattr__(self, attr_name, value):
        if attr_name == 'x':
            attr_name = 'value'
        object.__setattr__(self, attr_name, value)

    @staticmethod
    def main():
        a = AttrSquare(5)
        # print(a.__dict__)
        # print(a.value)
        print(a.x)
        # a.x = 10
        # print(a.__dict__)
        # print(a.x)
        # print(a.value)


class GetAttr:
    attr1 = "class attribute"

    def __init__(self):
        self.attr2 = 'instance attribute'

    def __getattr__(self, attr_name):
        print(f'get: {attr_name}')
        if attr_name == 'attr3':
            return 'virtual managed attribute'
        else:
            raise AttributeError(attr_name)

    @staticmethod
    def main():
        x = GetAttr()
        print(x.attr1)
        print(x.attr2)
        print(x.attr3)


class GetAttribute:
    attr1 = "class attribute"

    def __init__(self):
        self.attr2 = 'instance attribute'

    def __getattribute__(self, attr_name):
        print(f'get: {attr_name}')
        if attr_name == 'attr3':
            return 'virtual managed attribute'
        else:
            return object.__getattribute__(self, attr_name)

    @staticmethod
    def main():
        x = GetAttribute()
        print(x.attr1)
        print(x.attr2)
        print(x.attr3)


if __name__ == '__main__':
    # AttrSquare.main()
    # GetAttr.main()
    GetAttribute.main()
