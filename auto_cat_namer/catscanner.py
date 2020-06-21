import cv2
HAARS_FILE = "./haarcascade_frontalcatface_extended.xml"
IMG_PATH = "./images/cat_04.jpg"

image = cv2.imread(IMG_PATH)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load the cat detector Haar cascade, then detect cat faces
# in the input image
detector = cv2.CascadeClassifier(HAARS_FILE)
rects = detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=7, minSize=(75, 75))
# rects = detector.detectMultiScale(gray, 1.3, 5)

# loop over the cat faces and draw a rectangle surrounding each
for (i, (x, y, w, h)) in enumerate(rects):
  print(x, y, w, h)
  cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
  cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10),
    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
# show the detected cat faces
cv2.imshow("Cat Faces", image)
cv2.waitKey(0)
