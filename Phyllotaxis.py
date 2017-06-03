'''
Created on Dec 17, 2016

@author: Eisah
'''
import math, tkinter, time, colorsys
from tkinter.constants import GROOVE, RIDGE, SUNKEN, RAISED
from tkinter import colorchooser

stop = False
mainColor = None

#Create the main window       
master = tkinter.Tk()
master.title("Phyllotaxis Algorithm Animator")

#Create the main canvas where the animation occurs
canvas = tkinter.Canvas(master, width = 400, height = 400)
canvas.config(background = "#000000")
canvas.grid(column = 0, row = 0)

# This handles all of the angle information; a in the formula
canvas.angleFrame = tkinter.Frame(master, height = 1, width = 3)
canvas.angleFrame.grid(column = 0, row = 2, sticky = tkinter.W)
canvas.angleLabel = tkinter.Label(canvas.angleFrame, text = "Angle")
canvas.angleLabel.grid(column = 0, row = 0, sticky = tkinter.W, padx = 10, pady = 5)
sVar = tkinter.StringVar()
sVar.set('-')
canvas.angleEntry = tkinter.Entry(canvas.angleFrame, width = 8, text = sVar)
canvas.angleEntry.grid(column = 1, row = 0, padx = 10, pady = 5)
canvas.angleSuggestion = tkinter.Label(canvas.angleFrame, text = "(Try 137.3, 137.5, or 137.7)")
canvas.angleSuggestion.grid(column = 2, row = 0, padx = 20, pady = 5)

# This handles the circle density information; c in the formula
canvas.densityFrame = tkinter.Frame(master, height = 1, width = 3)
canvas.densityFrame.grid(column = 0, row = 3, sticky = tkinter.W)
canvas.densityLabel = tkinter.Label(canvas.densityFrame, text = "Circle Density")
canvas.densityLabel.grid(column = 0, row = 0, sticky = tkinter.W, padx = 10, pady = 5)
canvas.densityEntry = tkinter.Spinbox(canvas.densityFrame, from_ = 2, to = 20, width = 2)
canvas.densityEntry.grid(column = 1, row = 0, padx = 10, pady = 5)

def getColor():
    global mainColor
    color = colorchooser.askcolor()
    if color[0] != None:
        mainColor = color
    
def resetColor():
    stopAnim()
    global mainColor
    mainColor = None

# Color picker that overrides the hue field 
canvas.colorFrame = tkinter.Frame(master, height = 1, width = 3, relief = RAISED, borderwidth = 5)
canvas.colorFrame.grid(column = 0, row = 4, sticky = tkinter.W, padx = 10)
canvas.colorButton = tkinter.Button(canvas.colorFrame, text = "Choose Color", command = getColor)
canvas.colorButton.grid(column = 0, row = 0, sticky = tkinter.W)
canvas.colorClear = tkinter.Button(canvas.colorFrame, text = "Clear Color", command = resetColor)
canvas.colorClear.grid(column = 1, row = 0, sticky = tkinter.W)
canvas.colorLabel = tkinter.Label(canvas.colorFrame, text = "Overrides Hue selections\nClear to use Hue values   ")
canvas.colorLabel.grid(column = 2, row = 0)

tkinter.Label(master, text = "Hue Saturation Value Picker").grid(column = 0, row = 5, sticky = tkinter.W, padx = 10, pady = 10)

# Establishes lists with the necessary variables for changing values
options = ['None', 'n', 'a', 'r', 'x', 'y']
operators = ['None', '+', '-', '/', '*']

# Creates the frame for the tkinter Listboxes
canvas.hFrame = tkinter.Frame(master, height = 3, width = 5)
canvas.hFrame.grid(column = 0, row = 7, sticky = tkinter.W)
tkinter.Label(master, text = "   Hue\t\tSaturation\t              Luminosity").grid(column = 0, row = 6, sticky = tkinter.W)
tkinter.LabelFrame(canvas.hFrame, width = 13).grid(column = 0, row = 1)

# Listboxes for the Hue
canvas.hueBox1 = tkinter.Listbox(canvas.hFrame, height = 6, width = 4, exportselection = 0, activestyle = "none")
for i in enumerate(options, 1):
    canvas.hueBox1.insert(i[0], i[1])
canvas.hueBox1.grid(column = 1, row = 1, padx = 1)
canvas.hueBox1.select_set(0)

canvas.hueBox2 = tkinter.Listbox(canvas.hFrame, height = 6, width = 4, exportselection = 0, activestyle = "none")
for i in enumerate(operators, 1):
    canvas.hueBox2.insert(i[0], i[1])
canvas.hueBox2.grid(column = 2, row = 1, padx = 1)
canvas.hueBox2.select_set(0)

