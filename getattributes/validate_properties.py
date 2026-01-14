

class CardHolder:
    acct_len = 8
    retire_age = 62.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name        # This trigger property setters too!
        self.age = age
        self.addr = addr

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0 or value > 150:
            raise ValueError('age must be between 0 and 150')
        else:
            self.__age = value

    @property
    def acct(self):
        return self.__acct[:-3] + '***'

    @acct.setter
    def acct(self, value):
        if len(value := value.replace('-', '')) != self.acct_len:
            raise ValueError('invalid acct number')
        self.__acct = value

    @property
    def remain(self):
        return self.retire_age - self.age


if __name__ == '__main__':
    pass