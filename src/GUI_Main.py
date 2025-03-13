import tkinter as tk




width = 800 # x
height = 600 # y
mWidth = width//2
mHeight = height//2

main = tk.Tk()
main.title("Antons Robotic Arm")
main.geometry(f"{width}x{height}")

title = tk.Label(main, text="MAIN TITLE")
title.pack(pady=10)



buttonGrid = tk.Frame(main)
tk.Button(buttonGrid, text="-", width=4, height=2).grid(row=0, column=0)
tk.Button(buttonGrid, text="^").grid(row=0, column=1)
tk.Button(buttonGrid, text="-").grid(row=0, column=2)
tk.Button(buttonGrid, text="<").grid(row=1, column=0)
tk.Button(buttonGrid, text="x").grid(row=1, column=1)
tk.Button(buttonGrid, text=">").grid(row=1, column=2)
tk.Button(buttonGrid, text="-").grid(row=2, column=0)
tk.Button(buttonGrid, text="v").grid(row=2, column=1)
tk.Button(buttonGrid, text="-").grid(row=2, column=2)
buttonGrid.pack()





main.mainloop()