# Script for performing emotion analysis on facial expressions capture via the webcam using DeepFace.
#
# Copyright (C) Saul Johnson 2023
# Author: Saul Johnson <saul.a.johnson@gmail.com>
# Usage: python3 facial_emotion_recognition.py
#
# Used for a 2023 guest lencture at NHL Stenden Leeuwarden.
# See requirements.txt for dependencies.

from deepface import DeepFace
import cv2


# Read image from camera.
camera = cv2.VideoCapture(0)
result, image = camera.read()

# Analyze facial expression
analysis = DeepFace.analyze(image, actions=['emotion'])
emotions = analysis['emotion']

# Print results.
print(emotions)
