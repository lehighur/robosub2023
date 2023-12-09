#!/bin/bash
#Ensure that script is not run as root (as it would mess up the Python environment used)
if [[ `id -nu` != "lehighur" ]]; then
   echo "Not the correct user"
   exit 1
fi

#change to root directory (possibly unnecesary)
cd ~

#source ROS if using it 
source /opt/ros/foxy/setup.bash

#Run short movement program as Pixhawk has a chance of not responding to the first movement commands after boot 
python3 /home/lehighur/clMovementsTesting main halt,1

#Run the main python program that you want to run at startup
python3 /home/lehighur/clMovements2 main down,2 fore,35 turnRight,8 


