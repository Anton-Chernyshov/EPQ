import math

class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def cross(self, other):
        return Vec3(
            self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
            self.x*other.y - self.y*other.x
        )

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalized(self):
        l = self.length()
        return self * (1/l) if l != 0 else Vec3()

    def rotate_euler(self, pitch, yaw, roll):
        """ Apply XYZ (Tait-Bryan) rotation to the vector """
        x, y, z = self.x, self.y, self.z

        # Yaw (Z-axis)
        x1 = x * math.cos(yaw) - y * math.sin(yaw)
        y1 = x * math.sin(yaw) + y * math.cos(yaw)
        z1 = z

        # Pitch (X-axis)
        x2 = x1
        y2 = y1 * math.cos(pitch) - z1 * math.sin(pitch)
        z2 = y1 * math.sin(pitch) + z1 * math.cos(pitch)

        # Roll (Y-axis)
        x3 = x2 * math.cos(roll) + z2 * math.sin(roll)
        y3 = y2
        z3 = -x2 * math.sin(roll) + z2 * math.cos(roll)

        return Vec3(x3, y3, z3)

    def to_tuple(self):
        return (self.x, self.y, self.z)

    def __repr__(self):
        return f"Vec3({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"
