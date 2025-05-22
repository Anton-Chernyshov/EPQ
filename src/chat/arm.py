import math
from vec3 import Vec3

class RoboticArm:
    def __init__(self, lengths):
        """
        lengths: tuple of (base length, shoulder length, elbow length)
        """
        self.L0, self.L1, self.L2 = lengths  # Length of the base and arm segments

        # Joint angles: [Base, Shoulder, Elbow, Wrist]
        self.angles = [0, 0, 0, 0]  # Initialize all angles to 0

    def set_angles(self, base, shoulder, elbow, wrist):
        """ Set joint angles (degrees) """
        self.angles = [base, shoulder, elbow, wrist]

    def forward_kinematics(self):
        """ Compute the position of the end effector using forward kinematics """
        base_angle, shoulder_angle, elbow_angle, wrist_angle = self.angles

        # Convert angles to radians
        base_angle = math.radians(base_angle)
        shoulder_angle = math.radians(shoulder_angle)
        elbow_angle = math.radians(elbow_angle)
        wrist_angle = math.radians(wrist_angle)

        # Position of the base
        base_position = Vec3(0, 0, 0)

        # Apply base rotation (yaw around Z-axis)
        base_rot_matrix = [
            [math.cos(base_angle), -math.sin(base_angle), 0],
            [math.sin(base_angle), math.cos(base_angle), 0],
            [0, 0, 1]
        ]
        
        # Position of the shoulder joint
        shoulder_position = Vec3(self.L1 * math.cos(shoulder_angle), 0, self.L1 * math.sin(shoulder_angle))

        # Apply base rotation to shoulder joint
        shoulder_position = self.rotate_point(shoulder_position, base_rot_matrix)

        # Position of the elbow joint
        elbow_position = Vec3(self.L2 * math.cos(elbow_angle), 0, self.L2 * math.sin(elbow_angle))

        # Apply shoulder rotation to elbow joint
        elbow_position = self.rotate_point(elbow_position, base_rot_matrix)

        # Position of the end effector (wrist or tool)
        wrist_position = elbow_position + Vec3(self.L0, 0, 0)  # Extend further if needed

        return base_position, shoulder_position, elbow_position, wrist_position

    def rotate_point(self, point, matrix):
        """ Apply a rotation matrix to a 3D point """
        x = point.x * matrix[0][0] + point.y * matrix[0][1] + point.z * matrix[0][2]
        y = point.x * matrix[1][0] + point.y * matrix[1][1] + point.z * matrix[1][2]
        z = point.x * matrix[2][0] + point.y * matrix[2][1] + point.z * matrix[2][2]

        return Vec3(x, y, z)
