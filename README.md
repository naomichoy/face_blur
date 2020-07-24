# face_blur
 
This script modifies from https://github.com/ageitgey/face_recognition/blob/master/examples/ blur_faces_on_webcam.py and find_faces_in_picture_cnn.py to batch process photos in jpg/png format

HI CHING
download the zip file, unzip and have fun. (version 0.1) create a folder called "photos" and a folder called "processed" within this unzipped folder. put your photos in the photos folder.

version 0.1 -- rough script without flexible user directory input and options. some coding skills i've yet to learn. maybe i should include a file of my environment setup too

## DEPENDENCIES
Python 3.3+ is need to run the script. Google how to install python 3 on your mac/windows and follow the steps.

check if the following modules are installed. you need these modules to run the script
* numpy
* scipy
* opencv
* cmake (to install face_recognition)

```bash
pip3 install numpy scipy opencv-python cmake
```

you will also need to install this module I copied from ageitgey

```bash 
pip3 install face_recognition
```

## Running the script
In your terminal, nevigate to the directory where you extracted the zip, run this command

```bash 
python3 batch_process2.py
```

idk maybe directly click and run the script might work too

## BRUH THIS IS SO SLOW / MY LAPTOP FROZE!
sorry this processing eats your computer resources, because pure CPU sucks at image processing.
if your boss has a machine that has a nvidia GPU and dlib compiled with CUDA extensions (if he knows what this is he will understand this), the process can be accelerated
