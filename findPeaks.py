import cv2

# np is an alias pointing to numpy library
import numpy as np

# capture frames from a camera
cap = cv2.VideoCapture("sample.mp4")

# loop runs if capturing has been initialized
while (cap.isOpened()):
    # reads frames from video
    ret, frame = cap.read()

    # converting BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of red color in HSV
    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    # create a red HSV colour boundary and
    # threshold HSV image
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Display an original image
    cv2.imshow('Original', frame)

    # apply gaussian filter
    frame = cv2.GaussianBlur(frame, (9, 9), 0)

    cv2.imshow('blur', frame)

    # finds edges in the input image image and
    # marks them in the output map edges
    edges = cv2.Canny(frame, 100, 200, apertureSize = 3)

    # Display edges in a frame
    cv2.imshow('Edges', edges)

    # Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()