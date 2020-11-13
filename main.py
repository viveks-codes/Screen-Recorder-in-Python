import cv2
import numpy as np
import pyautogui


"""
display screen resolution, get it from your OS settings
Note: You need to get the correct SCREEN_SIZE from your operating system,
that is the screen resolution, otherwise writing to the file won't work (alternatively, 
you can use pyautogui.size() function to get the size of the primary monitor).
"""
SCREEN_SIZE = (1920, 1080)
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# create the video write object
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

while True:
    # make a screenshot
   
    img = pyautogui.screenshot() 
    
    """
    use
    img = pyautogui.screenshot(region=(0, 0, 300, 400))
    to capture specific region 
    """
    
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)
    # show the frame
    cv2.imshow("screenshot", frame)
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break

# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()
