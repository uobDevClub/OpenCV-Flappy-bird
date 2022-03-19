import cv2

cap = cv2.VideoCapture(0)
face_detection = cv2.CascadeClassifier(cv2.data.haarcascades +
                                       "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()  

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y+h), (255, 0, 0), 2)

    cv2.imshow('frame', frame)  
    if cv2.waitKey(10) == ord('q'):  
        break  

cap.release()
cv2.destroyAllWindows()