#This is Widgets (UI elements) we will learn to add buttons, labels and inputs 
import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="hello Tkinter!", font=("Arial",16))
label.pack()

entry = tk.Entry(root, width=20)
entry.pack()

button = tk.Button(root, text="Click Me", command=lambda: print(entry.get()))
button.pack()

root.mainloop()
#Below is the code given by gpt for learn how to add text, buttons, and input fields.
'''
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Step 3 - Widgets Example")
root.geometry("400x300")

# Label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=10)

# Entry field
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Button click function
def on_button_click():
    user_input = entry.get()
    label.config(text=f"You typed: {user_input}")

# Button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Run the application
root.mainloop()
'''

'''
Comman -> Widgets
label -> display text/images
Entry -> single-line text input
Text->  multi-line input
Button -> clickable button
Frame -> conatiner for other widgets 
'''