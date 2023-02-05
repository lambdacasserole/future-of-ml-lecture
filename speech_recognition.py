# Script for performing speech-to-text on sound captured via the microphone.
#
# Copyright (C) Saul Johnson 2023
# Author: Saul Johnson <saul.a.johnson@gmail.com>
# Usage: python3 speech_recognition.py
#
# Used for a 2023 guest lencture at NHL Stenden Leeuwarden.
# See requirements.txt for dependencies.

import speech_recognition as sr


# Initialize speech recognition engine.
recognizer = sr.Recognizer()

# Use the microphone to get audio...
with sr.Microphone() as mic:

    # Filter out background noise.
    recognizer.adjust_for_ambient_noise(mic, duration=0.2)

    # Capture audio, turn it into text.
    audio = recognizer.listen(mic)
    text = recognizer.recognize_google(audio)

    # Print results.
    print('It sounded like you said: ', text)
