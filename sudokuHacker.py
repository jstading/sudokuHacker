import tkinter as tk
from tkinter import IntVar, Tk, Canvas, Frame, BOTH, ttk

class sudokuGrid(Frame):
    
    def __init__(self):
        super().__init__()

        self.master.title("!!!Sudoku Hacker!!!")
        self.pack(fill=BOTH, expand=1)

        def draw_grid(self):
            i1j1_var = tk.IntVar(); i1j1_var = tk.IntVar(); i1j2_var = tk.IntVar(); i1j3_var = tk.IntVar(); i1j4_var = tk.IntVar(); i1j5_var = tk.IntVar()
            i1j6_var = tk.IntVar(); i1j7_var = tk.IntVar(); i1j8_var = tk.IntVar(); i1j9_var = tk.IntVar(); i2j1_var = tk.IntVar(); i2j2_var = tk.IntVar()
            i2j3_var = tk.IntVar(); i2j4_var = tk.IntVar(); i2j5_var = tk.IntVar(); i2j6_var = tk.IntVar(); i2j7_var = tk.IntVar(); i2j8_var = tk.IntVar()
            i2j9_var = tk.IntVar(); i3j1_var = tk.IntVar(); i3j2_var = tk.IntVar(); i3j3_var = tk.IntVar(); i3j4_var = tk.IntVar(); i3j5_var = tk.IntVar()
            i3j6_var = tk.IntVar(); i3j7_var = tk.IntVar(); i3j8_var = tk.IntVar(); i3j9_var = tk.IntVar(); i4j1_var = tk.IntVar(); i4j2_var = tk.IntVar()
            i4j3_var = tk.IntVar(); i4j4_var = tk.IntVar(); i4j5_var = tk.IntVar(); i4j6_var = tk.IntVar(); i4j7_var = tk.IntVar(); i4j8_var = tk.IntVar()
            i4j9_var = tk.IntVar(); i5j1_var = tk.IntVar(); i5j2_var = tk.IntVar(); i5j3_var = tk.IntVar(); i5j4_var = tk.IntVar(); i5j5_var = tk.IntVar()
            i5j6_var = tk.IntVar(); i5j7_var = tk.IntVar(); i5j8_var = tk.IntVar(); i5j9_var = tk.IntVar(); i6j1_var = tk.IntVar(); i6j2_var = tk.IntVar()
            i6j3_var = tk.IntVar(); i6j4_var = tk.IntVar(); i6j5_var = tk.IntVar(); i6j6_var = tk.IntVar(); i6j7_var = tk.IntVar(); i6j8_var = tk.IntVar()
            i6j9_var = tk.IntVar(); i7j1_var = tk.IntVar(); i7j2_var = tk.IntVar(); i7j3_var = tk.IntVar(); i7j4_var = tk.IntVar(); i7j5_var = tk.IntVar()
            i7j6_var = tk.IntVar(); i7j7_var = tk.IntVar(); i7j8_var = tk.IntVar(); i7j9_var = tk.IntVar(); i8j1_var = tk.IntVar(); i8j2_var = tk.IntVar()
            i8j3_var = tk.IntVar(); i8j4_var = tk.IntVar(); i8j5_var = tk.IntVar(); i8j6_var = tk.IntVar(); i8j7_var = tk.IntVar(); i8j8_var = tk.IntVar()
            i8j9_var = tk.IntVar(); i9j1_var = tk.IntVar(); i9j2_var = tk.IntVar(); i9j3_var = tk.IntVar(); i9j4_var = tk.IntVar(); i9j5_var = tk.IntVar()
            i9j6_var = tk.IntVar(); i9j7_var = tk.IntVar(); i9j8_var = tk.IntVar(); i9j9_var = tk.IntVar()

            canvas = Canvas(self)
            canvas.create_line(15, 25, 285, 25, width = 5)
            canvas.create_line(15, 55, 285, 55)
            canvas.create_line(15, 85, 285, 85)
            canvas.create_line(15, 115, 285, 115, width = 5)
            canvas.create_line(15, 145, 285, 145)
            canvas.create_line(15, 175, 285, 175)
            canvas.create_line(15, 205, 285, 205, width = 5)
            canvas.create_line(15, 235, 285, 235)
            canvas.create_line(15, 265, 285, 265)
            canvas.create_line(15, 295, 285, 295, width = 5)

            canvas.create_line(15, 25, 15, 295, width = 5)
            canvas.create_line(45, 25, 45, 295)
            canvas.create_line(75, 25, 75, 295)
            canvas.create_line(105, 25, 105, 295, width = 5)
            canvas.create_line(135, 25, 135, 295)
            canvas.create_line(165, 25, 165, 295)
            canvas.create_line(195, 25, 195, 295, width = 5)
            canvas.create_line(225, 25, 225, 295)
            canvas.create_line(255, 25, 255, 295)
            canvas.create_line(285, 25, 285, 295, width = 5)
            canvas.pack(fill=BOTH, expand=1)

            i1j1_entry = tk.Entry(root, textvariable=i1j1_var)
            canvas.create_window(30, 40, width = 20, height = 20,  window=i1j1_entry)
            i1j2_entry = tk.Entry(root, textvariable=i1j2_var)
            canvas.create_window(60, 40, width = 20, height = 20,  window=i1j2_entry)
            i1j3_entry = tk.Entry(root, textvariable=i1j3_var)
            canvas.create_window(90, 40, width = 20, height = 20,  window=i1j3_entry)
            i1j4_entry = tk.Entry(root, textvariable=i1j4_var)
            canvas.create_window(120, 40, width = 20, height = 20,  window=i1j4_entry)
            i1j5_entry = tk.Entry(root, textvariable=i1j5_var)
            canvas.create_window(150, 40, width = 20, height = 20,  window=i1j5_entry)
            i1j6_entry = tk.Entry(root, textvariable=i1j6_var)
            canvas.create_window(180, 40, width = 20, height = 20,  window=i1j6_entry)
            i1j7_entry = tk.Entry(root, textvariable=i1j7_var)
            canvas.create_window(210, 40, width = 20, height = 20,  window=i1j7_entry)
            i1j8_entry = tk.Entry(root, textvariable=i1j8_var)
            canvas.create_window(240, 40, width = 20, height = 20,  window=i1j8_entry)
            i1j9_entry = tk.Entry(root, textvariable=i1j9_var)
            canvas.create_window(270, 40, width = 20, height = 20,  window=i1j9_entry)

            i2j1_entry = tk.Entry(root, textvariable=i2j1_var)
            canvas.create_window(30, 70, width=20, height=20, window=i2j1_entry)
            i2j2_entry = tk.Entry(root, textvariable=i2j2_var)
            canvas.create_window(60, 70, width=20, height=20, window=i2j2_entry)
            i2j3_entry = tk.Entry(root, textvariable=i2j3_var)
            canvas.create_window(90, 70, width=20, height=20, window=i2j3_entry)
            i2j4_entry = tk.Entry(root, textvariable=i2j4_var)
            canvas.create_window(120, 70, width=20, height=20, window=i2j4_entry)
            i2j5_entry = tk.Entry(root, textvariable=i2j5_var)
            canvas.create_window(150, 70, width=20, height=20, window=i2j5_entry)
            i2j6_entry = tk.Entry(root, textvariable=i2j6_var)
            canvas.create_window(180, 70, width=20, height=20, window=i2j6_entry)
            i2j7_entry = tk.Entry(root, textvariable=i2j7_var)
            canvas.create_window(210, 70, width=20, height=20, window=i2j7_entry)
            i2j8_entry = tk.Entry(root, textvariable=i2j8_var)
            canvas.create_window(240, 70, width=20, height=20, window=i2j8_entry)
            i2j9_entry = tk.Entry(root, textvariable=i2j9_var)
            canvas.create_window(270, 70, width=20, height=20, window=i2j9_entry)

            i3j1_entry = tk.Entry(root, textvariable=i3j1_var)
            canvas.create_window(30, 100, width=20, height=20, window=i3j1_entry)
            i3j2_entry = tk.Entry(root, textvariable=i3j2_var)
            canvas.create_window(60, 100, width=20, height=20, window=i3j2_entry)
            i3j3_entry = tk.Entry(root, textvariable=i3j3_var)
            canvas.create_window(90, 100, width=20, height=20, window=i3j3_entry)
            i3j4_entry = tk.Entry(root, textvariable=i3j4_var)
            canvas.create_window(120, 100, width=20, height=20, window=i3j4_entry)
            i3j5_entry = tk.Entry(root, textvariable=i3j5_var)
            canvas.create_window(150, 100, width=20, height=20, window=i3j5_entry)
            i3j6_entry = tk.Entry(root, textvariable=i3j6_var)
            canvas.create_window(180, 100, width=20, height=20, window=i3j6_entry)
            i3j7_entry = tk.Entry(root, textvariable=i3j7_var)
            canvas.create_window(210, 100, width=20, height=20, window=i3j7_entry)
            i3j8_entry = tk.Entry(root, textvariable=i3j8_var)
            canvas.create_window(240, 100, width=20, height=20, window=i3j8_entry)
            i3j9_entry = tk.Entry(root, textvariable=i3j9_var)
            canvas.create_window(270, 100, width=20, height=20, window=i3j9_entry)

            i4j1_entry = tk.Entry(root, textvariable=i4j1_var)
            canvas.create_window(30, 130, width=20, height=20, window=i4j1_entry)
            i4j2_entry = tk.Entry(root, textvariable=i4j2_var)
            canvas.create_window(60, 130, width=20, height=20, window=i4j2_entry)
            i4j3_entry = tk.Entry(root, textvariable=i4j3_var)
            canvas.create_window(90, 130, width=20, height=20, window=i4j3_entry)
            i4j4_entry = tk.Entry(root, textvariable=i4j4_var)
            canvas.create_window(120, 130, width=20, height=20, window=i4j4_entry)
            i4j5_entry = tk.Entry(root, textvariable=i4j5_var)
            canvas.create_window(150, 130, width=20, height=20, window=i4j5_entry)
            i4j6_entry = tk.Entry(root, textvariable=i4j6_var)
            canvas.create_window(180, 130, width=20, height=20, window=i4j6_entry)
            i4j7_entry = tk.Entry(root, textvariable=i4j7_var)
            canvas.create_window(210, 130, width=20, height=20, window=i4j7_entry)
            i4j8_entry = tk.Entry(root, textvariable=i4j8_var)
            canvas.create_window(240, 130, width=20, height=20, window=i4j8_entry)
            i4j9_entry = tk.Entry(root, textvariable=i4j9_var)
            canvas.create_window(270, 130, width=20, height=20, window=i4j9_entry)

            i5j1_entry = tk.Entry(root, textvariable=i5j1_var)
            canvas.create_window(30, 160, width=20, height=20, window=i5j1_entry)
            i5j2_entry = tk.Entry(root, textvariable=i5j2_var)
            canvas.create_window(60, 160, width=20, height=20, window=i5j2_entry)
            i5j3_entry = tk.Entry(root, textvariable=i5j3_var)
            canvas.create_window(90, 160, width=20, height=20, window=i5j3_entry)
            i5j4_entry = tk.Entry(root, textvariable=i5j4_var)
            canvas.create_window(120, 160, width=20, height=20, window=i5j4_entry)
            i5j5_entry = tk.Entry(root, textvariable=i5j5_var)
            canvas.create_window(150, 160, width=20, height=20, window=i5j5_entry)
            i5j6_entry = tk.Entry(root, textvariable=i5j6_var)
            canvas.create_window(180, 160, width=20, height=20, window=i5j6_entry)
            i5j7_entry = tk.Entry(root, textvariable=i5j7_var)
            canvas.create_window(210, 160, width=20, height=20, window=i5j7_entry)
            i5j8_entry = tk.Entry(root, textvariable=i5j8_var)
            canvas.create_window(240, 160, width=20, height=20, window=i5j8_entry)
            i5j9_entry = tk.Entry(root, textvariable=i5j9_var)
            canvas.create_window(270, 160, width=20, height=20, window=i5j9_entry)

            i6j1_entry = tk.Entry(root, textvariable=i6j1_var)
            canvas.create_window(30, 190, width=20, height=20, window=i6j1_entry)
            i6j2_entry = tk.Entry(root, textvariable=i6j2_var)
            canvas.create_window(60, 190, width=20, height=20, window=i6j2_entry)
            i6j3_entry = tk.Entry(root, textvariable=i6j3_var)
            canvas.create_window(90, 190, width=20, height=20, window=i6j3_entry)
            i6j4_entry = tk.Entry(root, textvariable=i6j4_var)
            canvas.create_window(120, 190, width=20, height=20, window=i6j4_entry)
            i6j5_entry = tk.Entry(root, textvariable=i6j5_var)
            canvas.create_window(150, 190, width=20, height=20, window=i6j5_entry)
            i6j6_entry = tk.Entry(root, textvariable=i6j6_var)
            canvas.create_window(180, 190, width=20, height=20, window=i6j6_entry)
            i6j7_entry = tk.Entry(root, textvariable=i6j7_var)
            canvas.create_window(210, 190, width=20, height=20, window=i6j7_entry)
            i6j8_entry = tk.Entry(root, textvariable=i6j8_var)
            canvas.create_window(240, 190, width=20, height=20, window=i6j8_entry)
            i6j9_entry = tk.Entry(root, textvariable=i6j9_var)
            canvas.create_window(270, 190, width=20, height=20, window=i6j9_entry)

            i7j1_entry = tk.Entry(root, textvariable=i7j1_var)
            canvas.create_window(30, 220, width=20, height=20, window=i7j1_entry)
            i7j2_entry = tk.Entry(root, textvariable=i7j2_var)
            canvas.create_window(60, 220, width=20, height=20, window=i7j2_entry)
            i7j3_entry = tk.Entry(root, textvariable=i7j3_var)
            canvas.create_window(90, 220, width=20, height=20, window=i7j3_entry)
            i7j4_entry = tk.Entry(root, textvariable=i7j4_var)
            canvas.create_window(120, 220, width=20, height=20, window=i7j4_entry)
            i7j5_entry = tk.Entry(root, textvariable=i7j5_var)
            canvas.create_window(150, 220, width=20, height=20, window=i7j5_entry)
            i7j6_entry = tk.Entry(root, textvariable=i7j6_var)
            canvas.create_window(180, 220, width=20, height=20, window=i7j6_entry)
            i7j7_entry = tk.Entry(root, textvariable=i7j7_var)
            canvas.create_window(210, 220, width=20, height=20, window=i7j7_entry)
            i7j8_entry = tk.Entry(root, textvariable=i7j8_var)
            canvas.create_window(240, 220, width=20, height=20, window=i7j8_entry)
            i7j9_entry = tk.Entry(root, textvariable=i7j9_var)
            canvas.create_window(270, 220, width=20, height=20, window=i7j9_entry)

            i8j1_entry = tk.Entry(root, textvariable=i8j1_var)
            canvas.create_window(30, 250, width=20, height=20, window=i8j1_entry)
            i8j2_entry = tk.Entry(root, textvariable=i8j2_var)
            canvas.create_window(60, 250, width=20, height=20, window=i8j2_entry)
            i8j3_entry = tk.Entry(root, textvariable=i8j3_var)
            canvas.create_window(90, 250, width=20, height=20, window=i8j3_entry)
            i8j4_entry = tk.Entry(root, textvariable=i8j4_var)
            canvas.create_window(120, 250, width=20, height=20, window=i8j4_entry)
            i8j5_entry = tk.Entry(root, textvariable=i8j5_var)
            canvas.create_window(150, 250, width=20, height=20, window=i8j5_entry)
            i8j6_entry = tk.Entry(root, textvariable=i8j6_var)
            canvas.create_window(180, 250, width=20, height=20, window=i8j6_entry)
            i8j7_entry = tk.Entry(root, textvariable=i8j7_var)
            canvas.create_window(210, 250, width=20, height=20, window=i8j7_entry)
            i8j8_entry = tk.Entry(root, textvariable=i8j8_var)
            canvas.create_window(240, 250, width=20, height=20, window=i8j8_entry)
            i8j9_entry = tk.Entry(root, textvariable=i8j9_var)
            canvas.create_window(270, 250, width=20, height=20, window=i8j9_entry)

            i9j1_entry = tk.Entry(root, textvariable=i9j1_var)
            canvas.create_window(30, 280, width=20, height=20, window=i9j1_entry)
            i9j2_entry = tk.Entry(root, textvariable=i9j2_var)
            canvas.create_window(60, 280, width=20, height=20, window=i9j2_entry)
            i9j3_entry = tk.Entry(root, textvariable=i9j3_var)
            canvas.create_window(90, 280, width=20, height=20, window=i9j3_entry)
            i9j4_entry = tk.Entry(root, textvariable=i9j4_var)
            canvas.create_window(120, 280, width=20, height=20, window=i9j4_entry)
            i9j5_entry = tk.Entry(root, textvariable=i9j5_var)
            canvas.create_window(150, 280, width=20, height=20, window=i9j5_entry)
            i9j6_entry = tk.Entry(root, textvariable=i9j6_var)
            canvas.create_window(180, 280, width=20, height=20, window=i9j6_entry)
            i9j7_entry = tk.Entry(root, textvariable=i9j7_var)
            canvas.create_window(210, 280, width=20, height=20, window=i9j7_entry)
            i9j8_entry = tk.Entry(root, textvariable=i9j8_var)
            canvas.create_window(240, 280, width=20, height=20, window=i9j8_entry)
            i9j9_entry = tk.Entry(root, textvariable=i9j9_var)
            canvas.create_window(270, 280, width=20, height=20, window=i9j9_entry)

            solve_button = ttk.Button(root, text = "Solve", command=lambda: solve(self, 
            i1j1_var, i1j2_var, i1j3_var, i1j4_var, i1j5_var, i1j6_var, i1j7_var, i1j8_var, i1j9_var,
            i2j1_var, i2j2_var, i2j3_var, i2j4_var, i2j5_var, i2j6_var, i2j7_var, i2j8_var, i2j9_var,
            i3j1_var, i3j2_var, i3j3_var, i3j4_var, i3j5_var, i3j6_var, i3j7_var, i3j8_var, i3j9_var,
            i4j1_var, i4j2_var, i4j3_var, i4j4_var, i4j5_var, i4j6_var, i4j7_var, i4j8_var, i4j9_var,
            i5j1_var, i5j2_var, i5j3_var, i5j4_var, i5j5_var, i5j6_var, i5j7_var, i5j8_var, i5j9_var,
            i6j1_var, i6j2_var, i6j3_var, i6j4_var, i6j5_var, i6j6_var, i6j7_var, i6j8_var, i6j9_var,
            i7j1_var, i7j2_var, i7j3_var, i7j4_var, i7j5_var, i7j6_var, i7j7_var, i7j8_var, i7j9_var,
            i8j1_var, i8j2_var, i8j3_var, i8j4_var, i8j5_var, i8j6_var, i8j7_var, i8j8_var, i8j9_var,
            i9j1_var, i9j2_var, i9j3_var, i9j4_var, i9j5_var, i9j6_var, i9j7_var, i9j8_var, i9j9_var))
            solve_button.place(x= 305, y = 55)

            clear_button = ttk.Button(root, text="Clear", command=lambda: clear_grid(self))
            clear_button.place(x=305, y=145)

            quit_button = ttk.Button(root, text="Quit", command=lambda: root.quit())
            quit_button.place(x=305, y = 235)

        def solve(self, i1j1_var, i1j2_var, i1j3_var, i1j4_var, i1j5_var, i1j6_var, i1j7_var, i1j8_var, i1j9_var,
        i2j1_var, i2j2_var, i2j3_var, i2j4_var, i2j5_var, i2j6_var, i2j7_var, i2j8_var, i2j9_var,
        i3j1_var, i3j2_var, i3j3_var, i3j4_var, i3j5_var, i3j6_var, i3j7_var, i3j8_var, i3j9_var,
        i4j1_var, i4j2_var, i4j3_var, i4j4_var, i4j5_var, i4j6_var, i4j7_var, i4j8_var, i4j9_var,
        i5j1_var, i5j2_var, i5j3_var, i5j4_var, i5j5_var, i5j6_var, i5j7_var, i5j8_var, i5j9_var,
        i6j1_var, i6j2_var, i6j3_var, i6j4_var, i6j5_var, i6j6_var, i6j7_var, i6j8_var, i6j9_var,
        i7j1_var, i7j2_var, i7j3_var, i7j4_var, i7j5_var, i7j6_var, i7j7_var, i7j8_var, i7j9_var,
        i8j1_var, i8j2_var, i8j3_var, i8j4_var, i8j5_var, i8j6_var, i8j7_var, i8j8_var, i8j9_var,
        i9j1_var, i9j2_var, i9j3_var, i9j4_var, i9j5_var, i9j6_var, i9j7_var, i9j8_var, i9j9_var):
            
            i1j1 = i1j1_var.get(); i1j2 = i1j2_var.get(); i1j3 = i1j3_var.get(); i1j4 = i1j4_var.get(); i1j5 = i1j5_var.get(); i1j6 = i1j6_var.get()
            i1j7 = i1j7_var.get(); i1j8 = i1j8_var.get(); i1j9 = i1j9_var.get(); i2j1 = i2j1_var.get(); i2j2 = i2j2_var.get(); i2j3 = i2j3_var.get()
            i2j4 = i2j4_var.get(); i2j5 = i2j5_var.get(); i2j6 = i2j6_var.get(); i2j7 = i2j7_var.get(); i2j8 = i2j8_var.get(); i2j9 = i2j9_var.get()
            i3j1 = i3j1_var.get(); i3j2 = i3j2_var.get(); i3j3 = i3j3_var.get(); i3j4 = i3j4_var.get(); i3j5 = i3j5_var.get(); i3j6 = i3j6_var.get()
            i3j7 = i3j7_var.get(); i3j8 = i3j8_var.get(); i3j9 = i3j9_var.get(); i4j1 = i4j1_var.get(); i4j2 = i4j2_var.get(); i4j3 = i4j3_var.get()
            i4j4 = i4j4_var.get(); i4j5 = i4j5_var.get(); i4j6 = i4j6_var.get(); i4j7 = i4j7_var.get(); i4j8 = i4j8_var.get(); i4j9 = i4j9_var.get()
            i5j1 = i5j1_var.get(); i5j2 = i5j2_var.get(); i5j3 = i5j3_var.get(); i5j4 = i5j4_var.get(); i5j5 = i5j5_var.get(); i5j6 = i5j6_var.get()
            i5j7 = i5j7_var.get(); i5j8 = i5j8_var.get(); i5j9 = i5j9_var.get(); i6j1 = i6j1_var.get(); i6j2 = i6j2_var.get(); i6j3 = i6j3_var.get()
            i6j4 = i6j4_var.get(); i6j5 = i6j5_var.get(); i6j6 = i6j6_var.get(); i6j7 = i6j7_var.get(); i6j8 = i6j8_var.get(); i6j9 = i6j9_var.get()
            i7j1 = i7j1_var.get(); i7j2 = i7j2_var.get(); i7j3 = i7j3_var.get(); i7j4 = i7j4_var.get(); i7j5 = i7j5_var.get(); i7j6 = i7j6_var.get()
            i7j7 = i7j7_var.get(); i7j8 = i7j8_var.get(); i7j9 = i7j9_var.get(); i8j1 = i8j1_var.get(); i8j2 = i8j2_var.get(); i8j3 = i8j3_var.get()
            i8j4 = i8j4_var.get(); i8j5 = i8j5_var.get(); i8j6 = i8j6_var.get(); i8j7 = i8j7_var.get(); i8j8 = i8j8_var.get(); i8j9 = i8j9_var.get()
            i9j1 = i9j1_var.get(); i9j2 = i9j2_var.get(); i9j3 = i9j3_var.get(); i9j4 = i9j4_var.get(); i9j5 = i9j5_var.get(); i9j6 = i9j6_var.get()
            i9j7 = i9j7_var.get(); i9j8 = i9j8_var.get(); i9j9 = i9j9_var.get()

            row1 = [i1j1, i1j2, i1j3, i1j4, i1j5, i1j6, i1j7, i1j8, i1j9]
            row2 = [i2j1, i2j2, i2j3, i2j4, i2j5, i2j6, i2j7, i2j8, i2j9]
            row3 = [i3j1, i3j2, i3j3, i3j4, i3j5, i3j6, i3j7, i3j8, i3j9]
            row4 = [i4j1, i4j2, i4j3, i4j4, i4j5, i4j6, i4j7, i4j8, i4j9]
            row5 = [i5j1, i5j2, i5j3, i5j4, i5j5, i5j6, i5j7, i5j8, i5j9]
            row6 = [i6j1, i6j2, i6j3, i6j4, i6j5, i6j6, i6j7, i6j8, i6j9]
            row7 = [i7j1, i7j2, i7j3, i7j4, i7j5, i7j6, i7j7, i7j8, i7j9]
            row8 = [i8j1, i8j2, i8j3, i8j4, i8j5, i8j6, i8j7, i8j8, i8j9]
            row9 = [i9j1, i9j2, i9j3, i9j4, i9j5, i9j6, i9j7, i9j8, i9j9]

            board = []
            board.append(row1)
            board.append(row2)
            board.append(row3)
            board.append(row4)
            board.append(row5)
            board.append(row6)
            board.append(row7)
            board.append(row8)
            board.append(row9)

            solver(self, board)

            i1j1_var.set(board[0][0]); i1j2_var.set(board[0][1]); i1j3_var.set(board[0][2]); i1j4_var.set(board[0][3]); i1j5_var.set(board[0][4])
            i1j6_var.set(board[0][5]); i1j7_var.set(board[0][6]); i1j8_var.set(board[0][7]); i1j9_var.set(board[0][8]); i2j1_var.set(board[1][0])
            i2j2_var.set(board[1][1]); i2j3_var.set(board[1][2]); i2j4_var.set(board[1][3]); i2j5_var.set(board[1][4]); i2j6_var.set(board[1][5])
            i2j7_var.set(board[1][6]); i2j8_var.set(board[1][7]); i2j9_var.set(board[1][8]); i3j1_var.set(board[2][0]); i3j2_var.set(board[2][1])
            i3j3_var.set(board[2][2]); i3j4_var.set(board[2][3]); i3j5_var.set(board[2][4]); i3j6_var.set(board[2][5]); i3j7_var.set(board[2][6])
            i3j8_var.set(board[2][7]); i3j9_var.set(board[2][8]); i4j1_var.set(board[3][0]); i4j2_var.set(board[3][1]); i4j3_var.set(board[3][2])
            i4j4_var.set(board[3][3]); i4j5_var.set(board[3][4]); i4j6_var.set(board[3][5]); i4j7_var.set(board[3][6]); i4j8_var.set(board[3][7])
            i4j9_var.set(board[3][8]); i5j1_var.set(board[4][0]); i5j2_var.set(board[4][1]); i5j3_var.set(board[4][2]); i5j4_var.set(board[4][3])
            i5j5_var.set(board[4][4]); i5j6_var.set(board[4][5]); i5j7_var.set(board[4][6]); i5j8_var.set(board[4][7]); i5j9_var.set(board[4][8])
            i6j1_var.set(board[5][0]); i6j2_var.set(board[5][1]); i6j3_var.set(board[5][2]); i6j4_var.set(board[5][3]); i6j5_var.set(board[5][4])
            i6j6_var.set(board[5][5]); i6j7_var.set(board[5][6]); i6j8_var.set(board[5][7]); i6j9_var.set(board[5][8]); i7j1_var.set(board[6][0])
            i7j2_var.set(board[6][1]); i7j3_var.set(board[6][2]); i7j4_var.set(board[6][3]); i7j5_var.set(board[6][4]); i7j6_var.set(board[6][5])
            i7j7_var.set(board[6][6]); i7j8_var.set(board[6][7]); i7j9_var.set(board[6][8]); i8j1_var.set(board[7][0]); i8j2_var.set(board[7][1])
            i8j3_var.set(board[7][2]); i8j4_var.set(board[7][3]); i8j5_var.set(board[7][4]); i8j6_var.set(board[7][5]); i8j7_var.set(board[7][6])
            i8j8_var.set(board[7][7]); i8j9_var.set(board[7][8]); i9j1_var.set(board[8][0]); i9j2_var.set(board[8][1]); i9j3_var.set(board[8][2])
            i9j4_var.set(board[8][3]); i9j5_var.set(board[8][4]); i9j6_var.set(board[8][5]); i9j7_var.set(board[8][6]); i9j8_var.set(board[8][7])
            i9j9_var.set(board[8][8])
            
        def clear_grid(self):
            for widgets in Canvas.winfo_children(self):
                widgets.destroy()
            draw_grid(self)
        
        def find_empty(self, board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        return i, j

        def valid(self, board, pos, num):
            for i in range(9):
                if board[i][pos[1]] == num and \
                        (i, pos[1]) != pos:
                    return False

            for j in range(9):
                if board[pos[0]][j] == num and (pos[0], j) != pos:
                    return False

            start_i = pos[0] - pos[0] % 3
            start_j = pos[1] - pos[1] % 3
            for i in range(3):
                for j in range(3):
                    if board[start_i + i][start_j + j] == num and \
                            (start_i + i, start_j + j) != pos:
                        return False
            return True
        
        def solver(self, board):
            empty = find_empty(self, board)
            if not empty:
                return True

            for nums in range(9):
                if valid(self, board, empty, nums + 1):
                    board[empty[0]][empty[1]] = nums + 1

                    if solver(self, board):
                        return True
                    board[empty[0]][empty[1]] = 0
            return False

        draw_grid(self)

root = Tk()
root.geometry("400x315")
sudokuGrid()
root.mainloop()
