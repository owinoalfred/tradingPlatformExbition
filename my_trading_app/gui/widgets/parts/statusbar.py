import tkinter as tk

class Statusbar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = tk.Label(self, text="Ready")
        self.label.pack(side="left")