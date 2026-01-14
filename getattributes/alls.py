

class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def get_square(self):
        return self._square ** 2

    def set_square(self, value):
        self._square = value

    def get_cube(self):
        return self._cube ** 3

    def set_cube(self, value):
        self._cube = value

    square = property(get_square, set_square)
    cube = property(get_cube, set_cube)

    @staticmethod
    def main():
        powers = Powers(2, 3)
        print(powers.square)
        print(powers.cube)
        powers.square = 10
        print(powers.__dict__)


class ExponentDescriptor:
    def __init__(self, exponent):
        self.exponent = exponent

    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return vars(instance)[self.name] ** self.exponent

    def __set__(self, instance, value):
        vars(instance)[self.name] = value


class PowersWithDesc:
    square = ExponentDescriptor(2)
    cube = ExponentDescriptor(3)

    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    @staticmethod
    def main():
        powers = PowersWithDesc(5, 9)
        print(powers.square)
        print(powers.cube)


class PowersGetAttr:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattr__(self, attr_name):
        if attr_name == 'square':
            return self._square ** 2
        elif attr_name == 'cube':
            return self._cube ** 3
        else:
            raise TypeError(f'unknown attribute {attr_name!r}')

    def __setattr__(self, attr_name, value):
        if attr_name in ('square', 'cube'):
            vars(self)[f'_{attr_name}'] = value
        else:
            vars(self)[attr_name] = value

    @staticmethod
    def main():
        powers = PowersGetAttr(2, 5)
        print(powers.square)
        print(powers.cube)
        powers.square = 10
        print(vars(powers))
        powers.cube = 11
        print(vars(powers))


class PowersGetAttribute:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattribute__(self, attr_name):
        """
        if attr_name == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif attr_name == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, attr_name)
        """
        if attr_name == 'square':
            return self._square ** 2
        elif attr_name == 'cube':
            return self._cube ** 3
        else:
            return object.__getattribute__(self, attr_name)

    def __setattr__(self, attr_name, value):
        if attr_name in ('square', 'cube'):
            object.__setattr__(self, f'_{attr_name}', value)
            # vars(self)[f'_{attr_name}'] = value
        else:
            object.__setattr__(self, attr_name, value)

    @staticmethod
    def main():
        powers = PowersGetAttribute(2, 5)
        print(powers.square)
        print(powers.cube)
        powers.square = 10
        print(vars(powers))
        powers.cube = 11
        print(vars(powers))


if __name__ == '__main__':
    # Powers.main()
    # PowersWithDesc.main()
    # PowersGetAttr.main()
    PowersGetAttribute.main()
    pass