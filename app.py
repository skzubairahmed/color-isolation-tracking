import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    
    if ret is False:
        break

    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    upper_blue = np.array([135, 255, 255])
    lower_blue = np.array([90, 50, 50])

    mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Live Feed", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Isolation result", result)

    if cv2.waitKey(1) and 0xFF == 27:
        break

cv2.destroyAllWindows();
cap.release()