from selenium import webdriver
import tkinter as tk
from tkinter import LEFT, TOP, END
import pandas as pd
import all_data
from PIL import Image, ImageTk
import legend
import custom_classes
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

root = tk.Tk()
root.geometry("1000x600")
root.wm_title("Фольклор 2.0")
root.iconbitmap(os.getcwd()+'//favicon.ico')

canvas = tk.Canvas(root)
canvas.pack(side=LEFT, fill=tk.BOTH, expand=True)
root.minsize(root.winfo_width(), root.winfo_height())


def open_map():
    o = Options()
    o.add_experimental_option("detach", True)
    cservice = Service(executable_path=os.getcwd() + '//chromedriver.exe')
    driver = webdriver.Chrome(service=cservice, options=o)
    driver.get("file:///" + os.getcwd() + "//map1.html")


def close_app():
    root.quit()


def new_window():
    legend.Legend()


def open_faq():
    window = custom_classes.CustomTopLevel()
    title = tk.Label(master=window, text='Сведения о проекте', font=("Monotype Corsiva", 30, "bold"))
    title.pack(padx=8, pady=8)
    text = tk.Label(master=window, text="""
    Приложение «Фольклор 2.0» призвано облегчить визуализацию 
    результатов анализа данных, связанного с проведением научного исследования 
    на тему «Русская фольклорная музыкальная традиция в культурном пространстве 
    современной Москвы: формы актуализации».
    Интерфейс приложения включает в себя интерактивную карту мест проведения 
    музыкальных фольклорных мероприятий в рамках фестиваля "Московская Масленица"; 
    легенду карты; многоуровневое меню с более подробной информацией о местах 
    проведения, исполнителях и характере мероприятий; а также данную справку.
    Имеющиеся сведения постоянно дополняются.
    «Фольклор 2.0» написан Гусевой Миленой, студенткой 3 курса ФИЯР, 
    на языке программирования Python 3 с использованием библиотеки TKinter. 
    Анализ данных проводился средствами библиотеки Pandas.
    Интерактивная карта выполнена с помощью библиотеки Folium и 
    работает через библиотеку для автоматизированного тестирования веб-приложений Selenium.

    Приятного использования!""", font=("Times New Roman", 17), justify=LEFT)
    text.pack(fill=tk.BOTH, padx=8, pady=8)
    context_menu1 = custom_classes.ContextMenu(master=window)


menu = tk.Menu(canvas)
root.config(menu=menu)

sub_menu = tk.Menu(menu)
new_menu = tk.Menu(sub_menu)
menu.add_cascade(label="Опции", menu=sub_menu)
sub_menu.add_cascade(label="Написать разработчику", menu=new_menu)
new_menu.add_command(label="milenchik.guseva@ya.ru (нажмите, чтобы копировать адрес)", command=root.clipboard_append("milenchik.guseva@ya.ru"))
sub_menu.add_separator()
sub_menu.add_command(label="Выход", command=close_app)
sub_menu.add_separator()

context_menu = custom_classes.ContextMenu()

img_name = 'que.png'
img = Image.open(img_name)
img_photo = ImageTk.PhotoImage(img)
frame = tk.Frame(master=canvas)
faq = tk.Button(master=frame, image=img_photo, command=open_faq)
button1 = tk.Button(master=frame, text='Открыть карту', font=("Monotype Corsiva", 16), bg="#CFA4FF", width=40, command=open_map)
button2 = tk.Button(master=frame, text='Легенда карты', font=("Monotype Corsiva", 16), bg="#CFA4FF", width=40, command=new_window)
button1.grid(row=1, column=1, padx=5)
button2.grid(row=1, column=4, padx=5)
faq.grid(row=1, column=6, padx=5)
frame.pack(side=TOP, expand=False)

data = pd.read_csv("doc.txt", encoding='windows-1251')
district = data["properties/Attributes/District"]
area = data["properties/Attributes/AdmArea"]
address = data["properties/Attributes/Address"]

places = [area[i] + ', ' + district[i] + ', ' + address[i] for i in range(60)]
artists = all_data.info_list
forms = all_data.activities_list
methods = all_data.methods_list
artists_all = []
forms_all = []
for i in range(len(artists)):
    for j in range(len(artists[i])):
        for k in range(len(artists[i][j])):
            artists_all.append(artists[i][j][k])

for i in range(len(forms)):
    for j in range(len(forms[i])):
        for k in range(len(forms[i][j])):
            forms_all.append(forms[i][j][k] + ', ' + methods[i][j][k])

title_1 = tk.Label(master=canvas, text='Места проведения Масленицы в разные годы', font=("Arial", 10, "bold"))
title_1.pack(padx=1, pady=1)

first_lb = custom_classes.CustomListbox(master=canvas)
for i in places:
    first_lb.insert(places.index(i), i)


title_2 = tk.Label(master=canvas, text='Выступающие коллективы', font=("Arial", 10, "bold"))
title_2.pack(padx=1, pady=1)

second_lb = custom_classes.CustomListbox(master=canvas)

title_3 = tk.Label(master=canvas, text='Формы и методы актуализации музыкального фольклора', font=("Arial", 10, "bold"))
title_3.pack(padx=1, pady=1)

third_lb = custom_classes.CustomListbox(master=canvas)


def print_selection(event_type):
    second_lb.delete(0, END)
    third_lb.delete(0, END)
    selection = first_lb.curselection()
    string = places[selection[0]]
    ind = places.index(string)
    for i in range(len(artists[ind][0])):
        second_lb.insert(0, '2018: ' + artists[ind][0][i])
    for i in range(len(artists[ind][1])):
        second_lb.insert(0, '2019: ' + artists[ind][1][i])
    for i in range(len(artists[ind][2])):
        second_lb.insert(0, '2020: ' + artists[ind][2][i])


def right_selection(event_type):
    third_lb.delete(0, END)
    selection = first_lb.selection_get()
    if selection[6:] in artists_all:
        ind = artists_all.index(selection[6:])
        third_lb.insert(0, forms_all[ind])


first_lb.bind("<Double-Button-1>", print_selection)
second_lb.bind("<Double-Button-1>", right_selection)

root.mainloop()
