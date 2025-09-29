#Tkinter Basics
import tkinter as tk

root = tk.Tk() #Create main window
root.title("My App")
root.geometry("400x300") #Width X Height 

root.mainloop() #keep window open 

'''
Key points
TK() -> main application window.
title() -> sets title bar text
geometry() -> sets size (string "widthxheight")
mainloop() -> keeps app running 
'''