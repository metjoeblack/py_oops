

class Hack:
    def doit(self, message):
        print(f"{self.__class__.__name__}: {message}")



if __name__ == "__main__":
    instance = Hack()
    instance.doit("Hello world")
    method = instance.doit
    method("Hola")
    print(method)
    print(method.__self__.__class__.__name__)
    print(method.__func__)

    inst = Hack()
    meth = Hack.doit
    meth(inst, "Beautiful new world")
    pass

