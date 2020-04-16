# Vision-Based Guitar Tuner

## Summary

## Background
There are many guitar app tuning by the tone of the guitar. There are three disadvantages of tuning by the tone(sound): not accurate at a noisy place, cannot automatically distinguish string if two strings are in the same range, can only tune one string at a time.
So we want to develop a guitar tuner with a camera. The camera can automatically distinguish which string you are tuning and based on the wavelength. Guitar players can even test which string is off tune by strumming. This method would work perfectly outdoors. 

## The Challenge
For this project, a problem is how to process real-time video to get visual oscillating string images., including determining the position of strings, how to identify strings order and so on.  After dealing with the images, the challenge for us is analyzing the waveform images spectrally. Another consideration is the accuracy of the toner’s identification, and it is a challenge that how to improve the accuracy when strumming. 

## Goals and Deliverables
### To implement a program with the features below:
1. Be able to receive multiple pictures or videos.
2. Be able to recognize the string of the guitar.
3. Be able to gather the physical features that describe how the string vibrates.
4. Be able to analyze the physical features gathered and identify the musical character(such as the scale or notes etc.)

### Potential goals and  of the program. (To make the project more practical)
1. Be able to receive and identify a musical note from a video.
2. Be able to record the correct musical notes to the database and check the musical notes for performers.
3. Be able to record the musical notes of a song and check whether the song is correctly performed.

### The deliverable are listed below.
1. Basic program structure, the center control of the program with the image input module.
2. The image recognition module. (The program should be able to recognize what is in the image at this stage.)
3. The image analysis module.
4. The musical notes or guitar tabs database. (Optional)
5. The real-time images process module. (Optional)

## Schedule

|  Date   | Deliverables to be done  |
|  ----  | ----  |
| Approval of the proposal - 2020-02-05 | Deliverable 1                         |
| 2020-02-05 - 2020-02-29               | Deliverable 2                         |
| 2020-03-01 - 2020-03-10               | Deliverable 3 and Program optimizing  |
| 2020-03-10 - 2020-03-31               | Deliverable 4,5(Optional)             |
| 2020-04-01 - Project Due              | Review                                |

## Result
TODO

***
Please run videoProcessing.py to process the input guitar video

Developed by newest numpy, OpenCV 3.4 and python 3.8
