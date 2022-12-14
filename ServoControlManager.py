from InterpolationMethod import calcPosServo
from SyncWriteServos import SyncWriteServos

ServosID = [1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
ServosSpeed = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 600, 600, 2000, 2000, 1200, 1200]

HeadID = [1, 2]
HeadSpeed = [2000, 2000]
ArmID = [11, 9, 7, 5, 12, 10, 8, 6]
ArmSpeed = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000]
PressID = [14, 15]
#PressID = [12, 13] #for test
PressSpeed = [2000, 2000]
BodyID = [13, 0]
BodySpeed = [2000, 0]
LegID = [17, 19, 21, 16, 18, 20]
LegSpeed = [600, 2000, 1200, 600, 2000, 1200]

GoalPosHeadPer = 0.5
GoalPosNeckPer = 0

ArmShoulderAnglRightPer = 0
ArmForearmAnglRightPer = 0
ArmElbowTopAnglRightPer = 0
ArmElbowBottAnglRightPer = 0
ArmElbowAnglRightPer = 0

ArmShoulderAnglLeftPer = 0
ArmForearmAnglLeftPer = 0
ArmElbowTopAnglLeftPer = 0
ArmElbowBottAnglLeftPer = 0
ArmElbowAnglLeftPer = 0
SwitchBothElbow = True

PressTopAnglPer = 0.5
PressBottAnglPer = 0.5

BodyRotPer = 0.5

HightBothLegPer = 0
HightLeftLegPer = 0
HightRightLegPer = 0
SwitchBothLeg = True

def CalcHeadPos():
    ReadPosArray = calcPosServo()
    HeadPos = ReadPosArray.CalcHead(GoalPosHeadPer, GoalPosNeckPer)
    return HeadPos

def CalcArmPos():
    ReadPosArray = calcPosServo()
    ArmPos = ReadPosArray.CalcArms(ArmShoulderAnglRightPer, ArmForearmAnglRightPer, ArmElbowTopAnglRightPer, ArmElbowBottAnglRightPer, ArmElbowAnglRightPer,
                 ArmShoulderAnglLeftPer, ArmForearmAnglLeftPer, ArmElbowTopAnglLeftPer, ArmElbowBottAnglLeftPer, ArmElbowAnglLeftPer, SwitchBothElbow)
    return ArmPos

def CalcPressPos():
    ReadPosArray = calcPosServo()
    PressPos = ReadPosArray.CalcPress(PressTopAnglPer, PressBottAnglPer)
    return PressPos

def CalcBodyPos():
    ReadPosArray = calcPosServo()
    BodyPos = ReadPosArray.CalcBody(BodyRotPer)
    return BodyPos

def CalcLegPos():
    ReadPosArray = calcPosServo()
    LegPos = ReadPosArray.CalcLeg(HightBothLegPer, HightLeftLegPer, HightRightLegPer, SwitchBothLeg)
    return LegPos

#Function run example
WritePos = SyncWriteServos()
GoalPos = CalcHeadPos()
ServosID = HeadID
ServosSpeed = HeadSpeed
WritePos = WritePos.SyncWriteData(ServosID, ServosSpeed, GoalPos)
print(WritePos)

WritePos = SyncWriteServos()
GoalPos = CalcPressPos()
ServosID = PressID
ServosSpeed = PressSpeed
WritePos = WritePos.SyncWriteData(ServosID, ServosSpeed, GoalPos)
print(WritePos)