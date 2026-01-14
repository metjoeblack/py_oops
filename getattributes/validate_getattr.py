

class CardHolder:
    acct_len = 8
    retire_age = 62.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name        # This trigger property setters too!
        self.age = age
        self.addr = addr

    def __getattr__(self, attr_name):
        match attr_name:
            case 'acct':
                return self._acct[:-3] + '***'
            case 'remain':
                return CardHolder.retire_age - self.age
            case _:
                raise AttributeError(attr_name)

    def __setattr__(self, attr_name, value):
        match attr_name:
            case 'name':
                value = value.lower().replace(' ', '_')
            case 'age':
                if value < 0 or value > 150:
                    raise ValueError('age must be between 0 and 150')
            case 'acct':
                attr_name = '_acct'
                if len(value := value.replace('-', '')) != self.acct_len:
                    raise ValueError("invalid acct number")
            case 'remain':
                raise ValueError("can't set remain attribute")
        vars(self)[attr_name] = value








