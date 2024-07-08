import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import os
from config import EMOTION_MODEL_PATH

class EmotionDetector:
    def __init__(self):
        self.emotion_model = self.load_emotion_model()
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

    def load_emotion_model(self):
        if os.path.exists(EMOTION_MODEL_PATH):
            return load_model(EMOTION_MODEL_PATH)
        else:
            raise FileNotFoundError(f"Emotion model file not found at {EMOTION_MODEL_PATH}")

    def detect_emotion(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (64, 64))
            roi_gray = roi_gray.astype('float') / 255.0
            roi_gray = img_to_array(roi_gray)
            roi_gray = np.expand_dims(roi_gray, axis=0)

            prediction = self.emotion_model.predict(roi_gray)[0]
            emotion = self.emotions[prediction.argmax()]

            return emotion

        return None

    def capture_emotion(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        if ret:
            return self.detect_emotion(frame)
        else:
            return None