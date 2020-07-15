from subprocess import call
call(["screenshot", "Chrome", "-w all_window", '-f board.png'])

import cv2
img = cv2.imread(" board.png")
import os
print(os.listdir('.'))
crop_img = img[230:1646, 405:1821]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)