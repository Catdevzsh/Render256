import tkinter as tk
from tkinter import ttk

def draw_gradient(canvas, width, height, color1, color2):
    """Draw a gradient from color1 to color2 on the canvas."""
    for i in range(height):
        r = int(color1[1:3], 16) + (int(color2[1:3], 16) - int(color1[1:3], 16)) * i // height
        g = int(color1[3:5], 16) + (int(color2[3:5], 16) - int(color1[3:5], 16)) * i // height
        b = int(color1[5:7], 16) + (int(color2[5:7], 16) - int(color1[5:7], 16)) * i // height
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, width, i, fill=color)

# ASCII Art of 1-Up Mushroom
mushroom_art = """
      @@@@
     @@@@@@
     @@@@@@
      @@@@
   @@@@@@@@@@
  @@@@@@@@@@@@
 @@@@@@@@@@@@@@
@@@@@@@@@@@@@@@
  @@@@@@@@@@@@
   @@@@@@@@@@
    @@@@@@@@
     @@@@@@
      @@@@
"""

# Create the Tkinter application
root = tk.Tk()
root.title('B3313 2.0 GAME PERSONLIZATION TEST AUGEMENTER 0.1')
root.geometry('800x600')
root.resizable(False, False)

# Create the Canvas for gradient
canvas = tk.Canvas(root, height=600)
canvas.pack(fill='both', expand=True)

# Draw the gradient on the Canvas
draw_gradient(canvas, 800, 600, '#87CEEB', '#FFFFFF')

# Create a frame for the label and ASCII Art
main_frame = tk.Frame(canvas, bg="#87CEEB")  # Use a matching background color
main_frame.place(relx=0.5, rely=0.3, anchor='center')

# Add the label using standard tk.Label
label = tk.Label(main_frame, text='NOW ONLINE', fg='white', font=('Arial', 18, 'bold'), bg="#87CEEB")
label.pack(pady=20)

# Add the ASCII Art
ascii_label = tk.Label(main_frame, text=mushroom_art, font=('Courier', 12), fg='green', bg="#87CEEB")
ascii_label.pack()

# Create buttons
button_frame = tk.Frame(canvas, bg="#87CEEB")
button_frame.place(relx=0.5, rely=0.8, anchor='center')
for i in range(1, 6):
    tk.Button(button_frame, text=f'Button {i}', command=lambda i=i: print(f"Button {i} clicked"), bg="#87CEEB").pack(side='left', padx=10)

# Run the Tkinter event loop
root.mainloop()
