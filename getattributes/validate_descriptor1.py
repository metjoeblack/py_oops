

class NameDesc:
    def __get__(self, instance, owner):
        return self.name

    def __set__(self, instance, value):
        self.name = value.lower().replace(' ', '_')


class AgeDesc:
    def __get__(self, instance, owner):
        return self.age

    def __set__(self, instance, value):
        if value < 0 or value > 150:
            raise ValueError('age must be between 0 and 150')
        self.age = value


class AcctDesc:
    def __get__(self, instance, owner):
        return self.acct[:-3] + '***'

    def __set__(self, instance, value):
        if len(value := value.replace('-', '')) != instance.acct_len:
            raise ValueError("invalid acct number")
        self.acct = value


class RemainDesc:
    def __get__(self, instance, owner):
        return instance.retire_age - instance.age

    def __set__(self, instance, value):
        raise ValueError("can't set remain")


class CardHolder:
    acct_len = 8
    retire_age = 62.5
    name = NameDesc()
    age = AgeDesc()
    acct = AcctDesc()
    remain = RemainDesc()

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name        # This trigger property setters too!
        self.age = age
        self.addr = addr
