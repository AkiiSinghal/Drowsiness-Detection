# Drowsiness-Detection
Driver fatigue is one of the major causes of accidents in the world. Detecting the drowsiness of the driver is one of the surest ways
of measuring driver fatigue. In this project we aim to develop a prototype drowsiness detection system. This system works by monitoring
the eyes and mouth of the driver and sounding an alarm when he/she is drowsy. The programming for this is done in OpenCV using the Dlib
library for the detection of facial features.

## Installations
1. Install Python 3.6 in your system.
   * Click [here](https://www.python.org/downloads/release/python-368/) to install.
2. Now install OpenCV and dlib also.
   * Click [here](https://pypi.org/project/opencv-python/) to install OpenCV.
   * To install Dlib :
     * Download [dlib-19.8.1-cp36-cp36m-win_amd64.whl](https://files.pythonhosted.org/packages/0e/ce/f8a3cff33ac03a8219768f0694c5d703c8e037e6aba2e865f9bae22ed63c/dlib-19.8.1-cp36-cp36m-win_amd64.whl#sha256=794994fa2c54e7776659fddb148363a5556468a6d5d46be8dad311722d54bfcf).
     * Use cmd to navigate to the file directory and use command ***pip install dlib-19.8.1-cp36-cp36m-win_amd64.whl*** to install dlib.

## Implementation
1. To change the camera use 0 for internal camera and 1 for external webcam in the **cap = cv2.VideoCapture(0)** of [Drowsiness_detection.py](https://github.com/AkiiSinghal/Drowsiness-Detection/blob/master/Drowsiness_detection.py).
2. Run using ***python Drowsiness_detection.py*** command.

## Screenshots
![Screenshot (27)~2](https://user-images.githubusercontent.com/42001728/62093938-d7fd8500-b298-11e9-95ec-e76a99b31a45.png)
![Screenshot (29)~2](https://user-images.githubusercontent.com/42001728/62093939-d8961b80-b298-11e9-839b-6710de285be5.png)
![Screenshot (46)~2](https://user-images.githubusercontent.com/42001728/62093941-d8961b80-b298-11e9-927d-3a71df9933d8.png)
