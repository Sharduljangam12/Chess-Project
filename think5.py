#This step is very important because in bigger projects (like your Chess project)
# , you need to organize widgets properly. Tkinter gives us 3 layout managers:
import tkinter as tk

#create main window
root = tk.Tk()
root.title("Step 6 - Frames & layout management")
root.geometry("500x400")

#Using pack()
frame1 = tk.Frame(root, bg="lightblue",height=100)
frame1.pack(fill="x") #fill horizontally

label1 = tk.Label(frame1, text="This is packed at the TOP", bg="lightblue")
label1.pack(pady=10)

frame2 = tk.Frame(root, bg="lightgreen", height=100)
frame2.pack(fill="x", side="bottom") #stick at the bottom

label2 = tk.Label(frame2, text="This is packed at the BOTTOM", bg="lightgreen")
label2.pack(pady=10)

#using grid()
frame3 = tk.Frame(root, bg="lightyellow")
frame3.pack(fill="both",expand=True)

label3 = tk.Label(frame3, text="Row 0, Col 0", bg="orange", width=15)
label3.grid(row=0, column=0, padx=5, pady=5)

label4 = tk.Label(frame3, text="Row 0, Col 1", bg="pink", width=15)
label4.grid(row=0, column=1, padx=5, pady=5)

label5 = tk.Label(frame3, text="Row 1, Col 0", bg="lightblue", width=15)
label5.grid(row=1, column=0, padx=5, pady=5)

label6 = tk.Label(frame3, text="Row 1, Col 1", bg="lightgreen", width=15)
label6.grid(row=1, column=1, padx=5, pady=5)

#using place()
label7 = tk.Label(root, text="Placed at(200,300)", bg="red", fg="white")
label7.place(x=200, y=300) #absolute positioning 

#Strat the Tkinter event loop
root.mainloop()