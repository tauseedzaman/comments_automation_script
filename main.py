import pyautogui
import time

# wait for 3 sec
time.sleep(3)
# start from 0 and move ......
i =0

while True:
	# wait for 0.2 sec
	time.sleep(0.2)
	# write in the focused field number and imoji
	pyautogui.typewrite(""+str(i)+" :)")
	# press enter to sumbit
	pyautogui.press('enter')
	i = i+1
