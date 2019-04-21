import os
from PIL import Image
import speedAlgs
import imageio

def runProgram(openAfter, files, speeds, algs):
    numFrames = 360
    openImages = []
    imageList = []

    for file in files:
        openImages.append(Image.open(file))
    numLayers = len(openImages)

    for i in range(0, numFrames):
        temp = openImages.copy()
        temp = temp[::-1]
        for j in range(0, numLayers):
            temp[j] = temp[j].rotate(speedAlgs.callAlg(algs[j], i/(1/float(speeds[j]))))
        for k in range(0, numLayers):
            if k < numLayers-1:
                temp[k+1] = Image.alpha_composite(temp[k], temp[k+1])
        imageList.append(temp[numLayers-1])

    imageio.mimsave(r"C:\Users\Josh\Desktop\mandalaTest\test.gif", imageList)

    if openAfter:
        os.startfile(r"C:\Users\Josh\Desktop\mandalaTest\test.gif")

