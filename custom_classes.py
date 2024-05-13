import tkinter as tk
from tkinter import Frame, Menu, RIGHT


class CustomListbox(tk.Listbox):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.scrollable = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.yview)
        self.scrollable.pack(side=RIGHT, fill=tk.Y)
        self.config(yscrollcommand=self.scrollable.set)
        self.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)


# I still wonder if there's need in this class
class CustomTopLevel(tk.Toplevel):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.geometry("1000x600")
        self.wm_title("Фольклор 2.0")
        self.iconbitmap('favicon.ico')


class ContextMenu(Frame):
    def show_menu(self, e):
        self.menu.post(e.x_root, e.y_root)

    def on_exit(self):
        self.master.withdraw()

    def __init__(self,  **kw):
        super().__init__(**kw)
        self.menu = Menu(tearoff=0)
        self.menu.add_command(label="Выход", command=self.on_exit)
        self.master.bind("<Button-3>", self.show_menu)
        self.pack(expand=False)
