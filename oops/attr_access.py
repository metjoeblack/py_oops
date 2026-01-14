

class Empty:
    def __getattr__(self, attr_name):
        if attr_name == 'age':
            return 27
        else:
            raise AttributeError(f"attribute {attr_name!r} is undefined")


class AccessControl:
    def __setattr__(self, attr_name, value):
        if attr_name == 'age':
            object.__setattr__(self, attr_name, value)
            # Also: self.__dict__[attr_name] = value
        else:
            raise AttributeError(f"{attr_name!r} isn't allowed")


if __name__ == '__main__':
    x = Empty()
    print(x.age)
    x.age = 20
    print(x.age)
    print(x.name)





