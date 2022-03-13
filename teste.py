import tkinter as tk
from tkinter import ttk
from core.gui import make_root

class Interface:
    """Interface"""
    def __init__(self, 
                root: tk.Tk):
        self.root = root

    def start(self):
        self.root.mainloop()