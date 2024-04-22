import tkinter as tk
import customtkinter as ctk

def create_trading_menu(root):
    # Create a CTKMenu
    menu = ctk.CTkMenu(root, bg_color="black", fg_color="white", hover_color="green")

    # Add some menu items
    file_menu = ctk.CTkMenu(menu, tearoff=0, bg_color="black", fg_color="white", hover_color="green")
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New Trade")
    file_menu.add_command(label="Open Portfolio")
    file_menu.add_command(label="Save Portfolio")
    file_menu.add_command(label="Exit", command=root.quit)

    # Create a dropdown menu under the "Trade" menu
    trade_menu = ctk.CTkMenu(menu, tearoff=0, bg_color="black", fg_color="white", hover_color="green")
    menu.add_cascade(label="Trade", menu=trade_menu)
    buy_menu = ctk.CTkMenu(trade_menu, tearoff=0, bg_color="black", fg_color="white", hover_color="green")
    trade_menu.add_cascade(label="Buy", menu=buy_menu)
    buy_menu.add_command(label="Stocks")
    buy_menu.add_command(label="Bonds")
    buy_menu.add_command(label="Commodities")

    sell_menu = ctk.CTkMenu(trade_menu, tearoff=0, bg_color="black", fg_color="white", hover_color="green")
    trade_menu.add_cascade(label="Sell", menu=sell_menu)
    sell_menu.add_command(label="Stocks")
    sell_menu.add_command(label="Bonds")
    sell_menu.add_command(label="Commodities")

    # Configure the root menu
    root.config(menu=menu)

root = tk.Tk()
create_trading_menu(root)
root.mainloop()