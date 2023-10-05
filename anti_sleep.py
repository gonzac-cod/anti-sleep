import pyautogui
import time
import sched

pyautogui.FAILSAFE = False

def centerPointer():
	global MAX_X, MAX_Y
	screen_width, screen_height = pyautogui.size()
	MAX_X, MAX_Y = (screen_width, screen_height)
	x, y = screen_width // 2, screen_height // 2
	pyautogui.moveTo(x, y)

def movePointer(schedule):
	print("Simulating activity")
	initial_x, initial_y = pyautogui.position()

	new_x = initial_x + 1 if 0 <= initial_x <= MAX_X else initial_x - 1
	new_y = initial_y + 1 if 0 <= initial_y <= MAX_Y else initial_y - 1

	pyautogui.moveTo(new_x, new_y)
	pyautogui.moveTo(initial_x, initial_y)
	schedule.enter(1800, 1, movePointer, (schedule,))

def createSchedule():
	schedule = sched.scheduler(time.time, time.sleep)
	schedule.enter(0, 1, movePointer, (schedule,))
	schedule.run()

def main():
	centerPointer()
	createSchedule()

if __name__ == "__main__":
    main()
