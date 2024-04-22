from tkinter import Tk
from gui.widgets.parts.menu_bar import create_trading_menu

class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("My Trading App")
        create_trading_menu(self.root)  # Add the menu bar to the main window

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    window = MainWindow()
    window.run()