import cv2
import face_recognition
import dlib
import numpy as np

# Get a reference to webcam
#video_capture = cv2.VideoCapture("videoplayback.mp4")
video_capture = cv2.VideoCapture(0)

# Initialize variables
face_locations = []
detector = dlib.get_frontal_face_detector()

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    #frame = cv2.flip(frame, 1)

    # Convert the image from BGR color (which OpenCV uses) to RGB colo
    # rgb_frame = frame[:, :, ::-1]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Find all the faces in the current frame of video
    # face_locations = face_recognition.face_locations(rgb_frame)
    faces = detector(gray)
    # if faces:
    #print("FACE FOUND...")
    # else:
    #print("NO FACE...")
    # Display the results
    i = 0
    #frame = cv2.flip(frame, 1)
    for face in faces:

        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (12, 12, 12), 2)
        i += 1
        cv2.putText(frame, 'faces : '+str(i), (x-10, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    #print(face, i)
    # Display the resulting image
    cv2.imshow("FACE COUNTER", frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