canvas.hueBox3 = tkinter.Listbox(canvas.hFrame, height = 6, width = 4, exportselection = 0, activestyle = "none")
for i in enumerate(options, 1):
    canvas.hueBox3.insert(i[0], i[1])
canvas.hueBox3.grid(column = 3, row = 1, padx = 1)
canvas.hueBox3.select_set(0)

tkinter.LabelFrame(canvas.hFrame, width = 10).grid(column = 4, row = 1)

# Listboxes for the Saturation
canvas.satBox1 = tkinter.Listbox(canvas.hFrame, height = 6, width = 4, exportselection = 0, activestyle = "none")
for i in enumerate(options, 1):
    canvas.satBox1.insert(i[0], i[1])
canvas.satBox1.grid(column = 5, row = 1, padx = 1)
canvas.satBox1.select_set(0)

canvas.satBox2 = tkinter.Listbox(canvas.hFrame, height = 6, width = 4, exportselection = 0, activestyle = "none")
for i in enumerate(operators, 1):
    canvas.satBox2.insert(i[0], i[1])
canvas.satBox2.grid(column = 6, row = 1, padx = 1)
canvas.satBox2.select_set(0)

canvas.satBox3 = tkinter.Listbox(canvas.hFrame, height = 6, width = 4, exportselection = 0, activestyle = "none")
for i in enumerate(options, 1):
    canvas.satBox3.insert(i[0], i[1])
canvas.satBox3.grid(column = 7, row = 1, padx = 1)
canvas.satBox3.select_set(0)

tkinter.LabelFrame(canvas.hFrame, width = 10).grid(column = 8, row = 1)

# Listboxes for the Luminosity or Value
canvas.valBox1 = tkinter.Listbox(canvas.hFrame, height = 6, width = 4, exportselection = 0, activestyle = "none")
for i in enumerate(options, 1):
    canvas.valBox1.insert(i[0], i[1])
canvas.valBox1.grid(column = 9, row = 1, padx = 1)
canvas.valBox1.select_set(0)

canvas.valBox2 = tkinter.Listbox(canvas.hFrame, height = 6, width = 4, exportselection = 0, activestyle = "none")
for i in enumerate(operators, 1):
    canvas.valBox2.insert(i[0], i[1])
canvas.valBox2.grid(column = 10, row = 1, padx = 1)
canvas.valBox2.select_set(0)

canvas.valBox3 = tkinter.Listbox(canvas.hFrame, height = 6, width = 4, exportselection = 0, activestyle = "none")
for i in enumerate(options, 1):
    canvas.valBox3.insert(i[0], i[1])
canvas.valBox3.grid(column = 11, row = 1, padx = 1, pady = 3)
canvas.valBox3.select_set(0)

# Frame and contents for the key
canvas.keyFrame = tkinter.Frame(master, height = 3, width = 1)
canvas.keyFrame.grid(column = 0, row = 8, sticky = tkinter.W, pady = 10)
tkinter.Label(canvas.keyFrame, text = "Key: n = dot number   a = angle from origin").grid(column = 0, row = 0, sticky = tkinter.W, padx = 10)
tkinter.Label(canvas.keyFrame, text = "        r = radius from origin   x = x coordinate of dot").grid(column = 0, row = 1, sticky = tkinter.W, padx = 10)
tkinter.Label(canvas.keyFrame, text = "        y = y coordinate of dot").grid(column = 0, row = 2, sticky = tkinter.W, padx = 10)

# Displays any errors that may occur in the program
canvas.errorFrame = tkinter.Frame(master, height = 1, width = 1, relief = RIDGE, borderwidth = 5)
canvas.errorFrame.grid(column = 0, row = 9, sticky = tkinter.W + tkinter.E, rowspan = 10)
canvas.errorMessage = tkinter.Label(canvas.errorFrame, text = 'No Errors')
canvas.errorMessage.grid(column = 0, row = 0)


