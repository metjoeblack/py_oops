
from functools import singledispatch


class Shape:
    
    def __init__(self, solid):
        self.solid = solid


class Circle(Shape):
    
    def __init__(self, center, radius, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center = center
        self.radius = radius

    def draw(self):
        print("\u25cF" if self.solid else "\u25A1")


class Parallelogram(Shape):

    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc
        
    def draw(self):
        print("\u25B0" if self.solid else "\u25B1")


class Triangle(Shape):

    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc

    def draw(self):
        print("\u25B2" if self.solid else "\u25B3")


@singledispatch
def draw(shape):
    """Don't use the singledispatch decorator with instance methods"""
    raise TypeError(f"Don't know how to draw {shape!r}")


@draw.register(Circle)
def _(shape: Shape):
    print("\u25cF" if shape.solid else "\u25A1")


@draw.register(Parallelogram)
def _(shape: Shape):
    print("\u25B0" if shape.solid else "\u25B1")


@draw.register(Triangle)
def _(shape: Shape):
    print("\u25B2" if shape.solid else "\u25B3")


def main():
    shapes = [
        Circle(center=(0, 0), radius=5, solid=False),
        Parallelogram(pa=(0, 0), pb=(2, 0), pc=(1, 1), solid=False),
        Triangle(pa=(0, 0), pb=(1, 2), pc=(2, 0), solid=True),
    ]
    # for shape in shapes:
    #     shape.draw()
    for shape in shapes:
        draw(shape)


if __name__ == '__main__':
    main()
