# importing
import pyautogui

# getting the size of the pc
screenWidth, screenHeight = pyautogui.size()

# getting the position of the mouse cursor
currentMouseX, currentMouseY = pyautogui.position()

# moving the mouse cursor to a position
pyautogui.moveTo(100, 150)

# clicking on the screen where ever the mouse cursor is
pyautogui.click()

# moving mouse 10 pixels down
pyautogui.moveRel(None, 10)

# double clicking on the screen where ever the mouse cursor is
pyautogui.doubleClick()

# use tweening/easing function to move mouse over 2 seconds.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  

# type with quarter-second pause in between each key
pyautogui.typewrite('Hello world!', interval=0.25)  

# pressing on a specific keyboard button
pyautogui.press('esc')

# holding down a specific keyboard button
pyautogui.keyDown('shift')

# pressing a list of buttons in order
pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])

# releasing the shift button
pyautogui.keyUp('shift')

# using two keys together
pyautogui.hotkey('ctrl', 'c')

# making an alert pop-up
pyautogui.alert(text='YOU ARE BEING WATCHED', title="BE CAREFUL", button="IM NOT SAFE")
