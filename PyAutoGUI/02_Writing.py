import pyautogui as pg
import time

time.sleep(3)
pg.click()
messages = 0
while True:
    pg.write("hello")
    pg.press('enter')
    messages += 1
    time.sleep(0.2)