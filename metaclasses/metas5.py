

class EntriesMeta(type):

    def __new__(metacls, classname, super_classes, classdict, **kwargs):
        print(f"{kwargs = }")
        num_entries = kwargs.get("num_entries")
        print(f"{num_entries = }")
        classdict.update(
            {chr(i): i for i in range(ord('a'), ord('a') + num_entries)}
        )
        cls = super().__new__(metacls, classname, super_classes, classdict)
        return cls


class Atoz(metaclass=EntriesMeta, num_entries=26):
    pass

