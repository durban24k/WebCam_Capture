import cv2, time

capture=cv2.VideoCapture(0) # Creating a camera object
a=0
while True:
    a=a+1
    check, frame= capture.read() # creating a frame object 
    print(check)
    print(frame) # image
    gray_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # conversion to grayscale
    cv2.imshow("Imaging",gray_scale) # Showing the frame
    # cv2.waitKey(0) # Press any key to break the capture
    key=cv2.waitKey(1) #  To initiate stream

    if key == ord('q'):
        break

print(a)
capture.release() # Shutting down the camera
cv2.destroyAllWindows