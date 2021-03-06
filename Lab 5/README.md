# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

In Lab 5 part 1, we focus on detecting and sense-making.

In Lab 5 part 2, we'll incorporate interactive responses.


## Prep

1.  Pull the new Github Repo.
2.  Read about [OpenCV](https://opencv.org/about/).
3.  Read Belloti, et al's [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf)

### For the lab, you will need:

1. Raspberry Pi
1. Raspberry Pi Camera (2.1)
1. Microphone (if you want speech or sound input)
1. Webcam (if you want to be able to locate the camera more flexibly than the Pi Camera)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.


## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

Befor you get started connect the RaspberryPi Camera V2. [The Pi hut has a great explanation on how to do that](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera).  

#### OpenCV
A more traditional to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python.

Additionally, we also included 4 standard OpenCV examples. These examples include contour(blob) detection, face detection with the ``Haarcascade``, flow detection(a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (I.e. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example.

```shell
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```
#### Filtering, FFTs, and Time Series data. (beta, optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the set up from the [Lab 3 demo](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Spring2021/Lab%203/demo) and the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

Include links to your code here, and put the code for these in your repo--they will come in handy later.

#### Teachable Machines (beta, optional)
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple.  However, its simplicity is very useful for experimenting with the capabilities of this technology.

You can train a Model on your browser, experiment with its performance, and then port it to the Raspberry Pi to do even its task on the device.

Here is Adafruit's directions on using Raspberry Pi and the Pi camera with Teachable Machines:

1. [Setup](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/raspberry-pi-setup)
2. Install Tensorflow: Like [this](https://learn.adafruit.com/running-tensorflow-lite-on-the-raspberry-pi-4/tensorflow-lite-2-setup), but use this [pre-built binary](https://github.com/bitsy-ai/tensorflow-arm-bin/) [the file](https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0/tensorflow-2.4.0-cp37-none-linux_armv7l.whl) for Tensorflow, it will speed things up a lot.
3. [Collect data and train models using the PiCam](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/training)
4. [Export and run trained models on the Pi](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/transferring-to-the-pi)

Alternative less steps option is [here](https://github.com/FAR-Lab/TensorflowonThePi).

#### PyTorch  
As a note, the global Python install contains also a PyTorch installation. That can be experimented with as well if you are so inclined.


### Screenshots of different sense-making algorithms:

#### Contours-detection:
![Contours-detection](https://github.com/andrewljc0801/Interactive-Lab-Hub/blob/Spring2021/Lab%205/OpenCV_Examples_Screenshots/contour_out.jpg?raw=true)

#### Face-detection:
![Face-detection](https://github.com/andrewljc0801/Interactive-Lab-Hub/blob/Spring2021/Lab%205/OpenCV_Examples_Screenshots/faces_detected.jpg?raw=true)

#### Flow-detection:
![Flow-detection](https://github.com/andrewljc0801/Interactive-Lab-Hub/blob/Spring2021/Lab%205/OpenCV_Examples_Screenshots/flow.png?raw=true)

#### Object-detection:
![Object-detection](https://github.com/andrewljc0801/Interactive-Lab-Hub/blob/Spring2021/Lab%205/OpenCV_Examples_Screenshots/detected_out.jpg?raw=true)

#### Google Teachable Machines:
![car](https://github.com/andrewljc0801/Interactive-Lab-Hub/blob/Spring2021/Lab%205/OpenCV_Examples_Screenshots/car.png?raw=true)

### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interactions outputs and inputs.
**Describe and detail the interaction, as well as your experimentation.**

### I tried the Google Teachable Machines and used the image classification. First, I put some images of car, human, and wall as the dataset to train the model. Then, when I displayed a particular object to the camera, the percentage in the output demonstrated the prediction. In other words, it's predicted as the object with higher percentage. (See the examples experimentations for how it worked.) 

### Google Teachable Machines:
![car](https://github.com/andrewljc0801/Interactive-Lab-Hub/blob/Spring2021/Lab%205/OpenCV_Examples_Screenshots/car.png?raw=true)
![human](https://github.com/andrewljc0801/Interactive-Lab-Hub/blob/Spring2021/Lab%205/OpenCV_Examples_Screenshots/person.png?raw=true)
![wall](https://github.com/andrewljc0801/Interactive-Lab-Hub/blob/Spring2021/Lab%205/OpenCV_Examples_Screenshots/wall.png?raw=true)


#### I designed a visual assistant device for people who are visually impaired, called "Vision". The main goal of this device is to help people recognize the objects that are in front of them and use audio output to tell what the objects are. I will answer the questions in C and D regarding my project after "Part 2". 


### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.


#### Desgin of "Vision":
![design](https://github.com/andrewljc0801/Interactive-Lab-Hub/blob/Spring2021/Lab%205/Vision%20Design.jpg?raw=true)


### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note your observations**:
For example:
1. When does it do what it is supposed to do? 

*When the recognizable objects present in front of it. (Car, Wall and Human)*

2. When does it fail? 

*Mostly if an unrecognizable object presents (like cup, colorful pictures, etc), it gives the wrong result.*

3. When it fails, why does it fail? 

*Because the model has never seen the object before or it has similar characteristics with recognizable objects.*
 
4. Based on the behavior you have seen, what other scenarios could cause problems? 

*Poor lighting environment, unseen objects, similar shape objects.*

**Think about someone using the system. Describe how you think this will work.**
1. Are they aware of the uncertainties in the system? 

*I tried to handle the situation that if an unrelated object present, "Vision" will tell people to ask someone to help them identify what it is. However, if the object is classified incorrectly (a car is detected as "wall"), the users won't know.*

2. How bad would they be impacted by a miss classification? 

*Since "Vision" is designed to help visually impaired people recognize the objects that are in front of them and use audio output to tell them what they are, wrong classifications would cause some troubles. For example, if "Vision" detects a car as a human, the user might have safety issue.*

3. How could change your interactive system to address this? 

*One simple way is always prompting the users being aware that the system might give the wrong results.*

4. Are there optimizations you can try to do on your sense-making algorithm. 

*Beside the simple solution mentioned above, another approach is optimizing the dataset to cover more possible objects.*

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use "Vision" for?

*It can be used to recognize things. The goal of "Vision" is to help people recognize the objects that are in front of them and use audio output to tell them what the objects are.*

* What is a good environment for "Vision"?

*Adequate lighting enviornment and not many objects appear in a single time.*

* What is a bad environment for "Vision"?

*Poor lighting enviornment and many objects appear in a single time or even objects that have never seen before.*

* When will "Vision" break?

*It breaks when the objects that have never seen before appear, and sometimes when multiple recognizable objects appear. Though it rarely happened, it also breaks when single recognizable object appear but is incorrectly classified.*

* When it breaks, how will "Vision" break?

*It simply gives the user wrong output. For example, a "tape" is placed in front of the camera, but it is incorrectly classified as "car". Therefore, "Vision" says "Watch out! There is a car in front of you. Ask somebody for help!". Ideally, it's supposed to say "Cannot recognize the object. Maybe ask someone for help.".*

* What are other properties/behaviors of "Vision"?

*"Vision" will not keep speaking if no new object is detected (eliminate potential annoyance). It also handle the situation that an object which has never seen before appears.*

* How does "Vision" feel?

*It is designed as an easy-carry device (very light - 0.06 pound) that people can hang on their chest and the sound will be played via bluetooth headphones. It's convienient for visually impaired people to take with them and go out.*


**Include a short video demonstrating the answers to these questions.**

#### Here is the final demo video:

https://drive.google.com/file/d/1c2_Qysjla18U5fR-h_k50MSjZpwJFlQ8/view?usp=sharing
