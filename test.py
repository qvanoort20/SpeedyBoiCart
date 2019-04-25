import RoboPiLib as RPL
import setup, sys, tty, termios, signal
import directionlibrary as dl

def interrupted(signum, frame):
  dl.straight()
  dl.stop()

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
  elif ch == 's':
    dl.forward()
  elif ch == 'w':
    dl.backward()
  elif ch == 'a':
    dl.left()
  elif ch == 'd':
    dl.right()
