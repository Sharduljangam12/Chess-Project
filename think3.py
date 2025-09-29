#images and Canvas
#Shwo images and draw shapes (important for chess board)
#Tkinter can display images using PhotoImage (supports .png and .gif by default).
'''from tkinter import Tk, Canvas

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()

#Draw shapes 
canvas.create_rectangle(50, 50, 150, 150, fill="blue")


root.mainloop()'''

'''import tkinter as tk

#Create the main window
root = tk.Tk()
root.title("Step 4 - Adding Images")
root.geometry("400x400")

#Load an image(must be PNG or GIF)
img = tk.PhotoImage(file="webpic.png") 

#Create label with image 
image_label = tk.Label(root, image=image)
image_label.pack(pady=10)

#Add text label below iamge
text_label = tk.Label(root, text="This is an image in Tkinter", font=("Arial",14))
text_label.pack(pady=10)

#Start the Tkinter event loop
root.mainloop()'''
import tkinter as tk
import os

root = tk.Tk()
root.title("Step 4 - Adding Images")
root.geometry("400x400")

# Absolute path
img_path = r"C:\Users\student\Desktop\Shardul\Python\Chess_Project\webpic.png"
img = tk.PhotoImage(file=img_path)

image_label = tk.Label(root, image=img)
image_label.pack(pady=10)

text_label = tk.Label(root, text="This is an image in Tkinter", font=("Arial",14))
text_label.pack(pady=10)

root.mainloop()
