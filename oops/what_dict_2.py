
import logging


logging.basicConfig(level=logging.INFO, format='%(message)s')


class Record:
    def __init__(self, **fields):
        logging.info(f"[INIT] Creating record with fields: {fields}]")
        self.__dict__.update(fields)

    def __getattribute__(self, attr_name):
        if attr_name == "__dict__":
            return object.__getattribute__(self, "__dict__")
        value = super().__getattribute__(attr_name)
        logging.info(f"[GET] Accessing '{attr_name}' - {value}")
        return value

    def __setattr__(self, attr_name, value):
        if attr_name in self.__dict__:
            logging.info(f"[UPDATE] Modifying '{attr_name}' - {value}")
        else:
            logging.info(f"[SET] Creating '{attr_name}' - {value}")
        # self.__dict__[attr_name] = value
        super().__setattr__(attr_name, value)

    def __delattr__(self, attr_name):
        if attr_name in self.__dict__:
            logging.info(f"[DEL] Deleting '{attr_name}'")
            del self.__dict__[attr_name]
        else:
            logging.warning(
                f"[DEL] Attempted to delete non-existing field '{attr_name}'"
            )

    @staticmethod
    def main():
        jane = Record(first_name="Jane", last_name="Doe", age=25)
        print(jane)
        print(jane.first_name)
        print(jane.age)
        jane.age = 26

        jane.job = "Software Engineer"
        print(jane.__dict__)

        del jane.last_name
        print(jane.__dict__)


if __name__ == '__main__':
    Record.main()

