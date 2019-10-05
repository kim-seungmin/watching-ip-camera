import cv2
url = 'rtsp://admin:88888888@172.24.1.63:10554/tcp/av0_0'
cap = cv2.VideoCapture(url)
while True:
    ret, image = cap.read()
    cv2.imshow('stream', image)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
