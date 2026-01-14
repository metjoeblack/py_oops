

class CardHolder:
    acct_len = 8
    retire_age = 62.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name        # These trigger __setattr__ too!
        self.age = age
        self.addr = addr

    def __getattribute__(self, attr_name):
        super_get = object.__getattribute__
        match attr_name:
            case 'acct':
                return super_get(self, 'acct')[:-3] + '***'
            case 'remain':
                return super_get(self, 'retire_age') - super_get(self, 'age')
            case _:
                return super_get(self, attr_name)

    def __setattr__(self, attr_name, value):
        match attr_name:
            case 'name':
                value = value.lower().replace(' ', '_')
            case 'age':
                if value < 0 or value > 150:
                    raise ValueError('age must be between 0 and 150')
            case 'acct':
                if len(value := value.replace('-', '')) != self.acct_len:
                    raise ValueError("invalid acct number")
            case 'remain':
                raise ValueError("can't set remain attribute")
        object.__setattr__(self, attr_name, value)
