import time

start = input("Start the timer? [Y/N]: ")

if start == "y" or "Y":
	timeloop = True
	
Sec = 0
Min = 0

timeloop= start
while timeloop:
	Sec += 1
	print(str(Min), "Min ", str(Sec), "Secs")
	time.sleep(1)
	if Sec == 60:
		Sec = 0
		Min += 1
		print(str(Min), "Minutes")
