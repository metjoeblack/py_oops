
import importlib, sys


def load_class():
    module_name = sys.argv[1]
    module_obj = importlib.import_module(module_name)
    print(f'[Using: {module_obj.CardHolder}]')
    return module_obj.CardHolder


def print_holder(who):
    print(who.acct, who.name, who.age, who.remain, who.addr, sep=' / ')


if __name__ == '__main__':
    CardHolder = load_class()
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    print_holder(bob)
    bob.name = 'Bob Q. Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'
    print_holder(bob)
    print(bob.__dict__)

    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    print_holder(sue)
    try:
        sue.age = 200
    except ValueError:
        print('Bad age for Sue Jones')

    try:
        sue.remain = 5
    except (AttributeError, ValueError):
        print("Can't set sue.remain")

    try:
        sue.acct = '1234567'
    except (ValueError, TypeError):
        print('Bad acct for Sue Jones')

    print_holder(bob)