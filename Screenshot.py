import keyboard
from PIL import ImageGrab
import pyautogui
from datetime import datetime


def main():
    def on_key_event(e):
        global x_start, y_start, counter, in_boolean, out_boolean, ReloadedTimes,UHcounter #needed global vars

        if e.event_type == keyboard.KEY_DOWN and e.name == "caps lock":
            counter += 1
            if counter % 2 == 0: #If the counter is even ->Initial point.(you can chnge it as needed!)
                x_start, y_start = pyautogui.position()
                print("Press caps lock again!\n")

            elif counter % 2 == 1:#If the counter is even ->End point.
                if x_start is not None and y_start is not None:
                    
                    x_end, y_end = pyautogui.position()
                    width = abs(x_end - x_start)#Calculate the width of the rec
                    height = abs(y_end - y_start)#Calculate the height of the rec
                    if x_start < x_end:#Take screenshot From lefttop to right
                        if y_end < y_start:
                            print("You can only take screenshot starting from Topleft or from buttonright")
                        else:
                            Area = x_start, y_start, width, height
                            take_screenshot(*Area)
                    else:#Take screenshot From buttomright to left
                        if y_end > y_start:
                            print("You can only take screenshot starting from Topleft or from buttonright")      
                        else:
                            Area = x_end, y_end, width, height
                            take_screenshot(*Area)
                    #Unpacking the points of the rec and send it to screenshot process
                else:
                    print("Please press 'd' first to start the selection.")

        elif e.event_type == keyboard.KEY_DOWN and e.name == "s": #For stopping the prog
            print(f"Ended with {((counter-1)//2) * ReloadedTimes} Photos")
            in_boolean, out_boolean = False, False

        elif e.event_type == keyboard.KEY_DOWN and e.name == "r": #For reload the prog
            print(f"Reloaded!")
            in_boolean = False
            


    def take_screenshot(x, y, width, height):
        
        global x_start, y_start, counter
        screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))#A func help me translate the dimensions to a photo rectangle

        #if you need to add time or date
        # current_datetime = datetime.now()
        # current_date = current_datetime.date()
        # current_time = current_datetime.time() y

        nameOfPhoto = f"'{about}' {(counter-1)//2}th ".replace(":", "-")
        screenshot.save(f"C:\\Users\\CRIZMA MEGA STORE\\Desktop\\{nameOfPhoto}.png")
        print(f"Screenshot saved to {nameOfPhoto}\n")
        x_start, y_start = None, None #Re-intializing the start points for another screnntshots

    #subject or topic name
    about = input("What is the subject? ")
    print("Start by caps lock..")

    keyboard.hook(on_key_event)#Start hooking and waiting for Keyboard key event!

    try:
        while in_boolean:
            pass
    except KeyboardInterrupt:

        keyboard.unhook_all()# un hook the keyboard for any unwanted action
#Helping notes
note="""1.First 'caps lock' press to intialize the start position
2.press 'caps lock' again to get the screenshot of the needed rectangle!
3.press 'r' to reload the program for another name
4.press 's' To stop the program
5.press 'tab' For unhooking the keyboard temporary If you want to use the keyboard for writing\n
6.Important Note: You can only take screenshot starting from Topleft or from buttonright\n
"""
print(note)
#Intializing the globlal needed variables
x_start, y_start = None, None
counter = 1 #Number of the photos for each step
ReloadedTimes = 0
UHcounter = 1 #Unhook counter 
in_boolean = True #for inner loop
out_boolean = True #for outer loop
while out_boolean:
    keyboard.unhook_all()
    ReloadedTimes += 1
    in_boolean = True
    counter = 1
    main()
