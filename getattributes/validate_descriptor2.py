

class Desc:
    def __set_name__(self, owner, name):
        self.name = 'remain' if name == 'remain' else f'__{name}'

    def __get__(self, instance, owner):
        match self.name:
            case '__name' | '__age':
                return getattr(instance, self.name)
            case '__acct':
                return getattr(instance, self.name)[:-3] + "***"
            case 'remain':
                return instance.retire_age - instance.age
            case _:
                raise AttributeError(self.name.lstrip("__"))

    def __set__(self, instance, value):
        if self.name == '__name':
            value = value.lower().replace(' ', '_')
        elif self.name == '__acct':
            if len(value := value.replace('-', '')) != instance.acct_len:
                raise ValueError("invalid acct number")
        elif self.name == '__age':
            if value < 0 or value > 150:
                raise ValueError('age must be between 0 and 150')
        elif self.name == 'remain':
            raise ValueError("can't set 'remain' attribute")
        setattr(instance, self.name, value)


class CardHolder:
    acct_len = 8
    retire_age = 62.5
    name = Desc()
    age = Desc()
    acct = Desc()
    remain = Desc()

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name        # This trigger property setters too!
        self.age = age
        self.addr = addr


if __name__ == '__main__':
    pass