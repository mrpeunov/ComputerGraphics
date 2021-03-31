class Point:
    x: float
    y: float
    z: float

    def __init__(self):
        pass

    def __mul__(self, other):
        self.x *= other
        self.y *= other
        self.z *= other

        return self

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

        return self
