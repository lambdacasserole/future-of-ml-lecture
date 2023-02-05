# Looking to the Future of Machine Learning
Source code for my 2023 guest lecture on the future of machine learning at NHL Stenden Leeuwarden.

![Looking to the Future of Machine Learning: Lecture by Saul Johnson](header.png)

## Prerequisites
To run this project, you'll need:

* Python 3.6 or later with pip and virtual environments

## Setup
Setup will vary depending on whether you're using Windows or Mac/Linux. A script is included for each OS that will do the following for you:

* Delete any existing virtual environment for this project
* Provision fresh virtual environment
* Install all dependencies for this project in that virtual environment

### Windows
On Windows, execute `setup-venv.bat` via your command prompt from the root directory of the repository:

```
./setup-venv.bat
```

### On Mac/Linux
On Mac/Linux, execute `setup-venv.sh` via your terminal from the root directory of the repository. Make sure to invoke it using `bash`:

```
bash ./setup-venv.sh
```

## Using the Examples
Each example this session is quite different. Before you'll be able to run any of them, however, you'll need to make sure you're in the virtual environment we set up earlier:

* **On Windows** - Run `./venv/Scripts/activate` in your command prompt from the repo root directory
* **On Mac/Linux** - Tun `. venv/bin/activate` in your terminal from the repo root directory

### Classr MLaaS (`./classr_example.py`)
This example demonstrates using the online machine-learning-as-a-service (MLaaS) platform [Classr](https;//classr.dev) to train a text classification model in the cloud and use it to classify a text input from a Python program on your local machine.

You can train a classifier yourself by logging in with your GitHub account on the Classr platform [here](https;//classr.dev) and swap out the ID in `classr_example.py` with your own to use it instead of the default (an SMS spam classifier):

```python
cloud_classifier = Classr('<your-classifier-id>')
```

Run it like this:

```bash
python classr_example.py
```

### Facial Emotion Recognition (`./facial_emotion_recognition.py`)
This example will capture an image from your webcam and use the [DeepFace](https://github.com/serengil/deepface) library to perform a facial expression analysis on it. It will then print the results of this analysis to the command line. Run it like this:

```
python facial_emotion_recognition.py
```

Note that this script will throw an error if it fails to detect a face. Don't worry if this happens, just give it another try! You'll get output that looks something like this:

```
{
  'angry': 0.05649591330438852,
  'disgust': 5.57847656956767e-09,
  'fear': 74.32841062545776,
  'happy': 3.6657944235685136e-06,
  'sad': 21.667467057704926,
  'surprise': 0.005379965659813024,
  'neutral': 3.942243754863739,
}
```

Each of these numbers shows a confidence score (out of 100) that the given emotion is present in the facial expression of the individual pictured.

### Speech Recognition (`./speech_recognition.py`)
This example will take input via the computer's microphone and attempt to transcribe it into accurate text (it's not always 100% accurate). Run it like this:

```bash
python3 speech_recognition.py
```

## Limitations
These examples are just that: examples. They're designed to be the absolute minimum required to get something working. Why not try building upon them or chaining them together into something more advanced?

