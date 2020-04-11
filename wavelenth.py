import cv2
import numpy as np
from matplotlib import pyplot as plt

def getResultAndWavelenth(matches):
    location = [[matches[0][0]],[matches[1][0]]]

    for i in range(1,len(matches[1])):
        if matches[1][i] - matches[1][i-1] > 5:
            location[0].append(matches[0][i])
            location[1].append(matches[1][i])


    print(location)

    wavelenth = 0
    for i in range(1,len(location[1])):
        lenth = np.sqrt((location[1][i]-location[1][i-1])**2 + (location[0][i]-location[0][i-1])**2)
        print(lenth)
        wavelenth += lenth

        

    wavelenth /= (len(location[1]) - 1)
    print(wavelenth)

    return location,wavelenth

