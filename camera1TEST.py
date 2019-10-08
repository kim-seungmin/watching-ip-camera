import cv2
rtsp = 'ur rtsp address'
cap = cv2.VideoCapture(rtsp)
while True:
    ret, image = cap.read()
    cv2.imshow('stream', image)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
