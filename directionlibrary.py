import RoboPiLib as RPL
import setup

def left():
  RPL.servoWrite(3,900)
def right():
  RPL.servoWrite(3,1300)
def straight():
  RPL.servoWrite(3,1150)
def stop():
  RPL.servoWrite(0,0)
  RPL.servoWrite(1,0)
def forward():
  RPL.servoWrite(0,1550)
  RPL.servoWrite(1,1450)
def backward():
  RPL.servoWrite(0,1450)
  RPL.servoWrite(1,1550)
