import tkinter as tk


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
def x(): # HOMING FUNCTION
    print(XEntry.get(), YEntry.get(), ZEntry.get(), scaleEntry.get())

def ScaleUp():
    scaleEntry.set(incrementString(scaleEntry.get(), 1))
def ScaleDown():
    scaleEntry.set(incrementString(scaleEntry.get(), -1))


########## MAIN ##########

width = 800 # x
height = 600 # y
mWidth = width//2
mHeight = height//2

main = tk.Tk()
main.title("Antons Robotic Arm")
main.geometry(f"{width}x{height}")

main.config(bg="black", padx=10, pady=10, cursor="tcross")

title = tk.Label(main, text="MAIN TITLE")
title.pack(pady=10)


XEntry = tk.StringVar()
YEntry = tk.StringVar()
ZEntry = tk.StringVar()
scaleEntry = tk.StringVar()

buttonGrid = tk.Frame(main)
tk.Button(buttonGrid, text="+", width=4, height=2, command=ScaleUp).grid(row=0, column=0) 
tk.Button(buttonGrid, text="X", width=4, height=2, command=x).grid(row=0, column=1) 
tk.Button(buttonGrid, text="/", width=4, height=2, command=inward).grid(row=0, column=2) 
tk.Button(buttonGrid, text="-", width=4, height=2, command=ScaleDown).grid(row=1, column=0) 
tk.Button(buttonGrid, text="^", width=4, height=2, command=up).grid(row=1, column=1) 
tk.Button(buttonGrid, text="\\", width=4, height=2, command=out).grid(row=1, column=2) 
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


main.mainloop()