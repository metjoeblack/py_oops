

class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def __getattr__(self, attr_name):
        print(f'get: {attr_name!r}')
        if attr_name == 'name':
            return self._name
        else:
            raise AttributeError(attr_name)

    # def __getattribute__(self, attr_name):
    #     print(f'get: attribute {attr_name!r}')
    #     if attr_name == 'name':
    #         attr_name = '_name'
    #     return object.__getattribute__(self, attr_name)

    def __setattr__(self, attr_name, value):
        print(f'set: {attr_name!r}')
        if attr_name == 'name':
            attr_name = '_name'
        object.__setattr__(self, attr_name, value)
        # vars(self)[attr_name] = value

    def __delattr__(self, attr_name):
        print(f'del: {attr_name!r}')
        if attr_name == 'name':
            attr_name = '_name'
        # del vars(self)[attr_name]
        # del self.__dict__[attr_name]
        object.__delattr__(self, attr_name)

    @staticmethod
    def main():
        sue = Person('Sue Jones', 25)
        print(sue.__dict__)
        print(sue.name)
        sue.name = 'Susan Jones'
        print(sue.name)
        print(vars(sue))
        del sue.name
        # print(sue.name)



if __name__ == '__main__':
    Person.main()
