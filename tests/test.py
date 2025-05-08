from ..src.servoClass import Servo

def testServos():
    testServo1 = Servo(1, 0, 180)
    testServo1.angle = 90
    assert testServo1.angle == 90
    testServo1.angle = 200
    assert testServo1.angle == 180
    testServo1.angle = -10
    assert testServo1.angle == 0
    testServo2 = Servo(2, 45, 135)
    testServo2.angle = 90
    assert testServo2.angle == 90
    testServo2.angle = 200
    assert testServo2.angle == 135
    testServo2.angle = -10
    assert testServo2.angle == 45
    print("All tests passed")


