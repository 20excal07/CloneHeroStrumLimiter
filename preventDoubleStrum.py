import time

if starting:
	strumHoldPeriod = 0.033333		#seconds (default: 1/30th of a second)
	vJoyId = 0
	vJoy_joyId = "vJoy Device"
	joyId = 1
	
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = 1000 / 120
	timepress = 0

clock = time.clock()

if keyboard.getPressed(Key.Space) is True:
	vJoy[vJoyId].setPressed(0)

for i in range(13):
	if joystick[joyId].getDown(i) is True:
		if not joystick[vJoy_joyId].getDown(i): vJoy[vJoyId].setButton(i, True)
	else:
		if joystick[vJoy_joyId].getDown(i): vJoy[vJoyId].setButton(i, False)

if joystick[joyId].pov[0] != -1:
	timepress = clock
	if joystick[vJoy_joyId].pov != joystick[joyId].pov:
		vJoy[vJoyId].setAnalogPov(0, joystick[joyId].pov[0])

if (timepress > 0 and clock > timepress + strumHoldPeriod):
	vJoy[vJoyId].setAnalogPov(0, -1)
	timepress = 0

if joystick[joyId].z > 0:
	vJoy[vJoyId].z = filters.mapRange(joystick[joyId].z,-1000,1000, 0,0x8000)
elif joystick[vJoy_joyId].z != joystick[joyId].z:
	vJoy[vJoyId].z = filters.mapRange(joystick[joyId].z,-1000,1000, 0,0x8000)
