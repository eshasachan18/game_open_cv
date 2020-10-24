import cv2
import numpy as np
import pyautogui
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
PINK_MIN = np.array([120, 50, 50], np.uint8)
PINK_MAX = np.array([180, 180, 200], np.uint8)
centroid_x = 0
centroid_y = 0
s = ''
move = ''
while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    orig = cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    frame_threshed = cv2.inRange(hsv, PINK_MIN, PINK_MAX)
    contours,hierarchy = cv2.findContours(frame_threshed, 1, 2)

    max_area = 0
    last_x = centroid_x
    last_y = centroid_y
    if contours:
        for i in contours:
            area = cv2.contourArea(i)
            if area > max_area:
                max_area = area
                cnt = i

    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    centroid_x = (x + x + w) / 2
    centroid_y = (y + y + h) / 2

    cv2.line(img, (200, 0), (200, 700), (255, 0, 0), 5)
    cv2.line(img, (500, 0), (500, 700), (255, 0, 0), 5)
    cv2.line(img, (200, 150), (500, 150), (255, 0, 0), 5)
    cv2.line(img, (200, 350), (500, 350), (255, 0, 0), 5)

    # font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # org
    org = (50, 50)

    # fontScale
    fontScale = 1

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2

    cv2.putText(img, 'LEFT', (100,200), font,
                        fontScale, color, thickness, cv2.LINE_AA)
    cv2.putText(img, 'Right', (520,200), font,
                fontScale, color, thickness, cv2.LINE_AA)
    cv2.putText(img, 'Down', (300,400), font,
                fontScale, color, thickness, cv2.LINE_AA)
    cv2.putText(img, 'UP',(300,100), font,
                fontScale, color, thickness, cv2.LINE_AA)
    if centroid_x >= 200 and centroid_x <= 500:
        # up
        if centroid_y >= 0 and centroid_y <= 150:
            print
            'up'
            pyautogui.press('up',presses=1)
            cv2.waitKey(2000)
        # down
        if centroid_y >= 350 and centroid_y <= 700:
            print
            'down'
            pyautogui.press('down',presses=1)
            cv2.waitKey(2000)

        # left-right move
    if centroid_y >= 0 and centroid_y <= 700:
        # left
        if centroid_x >= 0 and centroid_x <= 200:
            print
            'left'
            pyautogui.press('left',presses=1)
            cv2.waitKey(2000)
        # right
        if centroid_x >= 500:
            print
            'right'
            pyautogui.press('right',presses=1)
            cv2.waitKey(2000)

        cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break