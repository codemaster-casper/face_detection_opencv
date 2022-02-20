#!/usr/bin/python3


#importing opencv lib
import cv2

#creating object for face cascade classifire. 
face_cascade_classifire = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#capting voideo in an object. 0 attribute defines the default camera source
cap = cv2.VideoCapture(0)

#Video is a continous sequence of franes. Creating infinite loop to show to frames continously. 
while True:

    #Readtingg the video source object and storing each frame in the "frame"
    #"success" returns a boolean value for the frame storage operation
    sucess, frame = cap.read()

    #Converting Color frame to gray, since the classifire works with BnW only
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #implementing the face cascade classifire to the gray franmes
    faces = face_cascade_classifire.detectMultiScale(gray_frame,1.1,4)

    #creating a bounding box around the face and passing original frame "frame" in argument
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    #Displaying frame by frame in a window a video
    cv2.imshow("Video", frame)

    #dislplaying the each frame for 1ms and quitting by pressing "q" 
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break

#releasing the source camera 
cap.release()

#to distroy all the windows we created
cv2.destroyAllWindows()
