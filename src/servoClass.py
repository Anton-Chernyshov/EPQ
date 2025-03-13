"""Base classes for the arm"""

class Servo:
    def __init__(self, pin, minAngle, maxAngle):
        self.__pin = pin
        self.minAngle = minAngle
        self.maxAngle = maxAngle
        self.__angle = 0
    
    @property
    def pin(self) -> int:
        return self.__pin

    @property
    def angle(self) -> int:
        return self.__angle

    def __moveToAngle(self, angle):
        ## WRITE CODE TO MOVE SERVO TO ANGLE

        ## --
        print(f"Servo on pin {self.__pin} moved to {angle} degrees")

    @angle.setter
    def angle(self, value):
        if value < self.minAngle:
            self.__angle = self.minAngle
            self.__moveToAngle(self.minAngle)
        elif value > self.maxAngle:
            self.__angle = self.maxAngle
            self.__moveToAngle(self.maxAngle)
        else:
            self.__angle = value
            self.__moveToAngle(value)

            


class Arm:
    def __init__(self, base: Servo, shoulder: Servo, elbow: Servo, wrist: Servo, gripper: Servo):
       self.base = base
       self.shoulder = shoulder
       self.elbow = elbow
       self.wrist = wrist
       self.gripper = gripper
       self.upperArmLength = ...
       self.lowerArmLength = ...
       self.wristLength = ...
       
    def moveJoint(self, joint, angle):
        self.joint.angle = angle

    def moveArm(self, x, y, z):
        ## WRITE CODE TO MOVE ARM TO POSITION (x, y, z)



        ## --
        print(f"Arm moved to position ({x}, {y}, {z})")

if __name__ == "__main__":
    ...