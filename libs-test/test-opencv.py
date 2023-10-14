import cv2

# vid = cv2.VideoCapture('./samples/vdo.mp4')
vid = cv2.VideoCapture('http://192.168.0.106:2160/videostream.cgi?user=admin&pwd=12345678')
# vid = cv2.VideoCapture(0)

while True:
  _,frame = vid.read()
  print(frame)
  cv2.imshow('Video',frame)
  key = cv2.waitKey(1) & 0xFF
  if key ==ord('q'):
    break

vid.release()
cv2.destroyAllWindows()
