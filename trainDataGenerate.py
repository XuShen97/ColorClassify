import tkinter as tk
import random


def addZero(aStr):
    if len(aStr) == 1:
        return '0' + aStr
    else:
        return aStr


# callback function definition

def updateColorString():
    global colorString
    r = addZero(str(hex(int(random.random() * 255)))[2:])
    g = addZero(str(hex(int(random.random() * 255)))[2:])
    b = addZero(str(hex(int(random.random() * 255)))[2:])
    colorString = '#' + r + g + b


def yClick():
    file.write(colorString + ' 1\n')
    global label
    global colorName
    updateColorString()
    label["background"] = colorString
    colorName["text"] = colorString


def nClick():
    file.write(colorString + ' 0\n')
    global label
    global colorName
    updateColorString()
    label["background"] = colorString
    colorName["text"] = colorString


# param init
colorString = "#bc9ef4"
file = open("trainData.txt", "w")
# Training window display
wnd = tk.Tk()
wnd.wm_title("Training...")
label = tk.Label(wnd, background=colorString, width=40, height=20)
label.pack()
colorName = tk.Label(wnd, background='white', text=colorString)
colorName.pack(fill='x')
buttonY = tk.Button(wnd, text="Like", command=yClick)
buttonY.pack(fill='x')
buttonN = tk.Button(wnd, text="Hate", command=nClick)
buttonN.pack(fill='x')
wnd.mainloop()
file.close()
