#How to add image to a web page in tkinter
from tkinter import PhotoImage
img = PhotoImage(file="image.png")
label = tk.Label(root,image=img)
label.pack()