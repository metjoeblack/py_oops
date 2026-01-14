"""
classtree.py: Climb inheritance trees using namespace links,
displaying higher superclasses with indentation for height.
"""

def class_tree(cls, indent):
    print(f"{'.' * indent}{cls.__name__}")
    for superclass in cls.__bases__:
        class_tree(superclass, indent + 3)


def instance_tree(instance):
    print(f"Tree of {instance.__class__.__name__}")
    class_tree(instance.__class__, 3)


if __name__ == "__main__":
    def self_test():
        """
                A
        B               C
                D                  (E)
                        F
        """
        class A: pass
        class B(A): pass
        class C(A): pass
        class D(B, C): pass
        class E: pass
        class F(D, E): pass

        instance_tree(B())
        instance_tree(F())

    self_test()