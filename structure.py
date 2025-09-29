#Create a GUI window using Tkinter that displays a proper 8x8 chessboard grid with alternating colors (light and dark squares), just like a real board.
'''import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Chess")
current_player = "White"  # Game always starts with player X

# 3x3 board represented by buttons
buttons = [[None for _ in range(8)] for _ in range(8)]

# Function to handle button click
def on_click(row, col):
    global current_player

    # If the button is already used, ignore click
    if buttons[row][col]["text"] != "":
        return

    # Update the button with current player's symbol
    buttons[row][col]["text"] = current_player
    buttons[row][col]["state"] = "disabled"


# Disable all buttons when game is over
def disable_all_buttons():
    for i in range(8):
        for j in range(8):
            buttons[i][j]["state"] = "disabled"

# Reset the game board
def reset_board():
    global current_player
    current_player = "White"
    for i in range(8):
        for j in range(8):
            buttons[i][j]["text"] = ""
            buttons[i][j]["state"] = "normal"

# Create the grid of buttons using nested loop
for i in range(8):
    for j in range(8):
        color = "white" if (i + j) % 2 == 0 else "black"
        text_color = "black" if color == "white" else "white"

        buttons[i][j] = tk.Button(
            window,
            text="",
            font=("Helvetica", 24),
            width=5,
            height=2,
            bg=color,                      # Checkerboard background
            fg=text_color,                # Text contrast
            activebackground=color,       # Keep color on click
            disabledforeground=text_color,
            command=lambda r=i, c=j: on_click(r, c)
        )
        buttons[i][j].grid(row=i, column=j)


# Add Reset Button
restart_button = tk.Button(window, text="Restart", font=("Helvetica", 14), command=reset_board)
restart_button.grid(row=8, column=0, columnspan=8)

# Start the GUI event loop
window.mainloop()
'''
'''🎯 Task: Create the Chessboard Layout
Import Tkinter.
Create a main window (Tk).
Use a Canvas (or grid of Labels/Frames) to draw an 8×8 chessboard.
Alternate black and white squares.
Hints: Use nested loops (row, column). Each square can be 50×50 px (so the full board = 400×400 px).
Color logic:
if (row + col) % 2 == 0:
    color = "white"
else:
    color = "black"
Expected Output: A Tkinter window showing an 8×8 chessboard with alternating black and white squares.'''
import tkinter as tk

root = tk.Tk()
root.title("Chess Board")

# Create a canvas (400x400 = 50px * 8)
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Draw 8x8 squares
square_size = 50
for row in range(8):
    for col in range(8):
        x1 = col * square_size
        y1 = row * square_size
        x2 = x1 + square_size
        y2 = y1 + square_size

        color = "white" if (row + col) % 2 == 0 else "black"
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

root.mainloop()