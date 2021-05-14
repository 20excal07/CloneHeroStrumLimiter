import time

if starting:
	strumHoldPeriod = 0.033333		#seconds (default: 1/30th of a second)
	vJoyId = 0
	joyId = 1
	
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = 1000 / 120
	timepress = 0

if keyboard.getPressed(Key.Space) is True:
	vJoy[vJoyId].setPressed(0)

for i in range(13):
	vJoy[vJoyId].setButton(i, joystick[joyId].getDown(i))

if joystick[joyId].pov[0] != -1:
	timepress = time.clock()
	vJoy[vJoyId].setAnalogPov(0, joystick[joyId].pov[0])

if (timepress > 0 and time.clock() > timepress + strumHoldPeriod):
	vJoy[vJoyId].setAnalogPov(0, -1)
	timepress = 0

vJoy[vJoyId].z = filters.mapRange(joystick[joyId].z,-1000,1000, 0,0x8000)
