import tkinter as tk
from customtkinter import CTkFrame
from gui.widgets.parts.toolbar import Toolbar
from gui.widgets.parts.statusbar import Statusbar

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Trading Platform")

        self.toolbar = Toolbar(self)
        self.toolbar.pack(side="top", fill="x")

        self.main_frame = CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.statusbar = Statusbar(self)
        self.statusbar.pack(side="bottom", fill="x")