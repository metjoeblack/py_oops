
import shelve
from person import Person, Manager


SHELVE_FILE = "persons_db.shelve"


def store_to_shelve():
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", paycheck=100_000)
    pat = Manager("Pat Jones", paycheck=50_000)
    with shelve.open(SHELVE_FILE) as shelf_db:
        for person in (bob, sue, pat):
            shelf_db[person.name] = person


def read_from_shelve():
    with shelve.open(SHELVE_FILE) as shelf_db:
        print(len(shelf_db))
        print(list(shelf_db.keys()))
        pat = shelf_db["Pat Jones"]
        print(pat.get_last_name())

        for key in shelf_db:
            print(f"{key} ==> {shelf_db[key]!r}")


if __name__ == "__main__":
    # store_to_shelve()
    read_from_shelve()
    pass
