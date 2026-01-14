
def mro_diamond():
    class D:            #    object
        attr = "D"      #      |
    class C(D):         #      D
        attr = "C"      #    /    \
    class B(D):         #   B      C
        pass            #    \    /
    class A(B, C):      #      A
        pass            #      |
                        #      i
    i = A()
    print(i.attr)
    print([cls.__name__ for cls in A.__mro__])
    # A, B, C, D, object


def mro_nondiamond():
    class E:
        attr = "E"         #     object
    class F:               #    /     \
        attr = "F"         #   F       E
    class C(E):            #   |       |
        attr = "C"         #   B       C
    class B(F):            #    \     /
        pass               #       A
    class A(B, C):         #       |
        pass               #       i

    i = A()
    print(i.attr)
    print([cls.__name__ for cls in A.__mro__])
    # A, B, F, C, E, object
    print([cls.__name__ for cls in A.__bases__])


if __name__ == "__main__":
    mro_diamond()
    mro_nondiamond()
    pass

