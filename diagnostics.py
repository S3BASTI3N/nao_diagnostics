#!/usr/bin/env python
from naoqi import ALProxy
import math

ROBOT_IP = "10.42.0.20"
ROBOT_PORT = 9559

ACTUATORS = [
	"HeadPitch",
	"HeadYaw",
	"RShoulderRoll",
	"RShoulderPitch",
	"RElbowYaw",
	"RElbowRoll",
	"RWristYaw",
	"RHand",
	"LShoulderRoll",
	"LShoulderPitch",
	"LElbowYaw",
	"LElbowRoll",
	"LWristYaw",
	"LHand",
	"RHipPitch",
	"RHipRoll",
	"RKneePitch",
	"RAnklePitch",
	"RAnkleRoll",
	"LHipPitch",
	"LHipRoll",
	"LKneePitch",
	"LAnklePitch",
	"LAnkleRoll",]

TEMP_STATUS = ["OK(0)", "WARM(1)", "HOT(2)", "FIRE(3)" ]

#dcm = ALProxy("DCM", ROBOT_IP, ROBOT_PORT )
memory = ALProxy("ALMemory", ROBOT_IP, ROBOT_PORT )
motion = ALProxy("ALMotion", ROBOT_IP, ROBOT_PORT )

motion.setStiffnesses("Body", 1 )

print "Starting diagnostics of joints"

for i, actuator in enumerate(ACTUATORS):
	try:
		#print "Checking: " + actuator
		value = memory.getData("Diagnosis/Active/"+actuator+"/Error")

		if( value == 1 ):
			print "ERROR for " + actuator
			temperature = memory.getData("Device/SubDeviceList/"+actuator+"/Temperature/Sensor/Value")
			temperatureStatus = memory.getData("Device/SubDeviceList/"+actuator+"/Temperature/Sensor/Status")
			sensorPosition = memory.getData("Device/SubDeviceList/"+actuator+"/Position/Sensor/Value")
			commandPosition = memory.getData("Device/SubDeviceList/"+actuator+"/Position/Actuator/Value")
			print "   temperate status: " + TEMP_STATUS[temperatureStatus]
			print "   temperature: " + str(temperature)
			print "   position: " + str(commandPosition)
			print "   sensor position: " + str(sensorPosition)
			print "   position difference: " + str(math.fabs(commandPosition-sensorPosition))

	except Exception, e:
		print e
