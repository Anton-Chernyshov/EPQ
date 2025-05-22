"""Base classes for the arm"""
import gpiozero
import math

class Servo:
    def __init__(self, pin, minAngle, maxAngle):
        self.__pin = pin
        self.__minAngle = minAngle
        self.__maxAngle = maxAngle
        self.__angle = 0
        self.__servo = gpiozero.AngularServo(self.__pin, self.__minAngle, self.__maxAngle)
    
    @property
    def pin(self) -> int:
        return self.__pin
    
    @property
    def angle(self) -> int:
        return self.__angle

    def __moveToAngle(self, angle):
        self.__servo.angle = angle
        print(f"Servo on pin {self.__pin} moved to {angle} degrees")

    @angle.setter
    def angle(self, value: int):
        """Move to angle value and clamp between minAngle and maxAngle"""
        if value < self.__minAngle:
            self.__angle = self.__minAngle
            self.__moveToAngle(self.__minAngle)
        elif value > self.__maxAngle:
            self.__angle = self.__maxAngle
            self.__moveToAngle(self.__maxAngle)
        else:
            self.__angle = value
            self.__moveToAngle(value)

            


class Arm:
    def __init__(self, base: Servo, shoulder: Servo, elbow: Servo, wrist: Servo, gripper: Servo, upperArmLength: int, lowerArmLength: int, wristLength: int):
       self.base = base
       self.shoulder = shoulder
       self.elbow = elbow
       self.wrist = wrist
       self.gripper = gripper
       self.upperArmLength = upperArmLength
       self.lowerArmLength = lowerArmLength
       self.wristLength = wristLength
       
    def moveJoint(self, joint, angle):
        joint.angle = angle

    def moveArm(self, x, y, z):
        baseAngle = math.degrees(math.atan2(y, x))
        r = math.sqrt(x**2 + y**2)
        d = math.sqrt(r**2 + z**2)
        L1 = self.upperArmLength
        L2 = self.lowerArmLength
        if d > (L1 + L2):
            print("Target out of reach.")
            return

        try:
            elbowAngleRad = math.acos((L1**2 + L2**2 - d**2) / (2 * L1 * L2))
            elbowAngle = math.degrees(elbowAngleRad)

            alpha = math.atan2(z, r)
            beta = math.acos((d**2 + L1**2 - L2**2) / (2 * d * L1))
            shoulderAngle = math.degrees(alpha + beta)

 
            wristAngle = - (shoulderAngle - elbowAngle)
        except ValueError:
            print(f"Domain error, unreachable?? {(elbowAngle, alpha, beta, shoulderAngle, elbowAngle, wristAngle)}")
            return

        self.base.angle = baseAngle
        self.shoulder.angle = shoulderAngle
        self.elbow.angle = elbowAngle
        self.wrist.angle = wristAngle
        print(f"Arm moved to position ({x}, {y}, {z})")

if __name__ == "__main__":
    print("This must be run as a module, not as main")
