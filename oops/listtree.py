



class ListTree:
    """
    Mix-in that returns a __str__ trace of the entire class tree and all
    its objects' attributes at and above the self instance. The display is
    run by print() automatically; use str() to fetch as a string. This:

    -- Use __X pseudoprivate attribute names to avoid conflicts with clients
    -- Recurses to superclasses explicitly in DLFR (though not MRO) order
    """
    def __get_attribute_names(self, obj, indent, underscore_included=False):
        spaces = " " * (indent + 1)
        result = ""
        for attr in sorted(obj.__dict__):
            if attr.startswith("__") and attr.endswith("__"):
                if underscore_included:
                    result += f"{spaces}{attr}\n"
            else:
                result += f"{spaces}{attr}={getattr(obj, attr)!r}\n"
        return result

    def __list_class(self, a_class, indent):
        dots = "." * indent
        preamble = (
            f"\n{dots}"
            f"<Class {a_class.__name__!r}>"
            f", address {id(self):#x}"
        )

        if a_class in self.__visited:
            return preamble + ": (see above)>\n"
        elif a_class is object:
            self.__visited[a_class] = True
            return preamble + ": (see dir(object))>\n"
        else:
            self.__visited[a_class] = True
            here = self.__get_attribute_names(a_class, indent)
            above = ""
            for super_class in a_class.__bases__:
                above += self.__list_class(super_class, indent + 4)
            return preamble + f":\n{here}{above}{dots}>\n"

    def __str__(self):
        self.__visited = {}
        here = self.__get_attribute_names(self, 0)
        above = self.__list_class(self.__class__, 4)
        return (
            f"<Instance of {self.__class__.__name__!r}"
            f", address {id(self):#x}"
            f":\n{here}{above}>"
        )


