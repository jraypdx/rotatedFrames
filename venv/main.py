# Endgame:Procedurally generates layers (circle type shapes) based on a randomly selected
#         predefined shape and color scheme, and rotates it based on differenet speed
#         changing algorithms, and zooms in while procedurally generating more

# Idea:   eventually takes two images and rotates them slowly in oposite directions,
#         then eventually puts them together in a gif/video.  Maybe add zooming effects,
#         in future
#
# Todo:   Make the gui a grid/better layout so it fits

import imageio
from PIL import Image
from appJar import gui
import runProgram

#globals
numlayers = 1
files = []
speeds = []
algs = []

def press(button):
    if button == "Close":
        app.stop()
    else:
        #numLayers = int(app.getEntry("numLayers"))
        # if numLayers <= 0 or numLayers > 8:
        #     numLayers = 1
        for i in range(1,numLayers+1):
            speeds.append(app.getEntry("speed" + str(i)))
            if speeds[i-1] == None or speeds[i-1] == "":
                speeds[i-1] = "1.00"
            algs.append(app.getOptionBox("algs" + str(i)))
        openAfter = app.getCheckBox("Open when finished")
        #backwards = app.getCheckBox("Rotate counterclockwise")
        runProgram.runProgram(openAfter, files, speeds, algs)#, backwards)


#def chooseSaveLocation():
#    app.saveBox(title=None, fileName="rotatedFrames", dirName=None, fileExt=".gif", fileTypes=None, asFile=None, parent=None)


def openNextWindow(button):
    if button == "Close":
        app.stop()
        return
    global numLayers
    numLayers = int(app.getEntry("numLayers"))
    app.removeAllWidgets()

    if numLayers <= 0 or numLayers > 8:
        numLayers = 1

    for i in range(1,numLayers+1):
        if (i == 1):
            layeri = "Layer " + str(i) + " (smallest):"
        else:
            layeri = "Layer " + str(i) + ":"
        dir = app.openBox(title=None, dirName=None, fileTypes=None, asFile=False, parent=None)
        files.append(dir)
        app.addLabel(layeri)
        app.addLabel("Rotation speed: (0.125 - 4.00)" + str(i))
        speedi = "speed" + str(i)
        app.addEntry(speedi)
        algsi = "algs" + str(i)
        app.addLabelOptionBox(algsi, ["- Algorithms -", "clockwise", "counterclockwise",
                                      "1", "2", "3", "4", "5", "6", "7", "8"])

    app.addCheckBox("Open when finished")
    #app.addCheckBox("Rotate counterclockwise")
    #saveDir = app.addButton("Choose save location", chooseSaveLocation)
    app.addButtons(["Render", "Close"], press)
    app.go()

app = gui()
app.addLabel("Number of layers: (1-9)")
app.addEntry("numLayers")
app.addButtons(["Pick files", "Close"], openNextWindow)
app.go()

