import pyautogui #To click the mouse
import pyscreeze #To compare pixel colours
from PIL import ImageColor #To take a screensht
import time #To add delays
import winsound #To make a beep

wh = pyautogui.size() #Check size of your screen

print(wh)

#VERY IMPORTANT READ THIS vvvvvvvv
# pyautogui.mouseInfo() #use this to open a window which shows which pixel you mouse is on and the color of that pixel(Make sure to comment out everything else)

# wh = pyautogui.pixel(450, 60) #Check color of a specific pixel
# print(wh)

i = 0
while(True):
    time.sleep(1)
    #700, 1100 (255, 221, 76)
    if(pyautogui.pixelMatchesColor(700, 1100, (255, 221, 76))): #Looks to see if you can attack (I have enhanced Mighty Bash so it check for the yellow color, you can change this to check for grey also)
        if(not pyautogui.pixelMatchesColor(1128, 46, (97, 97, 97))): #Beeps if there is a miscrit other than a common miscrit (You can disable this if you don't care about hunting and only care about levelling)
            winsound.Beep(2500, 2000)
            i=i+1
            screenshot = pyautogui.screenshot()
            screenshot.save("Crit"+str(int(i/2))+".png")
            print("Found something other than common")
            time.sleep(120)
            # break
        elif(pyautogui.pixelMatchesColor(1129, 83, (206, 74, 0))):
            winsound.Beep(2500, 1000)
            i = i + 1
            screenshot = pyautogui.screenshot()
            screenshot.save("SRatingMiscrit"+str(int(i/2))+".png")
            print("Found S or S+ Miscrit")
            time.sleep(60)
        else:
            # print("Yellow")
            # i = i + 1  #Uncomment these lines if you wanna keep track of what miscrits you fought while you were gone (Saves screenshots)
            # if(i%2==0):
            #     screenshot = pyautogui.screenshot()
            #     screenshot.save("Miscrit"+str(int(i/2))+".png")
            pyautogui.click(700, 1100)
    #960, 820 (223, 223, 223)
    elif(pyautogui.pixelMatchesColor(960, 820, (223, 223, 223))): #You hit the close button after beating a miscrit
        # print("Grey") 
        pyautogui.click(960, 820)
        time.sleep(1)
        if(pyautogui.pixelMatchesColor(1100, 450, (104, 125, 144))): #You hit the close button after evolving a miscrit (Needed for auto training past every 10 levels) #New Miscrit
            pyautogui.click(950, 785)
            time.sleep(2)
            pyautogui.click(1300, 300)
        elif(pyautogui.pixelMatchesColor(1060, 700, (182,200,225))): #You hit the close button after evolving a miscrit (Needed for auto training past every 10 levels) #Old miscrit
            pyautogui.click(1300, 300)
    #960, 584
    else:
        # print("nothing")
        #450, 60, (51, 135, 234)
        if(pyautogui.pixelMatchesColor(50, 100, (158, 186, 33)) and not pyautogui.pixelMatchesColor(450, 60, (51, 135, 234))):
            print("Training") #You train your miscrit in the second slot
            time.sleep(1)
            pyautogui.click(450, 60)
            time.sleep(1)
            pyautogui.click(720, 400)
            time.sleep(1)
            pyautogui.click(1000, 300)
            # time.sleep(1) # Comment this out
            # pyautogui.click(890, 890) # For plat training (Comment out normally)
            time.sleep(1)
            pyautogui.click(1100, 890)
            time.sleep(2)
            pyautogui.click(960, 700)
            time.sleep(2)
            pyautogui.click(1300, 300)
        else:
            pyautogui.click(960, 582) #Click on the search miscrit prop (You can edit this to click on different things just make sure you are not moving off the object you want to keep searching on)
            # pyautogui.click(955, 575)
            # pyautogui.click(990, 531)
    if(pyautogui.pixelMatchesColor(700, 1100, (24,24,24))):#To stop switch back to VS code, you'll have to change this to stop the program (Make sure to change this or you might get stuck)
        print("exiting")
        break
        #It should also AUTO STOP when you force your mouse to go to any corner of the screen (It's a built-in failsafe)


# if(pyautogui.pixelMatchesColor(960, 820, (223, 223, 223))):
#     print("true")

