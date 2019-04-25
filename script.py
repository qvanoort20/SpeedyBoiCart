from time import sleep
import directionlibrary as dl

while True:
  for x in range(0,2):
    if x == 1:
      variable = dl.forward()
    else:
      variable = dl.backward()
    variable
    dl.left()
    sleep(5)
    dl.right()
    sleep(5)
    dl.stop()
    dl.straight()
    sleep(1)
