from tkinter import *
import tkinter
from PIL import Image, ImageTk


class Legend:
    def __init__(self):
        self.win = tkinter.Toplevel()
        self.win.geometry("700x350")
        self.win.wm_title("Фольклор 2.0")
        self.win.iconbitmap('favicon.ico')

        self.frame = tkinter.Frame(self.win)
        self.frame.grid()

        self.image = Image.open("img1.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.but = tkinter.Button(self.frame, text="Элемент 1 из 2", font=("Monotype Corsiva", 16), bg="#CFA4FF", width=40, pady=5, command=self.change_image).grid(row=1, column=1)

        self.description = tkinter.Label(self.frame, text="""
                Зелёный маркер указывает на те точки на карте, 
                где за последние 3 года проходили мероприятия,
                связанные с русским музыкальным фольклором 
                в рамках фестиваля "Московская Масленица". """, font=('Arial', 11), justify=LEFT).grid(row=2, column=1)

        self.canvas = tkinter.Canvas(self.win, height=600, width=700)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=3, column=1)

    def change_image(self):
        self.but = tkinter.Button(self.frame, text="Элемент 2 из 2", font=("Monotype Corsiva", 16), bg="#CFA4FF", width=40, pady=5, command=self.change_back).grid(row=1, column=1)
        self.image = Image.open("img.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=3, column=1)
        self.description = tkinter.Label(self.frame, text="""
                        Оранжевый маркер указывает на те точки
                        на карте, где соответствующие мероприятия 
                        не проводились или же касательно которых
                        нет никаких данных.""", font=('Arial', 11), justify=LEFT).grid(row=2, column=1)

    def change_back(self):
        self.but = tkinter.Button(self.frame, text="Элемент 1 из 2", font=("Monotype Corsiva", 16), bg="#CFA4FF", width=40, pady=5, command=self.change_image).grid(row=1, column=1)
        self.image = Image.open("img1.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=2, column=1)
        self.description = tkinter.Label(self.frame, text="""
                        Зелёный маркер указывает на те точки на карте, 
                        где за последние 3 года проходили мероприятия,
                        связанные с русским музыкальным фольклором 
                        в рамках фестиваля "Московская Масленица". """, font=('Arial', 11), justify=LEFT).grid(row=2, column=1)
