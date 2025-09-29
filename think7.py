#Multiple Buttons with Different Actions
import tkinter as tk

#Create main window
root = tk.Tk()
root.title("Multiple Buttons with Actions")
root.geometry("400x300")

def say_yes():
    label.config(text="You clicked YES",fg="green")

def say_no():
    label.config(text="You clicked No", fg="red")

def reset():
    label.config(text="Click a butoon", fg="black")

label = tk.Label(root, text="Click a button", font=("Arial",14))
label.pack(pady=20)

#Buttons
yes_Button = tk.Button(root, text="YES", font=("Arial", 12),bg="lightgreen", command=say_yes)
yes_Button.pack(pady=5)

no_Button = tk.Button(root,text="NO", font=("Arial",12),bg="tomato", command=say_no)
no_Button.pack(pady=5)

reset_Button = tk.Button(root, text="RESET", font=("Arial",12),bg="lightblue", command=reset)
reset_Button.pack(pady=5)

root.mainloop()