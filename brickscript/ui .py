### UILibrary ###

#Standard refresh
def refresh():
	import os
	os.system("tput reset; clear")

#Color Handler
def colorise(text, color, newline):
	#Colors: Red, Blue, Green, Cyan
	import sys
	colors = {
	"red":"\033[1;31m",
	"blue":"\033[1;34m",
	"green":"\033[0;32m",
	"cyan":"\033[1;36m",
	"yellow":"\033[1;33m"
	}
	sys.stdout.write(colors[color])
	print(text) if newline else print(text, end="")
	sys.stdout.write("\033[0;0m")

#Error Handler
def errorMessage(error):
	import time
	colorise("<<Error: {}!>>".format(error), "red", True)
	time.sleep(1)
	return [False]

#Int Component -> Optional; Component
def cInt(question, minima, maxima):
	try:
		ans = int(input(question))
	except:
		return errorMessage("Invalid input")
	else:
		if minima <= ans and ans <= maxima:
			return [True, ans]
		else:
			return errorMessage("Out of range")

#Int IO -> UI Component
def gInt(question, minima, maxima):
	while True:
		refresh()
		ans = cInt(question, minima,maxima)
		if ans[0]:
			return ans[1]

#List IO -> UI Component
def gList(question, items, returnsIndex):
	while True:
		refresh()
		print(question)
		[print("[{}] ".format(i+1) + str(items[i])) for i in range(len(items))]
		ans = cInt(": ", 1, len(items))
		if ans[0]:
			return ans[1]-1 if returnsIndex else items[ans[1]-1]

#Bool IO -> UI Component
def gConfirm(question):
	while True:
		refresh()
		ans = input(question + " [Y/N]: ")
		if ans in ["Y", "y"]:
			return True
		elif ans in ["N", "n"]:
			return False
		else:
			errorMessage("Invalid input")

#Gauge UI -> UI Component
def dGauge(title, withDetail, x, maxima, length, color):
	import sys
	print(title, end="")
	percentage = x/maxima
	units = round(percentage*length*8, 0)
	filledUnits = int(units//8); partialUnits = int(units%8)
	bar = filledUnits * "█" + ["", "▏", "▎", "▍", "▌", "▋", "▊", "▉"][partialUnits]
	bar += (length - filledUnits - (1 if partialUnits > 0 else 0)) * " "
	payload = "▏{}▕".format(bar)
	if withDetail: payload += "\n[{}/{}]".format(x, maxima)
	if color == "":
		if percentage > 0.5: colorise(payload, "green", True)
		elif percentage > 0.3: colorise(payload, "yellow", True)
		else: colorise(payload, "red", True)
	else:
		colorise(payload, color, True)
	
#Gauge UI Demo
def dGaugeDemo():
	for i in range(100):
		import time
		refresh()
		dGauge("SATELLITE MAIN RESERVOIR         ", True, i+1, 100, 40, "")
		dGauge("SATELLITE EMERGENCY FUEL RESERVE ", True, 100-i-1, 100, 40, "")
		time.sleep(0.1)
