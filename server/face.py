import asyncio


import cv2


from fec.fec.detector import DetectorOpenCV
from fec.fec.emotionclassifier.hseasavchenkomobilenetv1 import EmotionClassifierHSEasavchenkoMobileNetv1


face_detector = DetectorOpenCV()
face_classifier = EmotionClassifierHSEasavchenkoMobileNetv1()
lock = asyncio.Lock()


def analyse_emotion(img: cv2.Mat):
    face_positions = face_detector.detect(img)

    for (x, y, w, h) in face_positions:

        ret = face_classifier.classify(img[y:y+h, x:x+w])

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255))

        return dict(map(lambda d: (d[0], float(d[1])), ret)), img

    return None