# Main function that handles the animation
def phyllotaxis_animate():
    # Declare global variables
    global stop
    global mainColor
    
    # Make sure the canvas is reset every time the ANIMATE button is pressed
    canvas.delete("all")
    canvas.errorMessage.config(text = "No Errors")   
    
    angle = None
    
    # Get all of the necessary variables in order to manipulate HSV values
    # mylistbox.get(mylistbox.curselection())
    # Hue Values
    h1 = canvas.hueBox1.get(canvas.hueBox1.curselection())
    h2 = canvas.hueBox2.get(canvas.hueBox2.curselection())
    h3 = canvas.hueBox3.get(canvas.hueBox3.curselection())
    
    #Saturation values
    s1 = canvas.satBox1.get(canvas.satBox1.curselection())
    s2 = canvas.satBox2.get(canvas.satBox2.curselection())
    s3 = canvas.satBox3.get(canvas.satBox3.curselection())
    
    #Luminosity Values
    l1 = canvas.valBox1.get(canvas.valBox1.curselection())
    l2 = canvas.valBox2.get(canvas.valBox2.curselection())
    l3 = canvas.valBox3.get(canvas.valBox3.curselection())
    
    #Circle Density Value
    density = canvas.densityEntry.get()
    
    #Angle Value
    tempA = canvas.angleEntry.get()
    
    #Make sure angle value is acceptable
    try:
        angle = int(tempA)
    except:
        try:
            angle = float(tempA)
        except:
            if tempA != '-':
                canvas.errorMessage.config(text = "Given angle value is not a number, using default value")
            angle = 137.5
        
    if mainColor == None:
        if h1 != "None":
            if h2 != "None":
                if h3 != "None":
                    h = h1+h2+h3
            else:
                h = h1
        else:
            h = 1
    else:
        calc = colorsys.rgb_to_hsv(mainColor[0][0], mainColor[0][1], mainColor[0][2])
        fh = calc[0]
        h = None
        
    if s1 != "None":
        if s2 != "None":
            if s3 != "None":
                s = s1+s2+s3 
            else:
                s = s1
        else:
            s = s1
    else:
        s = 1
        
    if l1 != "None":
        if l2 != "None":
            if l3 != "None":
                l = l1+l2+l3
            else:
                l = l1
        else:
            l = l1
    else:
        l = 1
    
    n = 0
    c = int(density)
    
    stop = False
    
    while(not stop):
        a = n * angle
        r = c * math.sqrt(n)
    
        x = r * math.cos(a) + 200
        y = r * math.sin(a) + 200
        
        print(x, y)
        
        if((abs(x) >= 400 and abs(y) >= 400) or (abs(x) <= 0 and abs(y) <= 0)):
            break
        
        #Setup color values
        if h != 1 and mainColor == None:
            try:
                fh = (eval(h)%256)/256
            except:
                fh = 1
                canvas.errorMessage.config(text = "Hue: Division by zero, using default values")   
        elif mainColor == None:
            fh = h
        
        if s != 1:
            try:
                fs = (eval(s)%256)/256
            except:
                fs = 1
                canvas.errorMessage.config(text = "Saturation: Division by zero, using default values")        
        else:
            fs = s
            
        if l != 1:
            try:
                fl = (eval(l)%256)/256
            except:
                fl = 1
                canvas.errorMessage.config(text = "Luminosity: Division by zero, using default values")   
        else:
            fl = l
        
        color_transfer = colorsys.hsv_to_rgb(fh, fs, fl)
        color = "#%02x%02x%02x" % (color_transfer[0]*255, color_transfer[1]*255, color_transfer[2]*255)
        if mainColor == None:
            canvas.create_oval(x, y, x + 8, y + 8, fill = color, outline = color)
        else:
            canvas.create_oval(x, y, x + 8, y + 8, fill = color, outline = '#000000')
        n += 1
        
        canvas.update()

# Used for testing basic features
# def phyllotaxis_test():
#     n = 0
#     c = 4
#     while(True):
#         a = n * 137.5
#         r = c * math.sqrt(n)
# 
#         x = r * math.cos(a) + 200 
#         y = r * math.sin(a) + 200
#         
#         if(x >= 400 and y >= 400):
#             break
#         
#         color_transfer = colorsys.hsv_to_rgb(1, 1, 1)
#         color = "#%02x%02x%02x" % (color_transfer[0]*255, color_transfer[1]*255, color_transfer[2]*255)
#         outline = '#000000'
#         canvas.create_oval(x, y, x + 8, y + 8, fill =      
#                            color, outline = outline)
# 
#         n += 1
#         
#         #canvas.after(0)
#         canvas.update()

def stopAnim():
    global stop
    stop = True
    
def clearCanvas():
    global stop
    stop = True
    canvas.delete('all')

# Creates the button that starts the animation 
canvas.buttonFrame = tkinter.Frame(master, height = 1, width = 3)  
canvas.buttonFrame.grid(column = 0, row = 1)   
canvas.animate_button = tkinter.Button(canvas.buttonFrame, text = 'Animate', command = phyllotaxis_animate)
canvas.animate_button.grid(column = 0, row = 0)
canvas.stopButton = tkinter.Button(canvas.buttonFrame, text = 'Stop', command = stopAnim)
canvas.stopButton.grid(column = 1, row = 0)
canvas.clearButton = tkinter.Button(canvas.buttonFrame, text = 'Clear', command = clearCanvas)
canvas.clearButton.grid(column = 2, row = 0)


#phyllotaxis_animate()   
#master.after(500, phyllotaxis_animate()) 
canvas.mainloop()