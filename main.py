# Main frogram for AR testbench
# bench top and HMD both available
# by KYD since 20180514


from tkinter import *
from tkinter import messagebox
from picamera import PiCamera

import time
#test git


running = True  # Global flag
idx = 0  # loop index

# Camera setting
# with picamera.PiCamera() as camera:
# camera.resolution = (1024, 768)

camera = PiCamera()
camera.resolution = (1024, 768)


def start():
    """Enable Capturing by setting the global flag to True."""
    global running
    running = True
    messagebox.showinfo("Camera mode","Start image grab")
    camera.start_preview(fullscreen=False, window = (100,20,612,404))

def stop():
    """Stop Capturing by setting the global flag to False."""
    global running
    running = False
    messagebox.showinfo("Camera mode","Stop image grab")
    camera.stop_preview()


root = Tk()
root.title("Camera Image grab")
root.geometry("1500x1000")

app = Frame(root)
app.grid()

start = Button(app, text="Start Camera", command=start)
stop = Button(app, text="Stop Camera", command=stop)

start.grid()
stop.grid()

root.mainloop()


"""
while True:
    if idx % 500 == 0:
        root.update()

    if running:
        print("hello andrew")
        idx += 1

"""
