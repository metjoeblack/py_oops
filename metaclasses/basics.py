

def extra(self, args):
    pass


class Extras(type):
    def __init__(cls, cla_name, super_cls, attribute_dict):
        if required():
            cls.extra = extra

class Client1(metaclass=Extras):
    pass


class Client2(metaclass=Extras):
    pass








