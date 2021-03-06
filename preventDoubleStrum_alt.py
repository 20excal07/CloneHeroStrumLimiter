import time

if starting:
	strumHoldPeriod = 1/30.0		#seconds (default: 1/30th of a second)
	vJoyId = 0
	vJoy_joyId = "vJoy Device"
	
	joyId = -1
	isDetecting = True
	info = "Please strum on the guitar controller you would like to use."
	diagnostics.watch(info)
	
	if vJoy[vJoyId].axisMax != -1:
		vjAxisMax = vJoy[vJoyId].axisMax
		vjAxisMin = -vJoy[vJoyId].axisMax
	else:
		vjAxisMax = 0x8000
		vjAxisMin = 0

if isDetecting:
	for x in range(5):
		try:
			if(joystick[x].pov[0] != -1):
				joyId = x
		except:
			pass
	if joyId != -1:
		isDetecting = False
		system.setThreadTiming(TimingTypes.HighresSystemTimer)
		system.threadExecutionInterval = 1000 / 120
		strumDir = -1
		strummed = False
		timepress = 0
		info = "Using guitar controller of ID "+str(joyId)+". Have fun!"
		diagnostics.watch(info)
		strums_blocked = 0
else:
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
			if joystick[joyId].pov[0] != strumDir:
				vJoy[vJoyId].setAnalogPov(0, joystick[joyId].pov[0])
				strummed = True
			else:
				strums_blocked += 1
				diagnostics.watch(strums_blocked)
			strumDir = joystick[joyId].pov[0]
	
	if (timepress > 0):
		if(strummed and clock > timepress + 0.001):
			vJoy[vJoyId].setAnalogPov(0, -1)
			strummed = False
		if(clock > timepress + strumHoldPeriod):	
			strumDir = -1
			timepress = 0
	
	if joystick[joyId].z > 0:
		vJoy[vJoyId].z = filters.mapRange(joystick[joyId].z, -1000, 1000, vjAxisMin, vjAxisMax)
	elif joystick[vJoy_joyId].z != joystick[joyId].z:
		vJoy[vJoyId].z = filters.mapRange(joystick[joyId].z, -1000, 1000, vjAxisMin, vjAxisMax)
