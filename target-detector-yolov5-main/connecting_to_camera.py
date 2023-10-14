import numpy as np
import cv2 as cv
from camera import connect_camera
from datetime import datetime
import time
from pathlib import Path
import os
import random
    
cap = connect_camera()
if not cap.isOpened():
    exit()
    
img_dir = Path('./school_bus_images/')
    
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    ###  resizing so it won't be so huge
    frame = cv.resize(frame, (int(frame.shape[1] * .5), int(frame.shape[0] * .5)))
    now = datetime.now()
    
    filename = now.strftime("%m-%d-%Y_%H-%M-%S-%f") + ".jpg"
    day = now.strftime("%m-%d-%Y")
    hour = now.strftime("%H")
    filepath = img_dir / day / hour / filename
    if not (img_dir / day).exists():
        os.mkdir(img_dir / day)
    if not (img_dir / day / hour).exists():
        os.mkdir(img_dir / day / hour)
      
    cv.imwrite(str(filepath), frame)
    #cv.imshow('frame', frame)
    time.sleep(0.1)
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break        
            
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()