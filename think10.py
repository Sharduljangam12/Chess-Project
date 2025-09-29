#Code of how to create menus like file-> open, Help-> About 
import tkinter as tk
from tkinter import messagebox

#Create main window
root = tk.Tk()
root.title("Menus Example")
root.geometry("400x300")

#Functionf or menu actions
def say_hello():
    messagebox.showinfo("hello","Hello from the Menu!")

def quit_app():
    root.quit()

#Create menu bar
menu_bar = tk.Menu(root)

#File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Say Hello", command=say_hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

#Help menu 
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "This is a Tkinter app"))
menu_bar.add_cascade(label="Help", menu=help_menu)

#Attach the menu bar to the window 
root.config(menu=menu_bar)

root.mainloop()