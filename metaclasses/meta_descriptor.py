
class PositiveDescriptor:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return vars(instance).get(self.name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(
                f"attribute {self.name!r} must be positive,"
                f" but given {value!r}"
            )
        vars(instance)[self.name] = value

    def __delete__(self, instance):
        raise AttributeError("cannot delete attribute")


class Planet:
    radius_meters = PositiveDescriptor()
    mass_kilograms = PositiveDescriptor()

    def __init__(self, name, radius_meters, mass_kilograms):
        self.name = name
        self.radius_meters = radius_meters
        self.mass_kilograms = mass_kilograms

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("name cannot be set empty.")
        self._name = value


if __name__ == '__main__':
    p = Planet('Planet A', 10, 20)
    print(vars(p))
