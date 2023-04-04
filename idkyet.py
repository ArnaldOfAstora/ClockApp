import tkinter as tk
from tkinter import ttk



root = tk.Tk()
root.geometry("800x500")
root.title("Clock")
root.mainframe = ttk.Frame(border="9px solid black", padding=22 )




label = tk.Label(root, text="Clock", font=("monospace", 30))
label.place(x=100, y=100)



root.mainloop()


