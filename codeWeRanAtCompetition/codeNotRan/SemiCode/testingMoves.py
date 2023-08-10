from time import sleep
#import compass
import movements
import setup

setup.setupDrone()
setup.setupDrone()

#movements.move('down', 3)

#sleep(60)

#movements.depthHoldGain = 0.68
movements.move('down', 4)
print("what")
movements.move('fore', 60)
print("why?")
sleep(60)





