

class ListInherited:
    """
    Use dir() to collect both instance attributes and names inherited
    from its classes. This includes default names inherited from the
    implied 'object' superclass above topmost classes. getattr() can
    fetch inherited names not in self.__dict__.
    """
    def __get_attribute_names(self, underscore_included=False):
        result = ""
        for attr in dir(self):
            if attr.startswith("__") and attr.endswith("__"):
                result += f"\t{attr}\n" if underscore_included else ""
            else:
                result += f"\t{attr}={getattr(self, attr)!r}\n"
        return result

    def __str__(self):
        return (
            f"<Instance of {self.__class__.__name__!r}, "
            f"address {id(self):#x}:\n"
            f"{self.__get_attribute_names()}>"
        )