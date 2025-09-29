#Code for Buttons + events (how to click & trigger actions) event handling when it's clicked 
import tkinter as tk

#Create the main window 
root = tk.Tk()
root.title("Buttons ans Events")
root.geometry("400x300")

#Function to run when button is clicked 
def on_dutton_click():
    label.config(text="Button was clicked !", fg="greeen")

label = tk.Label(root, text="Click the button below", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root,text="Click Me!", font=("Arial", 12), bg="lightblue", command=on_dutton_click)
button.pack(pady=10)

#Start Tkinter event loop
root.mainloop()