import pyautogui 
from PIL import Image, ImageGrab
import time

def hiting(key):
    pyautogui.keyDown(key)
    

def isCollide(temp):
    # rectangle for birds
    for i in range(300, 415):
        for j in range(313, 400):
            if temp[i, j] < 100:
                hiting("down")
                
     # rectangle for cactus           
    for i in range(300, 415):
        for j in range(400, 450):
            if temp[i, j] < 100:
                hiting("up")
               
    

if __name__ == "__main__":
    time.sleep(3)

    while True:
        image = ImageGrab.grab().convert('L')  
        temp = image.load()
        isCollide(temp)
            
        '''
        #rectangle for cactus
        for i in range(275, 325):
            for j in range(400, 450):
                temp[i, j] = 0
        
        #rectangle for birds
        for i in range(250, 300):
            for j in range(313, 400):
                temp[i, j] = 171

        image.show()
        break
        '''