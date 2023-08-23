import threading
import time 
import keyboard

# ===========================

direction = None

def printer():
    while True:
        global direction
        time.sleep(1)
        print(direction, flush=True)

def direction_changer():
    while True:
        global direction
        new_direction = keyboard.read_key()
        direction = new_direction


printer_thread = threading.Thread(target=printer)
direction_changer_thread = threading.Thread(target=direction_changer)

printer_thread.start()
direction_changer_thread.start()

# this is a test and i was trying to understand threading to use it in a bigger project