gain = 1
depthHoldGain = .675

vectors = {
   'fore' : [int(0+1000*gain),0,int(500-500*depthHoldGain),0,0],
   'back' : [int(0-1000*gain),0,int(500-500*depthHoldGain),0,0],
    'right' : [0,int(0+1000*gain),int(500-500*depthHoldGain),0,0],
    'left' : [0,int(0-1000*gain),int(500-500*depthHoldGain),0,0],
    'up' : [0,0,int(500+500*gain),0,0],
    'down' : [0,0,int(500-500*gain),0,0],
    'turnRight' : [0,0,int(500-500*depthHoldGain),int(0+1000*gain),0],
    'turnLeft' : [0,0,int(500-500*depthHoldGain),int(0-1000*gain),0],
    'halt' :[0,0,int(500-500*depthHoldGain),0,0]
    }



def move(direction,duration=0):
    print(f'Moving {direction}wards for {duration} seconds.')
    file.write(f'Moving {direction}wards for {duration} seconds.\n')
    i = 0
    while i <= duration :
        drone.mav.manual_control_send(drone.target_system,*vectors[direction])
        if duration-i<1:
            sleep(duration)
        else:
            sleep(1)
        i+=1
    if duration != 0:
        file.write(f'Done moving {direction}wards\n')
        print(f'Done moving {direction}wards')
