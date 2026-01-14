

class GetAttr:
    cls_attr = 88

    def __init__(self):
        self.instance_attr = 77

    def __len__(self):
        print('__len__: 66')
        return 66

    def __getattr__(self, attr_name):
        print(f'getattr: {attr_name}')
        if attr_name == '__str__':
            return lambda *args, **kwargs: '[Getattr str]'
        else:
            return lambda *args, **kwargs: None


class GetAttribute:
    cls_attr = 88

    def __init__(self):
        self.instance_attr = 77

    def __len__(self):
        print('__len__: 66')
        return 66

    def __getattribute__(self, attr_name):
        print(f'getattribute: {attr_name}')
        if attr_name == '__str__':
            return lambda *args, **kwargs: '[Getattribute str]'
        else:
            return lambda *args, **kwargs: None


def main():
    for Cls in (GetAttr, GetAttribute):
        print(f"\n {Cls.__name__.ljust(50, '=')}")
        x = Cls()
        print(x.cls_attr)
        print(x.instance_attr)
        print(x.other)
        print(len(x))

        try:
            x[0]
        except Exception:
            print('fail []')

        try:
            x + 99
        except Exception:
            print('fail +')

        try:
            x()
        except Exception:
            print('fail ()')

        x.__getitem__(0)
        x.__add__(99)
        x.__call__()

        print(x.__str__())
        print(x)


if __name__ == '__main__':
    main()