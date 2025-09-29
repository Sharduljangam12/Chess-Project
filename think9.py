# Code for grid like layout

import tkinter as tk

root = tk.Tk()
root.title("Nested Frames Example")
root.geometry("600x400")

#Main Layout: Left Frame (Chessboard), Right Frame(controls)
left_frame = tk.Frame(root, bg="white", width=400, height=400)
left_frame.pack(side="left", fill="both", expand=True)

right_frame = tk.Frame(root, bg="lightgray", width=200)
right_frame.pack(side="right", fill="y")

#Inside Left Fram -> Add Chessboard Placeholder 
board_label = tk.Label(left_frame, text="Chessboard Area", bg="white", font=("Arial",14))
board_label.pack(expand=True)

#Inside Right frame -> Add Buttons
btn_new = tk.Button(right_frame, text="New Game")
btn_new.pack(pady=10)

btn_exit = tk.Button(left_frame, text="Exit", command=root.quit)
btn_exit.pack(pady=10)

root.mainloop()