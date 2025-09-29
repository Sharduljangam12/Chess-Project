#Basic Fram Usage 
import tkinter as tk

#Create main window
root = tk.Tk()
root.title("Framse Basics")
root.geometry("500x400")

#Top fram(for title or info )
top_frame = tk.Frame(root, bg="lightblue", height=100)
top_frame.pack(fill="x")

#Bottom Fram(for buttons)
bottom_frame = tk.Frame(root, bg="lightgray", height=100)
bottom_frame.pack(side="bottom", fill="x")

#Add widgets inside frames
title_label = tk.Label(top_frame, text="welcome to Tkinter Frames!", font=("Arial",16), bg="lightblue")
title_label.pack(pady=20)

btn1 = tk.Button(bottom_frame, text="Button 1")
btn1.pack(side="left",padx=20, pady=20)

btn2 = tk.Button(bottom_frame, text="Butoon 2")
btn2.pack(side="right",padx=20, pady=20)

root.mainloop()