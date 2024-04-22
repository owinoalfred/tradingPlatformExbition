import tkinter as tk
from customtkinter import CTkButton

class Toolbar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.dashboard_button = CTkButton(self, text="Dashboard")
        self.dashboard_button.pack(side="left")

        self.markets_button = CTkButton(self, text="Markets")
        self.markets_button.pack(side="left")

        self.trades_button = CTkButton(self, text="Trades")
        self.trades_button.pack(side="left")

        self.futures_button = CTkButton(self, text="Futures")
        self.futures_button.pack(side="left")

        self.wallet_button = CTkButton(self, text="Wallet")
        self.wallet_button.pack(side="left")