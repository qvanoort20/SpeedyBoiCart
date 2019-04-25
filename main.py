import RoboPiLib as RPL
import setup, sys, tty, termios, signal

def interrupted(signum, frame):
  RPL.servoWrite(3,1150)
  RPL.servoWrite(0,1500)
  RPL.servoWrite(1,1500)

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
signal.signal(signal.SIGALRM, interrupted)
tty.setraw(sys.stdin.fileno())

while True:
 # print "is this even working"
  signal.setitimer(signal.ITIMER_REAL,0.255)
  ch = sys.stdin.read(1)
  signal.setitimer(signal.ITIMER_REAL,0)
  if ch == 'q':
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    break
  elif ch == 'w':
    RPL.servoWrite(1,1600)
    RPL.servoWrite(0,1400)
  elif ch == 's':
    RPL.servoWrite(1,1400)
    RPL.servoWrite(0,1600)
  elif ch == 'a':
    RPL.servoWrite(3,900)
  elif ch == 'd':
    RPL.servoWrite(3,1300)
