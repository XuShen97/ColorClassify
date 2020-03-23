import tkinter as tk


def addZero(aStr):
    if len(aStr) == 1:
        return '0' + aStr
    else:
        return aStr


# callback function definition

def onClick():
    global index
    global eleNum
    global colorString
    index += 1
    if index > eleNum:
        index -= eleNum
    colorString = colors[index - 1]
    label["background"] = colorString
    colorName["text"] = str(index) + " " + colorString + (' Like' if int(results[index - 1]) == 1 else ' Unlike')


# param init
colorString = "#ffffff"
colors = []
results = []
index = 0
eleNum = 0
for aLine in open("testResult.txt", "r"):
    colors.append(aLine[0:7])
    results.append(aLine[8:9])
    eleNum += 1
wnd = tk.Tk()
wnd.wm_title("Test Result")
label = tk.Label(wnd, background=colorString, width=40, height=20)
label.pack()
colorName = tk.Label(wnd, background='white', text="Click to start")
colorName.pack(fill='x')
buttonNext = tk.Button(wnd, text="Next", command=onClick)
buttonNext.pack(fill='x')
wnd.mainloop()
