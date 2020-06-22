import cv2
from pathlib import Path
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
HAARS_FILENAME = "./haarcascade_frontalcatface_extended.xml"
HAARS_FILE = os.path.join(ROOT_DIR, HAARS_FILENAME)


def write_name_to_image(name, image_path, output_path):
    image_path = Path(image_path).resolve()
    suffix = image_path.suffix
    image_path = str(image_path)
    output_path = Path(output_path).resolve()
    full_output_path = str(Path("%s/%s%s" % (output_path, name, suffix)))

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = cv2.CascadeClassifier(HAARS_FILE)
    rects = detector.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=7, minSize=(75, 75)
    )

    if len(rects) == 0:
        raise ValueError("Could not detect cat's face location")

    x, y, w, h = rects[0]
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(
        image, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2,
    )
    cv2.imwrite(full_output_path, image)
