import tkinter as tk
import servoClass
import os
import time
arm = servoClass.Arm(servoClass.Servo(1, 0, 180), servoClass.Servo(2, 45, 135), servoClass.Servo(3, 0, 180), servoClass.Servo(4, 0, 180), servoClass.Servo(5, 0, 180))

armScriptsDirectory = "/home/anton/Programming/EPQ/src/armscripts"

def incrementString(string, increment):
    return str(int(string) + increment)

########## button calls ##########
def up():
    YEntry.set(incrementString(YEntry.get(), int(scaleEntry.get())))
def down():
    YEntry.set(incrementString(YEntry.get(), -int(scaleEntry.get())))
def left():
    XEntry.set(incrementString(XEntry.get(), -int(scaleEntry.get())))
def right():
    XEntry.set(incrementString(XEntry.get(), int(scaleEntry.get())))
def inward():
    ZEntry.set(incrementString(ZEntry.get(), int(scaleEntry.get())))
def out():
    ZEntry.set(incrementString(ZEntry.get(), -int(scaleEntry.get())))   
def go(): # moveTo FUNCTION
    x, y, z = XEntry.get(), YEntry.get(), ZEntry.get()
    stdout("moving to " + str((x, y, z)), 0)
    #print(console.get(1.0, tk.END))
    arm.moveArm(x, y, z)
    ###### WRITE CODE FOR MOVING ARM TO THESE COORDINATES
    
def ScaleUp():
    scaleEntry.set(incrementString(scaleEntry.get(), 1))
def ScaleDown():
    scaleEntry.set(incrementString(scaleEntry.get(), -1))

def reset():
    XEntry.set("0")
    YEntry.set("0")
    ZEntry.set("0")
    scaleEntry.set("1")

def moveTo(x, y, z):
    XEntry.set(x)
    YEntry.set(y)
    ZEntry.set(z)
    go()

def loadScript(name):
    stdout(f"loading script {name}", 0)

    with open(f"{armScriptsDirectory}/{name}.arm") as f:
        for line in f:
            #stdout(line, 0)
            parseCommand(*(line.strip("\n").split(" ")))
            

def listScripts():
    return os.listdir(armScriptsDirectory)



##########################



######### Console functions #########
entryChars = "> "
def clear():
    console.delete(1.0, tk.END)
    console.insert(tk.END, entryChars)

def getConsole(*args):
    #print(args)
    data = console.get(1.0, tk.END)
    #print(data)
    return data

def parseCommand(*args):
    print(args)
    command = args[0]
    cargs = args[1:]
    match command:
        case "x":
            XEntry.set(cargs[0])
        case "y":
            YEntry.set(cargs[0])
        case "z":
            ZEntry.set(cargs[0])
        case "scale":
            scaleEntry.set(cargs[0])
        case "up":
            up()
        case "down":
            down()
        case "left":
            left()
        case "right":
            right()
        case "in":
            inward()
        case "out":
            out()
        case "moveto":
            moveTo(*cargs)
        case "go":
            go()
        case "reset":
            reset()
        case "exit":
            main.quit()
        case "wait":
            stdout(f"Waiting {cargs[0]} seconds", 0)

            time.sleep(int(cargs[0]))
        case "clear":
            clear()
        case "load":
            loadScript(cargs[0])
        case "list":
            print(listScripts())
        case "help":
            print("Commands: up, down, left, right, in, out, moveTo, go, reset, exit, wait, clear, load, list, help")
        case _:
            print(f"Invalid command {command}")
        
        


def stdout(string, mode, *args):
    """Mode: 0 = stdout, 1 = stderr"""
    console.insert(tk.END, "\n")
    if mode == 0:
        console.insert(tk.END, string)
    elif mode == 1:
        console.insert(tk.END, string)
    else:
        raise ValueError("Invalid mode")
    console.mark_set("insert", tk.END)
    console.insert(tk.END, "\n"+entryChars)
    console.see(tk.END)


def stdin(*args): # called upon return key (enter)
    #print(getConsole())
    entry = "".join(getConsole()).split(entryChars)[-1].strip("\n")
    
    print(entry)
    entry = entry.split(" ")

    parseCommand(*entry)

    console.mark_set("insert", tk.END)
    #console.delete(1.0, tk.END)
    
    console.insert(tk.END, "\n"+entryChars)
    return "break"

def clear():
    ...



########## MAIN ##########

width = 800 # x
height = 600 # y
mWidth = width//2
mHeight = height//2

main = tk.Tk()
main.title("Antons Robotic Arm")
main.geometry(f"{width}x{height}")

main.config(bg="black", padx=10, pady=10, cursor="tcross")

title = tk.Label(main, text="Robotic Arm Controller", font=("Arial", 20))
title.pack(pady=10)


XEntry = tk.StringVar()
YEntry = tk.StringVar()
ZEntry = tk.StringVar()
scaleEntry = tk.StringVar()

menuBar = tk.Menu(main)
menuBar.add_command(label="Reset", command=reset)
menuBar.add_command(label="Quit", command=main.quit)
main.config(menu=menuBar)




buttonGrid = tk.Frame(main)
tk.Button(buttonGrid, text="inc+", width=4, height=2, command=ScaleUp).grid(row=0, column=0) 
tk.Button(buttonGrid, text="Go", width=4, height=2, command=go).grid(row=0, column=1) 
tk.Button(buttonGrid, text="in", width=4, height=2, command=inward).grid(row=0, column=2) 
tk.Button(buttonGrid, text="inc-", width=4, height=2, command=ScaleDown).grid(row=1, column=0) 
tk.Button(buttonGrid, text="^", width=4, height=2, command=up).grid(row=1, column=1) 
tk.Button(buttonGrid, text="out ", width=4, height=2, command=out).grid(row=1, column=2) 
tk.Button(buttonGrid, text="<", width=4, height=2, command=left).grid(row=2, column=0)
tk.Button(buttonGrid, text="v", width=4, height=2, command=down).grid(row=2, column=1) 
tk.Button(buttonGrid, text=">", width=4, height=2, command=right).grid(row=2, column=2)

# + x /
# - ^ / 
# < v >
buttonGrid.pack()

textGrid = tk.Frame(main)
XEntry.set("0")
YEntry.set("0")
ZEntry.set("0")
scaleEntry.set("1")
tk.Label(textGrid, text="X: ").grid(row=0, column=0)
tk.Label(textGrid, text="Y: ").grid(row=1, column=0)
tk.Label(textGrid, text="Z: ").grid(row=2, column=0)
tk.Label(textGrid, text="Scale: ").grid(row=3, column=0)
tk.Entry(textGrid, width=10, textvariable=XEntry).grid(row=0, column=1)
tk.Entry(textGrid, width=10, textvariable = YEntry).grid(row=1, column=1)
tk.Entry(textGrid, width=10, textvariable=ZEntry).grid(row=2, column=1)
tk.Entry(textGrid, width=10, textvariable=scaleEntry).grid(row=3, column=1)
textGrid.pack()

consoleGrid = tk.Frame(main)
console = tk.Text(consoleGrid, width=50, height=10)#, textvariable = "consoleText")
console.pack()
console.insert(1.0, entryChars)
consoleGrid.pack()

console.bind("<Return>", stdin)
console



main.mainloop()