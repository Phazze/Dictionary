from tkinter import *
from tkinter import ttk
import json
from pprint import pformat


tf = open("jsondir.json", "r")
dict = json.load(tf)

def window_spravka():
    spravka = Tk()
    spravka.title("Справка")
    spravka.geometry('400x250')
    lbl = Label(spravka, text="""
    ================СПРАВКА================
    Данный словарь создан для большого количества
    слов, но вот вывод, пока что не способен 
    вывести все слова, которые появятся в будующем.
    Словарь разработан курсантами ВМПИ и 
    студентом ГУМРФ(Некрашевичем Г.В.)
    Для сохранения достаточно нажать на кнопку
    действия( например кнопку добавления или
    удаления) 
    Желаю приятного использования программы
    """, font=("Arial Bold", 12), anchor="nw")
    lbl.grid(column=1, row=1)
    spravka.mainloop()


def window_dobavlenie():
    dobavlenie = Tk()
    dobavlenie.title("Добавить слово")
    dobavlenie.geometry('750x200')
    lbl1 = Label(dobavlenie, text="Слово", font=("Arial Bold", 12))
    lbl1.place(x=10, y=10)
    txt = ttk.Entry(dobavlenie, width=30)
    txt.place(x=70, y=10)
    lbl2 = Label(dobavlenie, text="Определение", font=("Arial Bold", 12))
    lbl2.place(x=10, y=40)
    txt2 = ttk.Entry(dobavlenie, width=100)
    txt2.place(x=120, y=40)
    lbl3 = Label(dobavlenie, text="ГОСТ", font=("Arial Bold", 12))
    lbl3.place(x=10, y=70)
    txt3 = ttk.Entry(dobavlenie, width=30)
    txt3.place(x=70, y=70)
    lbl4 = Label(dobavlenie, text="Источник", font=("Arial Bold", 12))
    lbl4.place(x=10, y=100)
    txt4 = ttk.Entry(dobavlenie, width=30)
    txt4.place(x=90, y=100)

    def dobavit_slovo():
        word = txt.get()
        word.lower()
        opred = txt2.get()
        GOST = txt3.get()
        istochnik = txt4.get()
        dict[word] = "Определение: " + opred + "," + "ГОСТ: " + GOST + "," + "Источник: " + istochnik
        lbl10 = Label(dobavlenie, text = "Слово" + "," + word + "," + "добавлено")
        lbl10.place(x = 80, y = 130)
        tf = open('jsondir.json', 'w')
        json.dump(dict, tf)
        tf.close()


    btn_dobavit_slovo = Button(dobavlenie, text="Добавить", command=dobavit_slovo)
    btn_dobavit_slovo.place(x=10,  y= 130, width= 60, height=50)

def window_poisk():
    poisk = Tk()
    poisk.title("Поиск слова")
    poisk.geometry('400x100')
    lbl5 = Label(poisk, text = "Найти слово", font=("Arial Bold", 12))
    lbl5.place(anchor='nw')
    txt5 = ttk.Entry(poisk, width= 30)
    txt5.place(x= 10,  y = 30)

    def poisk_slova():
        word_poisk = txt5.get()
        word_poisk= word_poisk.lower()
        lbl6 = Label(poisk, text = dict.get(word_poisk, "Нет такого слова!"))
        lbl6.place(x = 10, y = 70)

    btn_poisk_slova = Button(poisk, text="Найти", command=poisk_slova)
    btn_poisk_slova.place(x=200, y=25, width=60, height=30)

def window_ydalenie():
    ydalit = Tk()
    ydalit.title("Удалить слово")
    ydalit.geometry("400x100")
    lbl7 = Label(ydalit, text = "Удалить слово", font= ("Arial Bold", 12))
    lbl7.place(anchor="nw")
    txt6 = ttk.Entry(ydalit, width=30)
    txt6.place(x = 10, y = 30)

    def ydalit_slovo():
        word_delit = txt6.get()
        word_delit = word_delit.lower()
        if word_delit in dict:
            del dict[word_delit]
            lbl8 = Label(ydalit, text = "Слово" +","+ word_delit +","+"удалено", font=("Arial Bold",12))
            lbl8.place(x = 10 , y =70)
            tf = open('jsondir.json', 'w')
            json.dump(dict, tf)
            tf.close()
        else:
            lbl8 = Label(ydalit, text ="Слова" +","+ word_delit +","+"нет", font=("Arial Bold",12))
            lbl8.place(x=10, y=70)
    btn_ydalit_slovo = Button(ydalit, text="Удалить", command=ydalit_slovo)
    btn_ydalit_slovo.place(x=200, y =25, width=60, height=30)

def window_vivod():
    vivod = Tk()
    vivod.title("Вывод словаря")
    vivod.geometry("800x600")
    lbl9 = Label(vivod, text = "Словарь", font=("Arial Bold",12))
    lbl9.place(anchor="nw")
    txt7= Text(vivod, wrap=WORD)
    txt7.place(x= 10, y = 30)
    txt7.insert(1.0, pformat(dict, width=txt7['width']))
def vyxod_def():
    window.destroy()

window = Tk()
window.title("Словарь основное окно")
window.geometry('450x150')
btn_spravka = Button(window, text="Справка", command=window_spravka)
btn_spravka.grid(column=150, row=120)
btn_spravka.place(x=280, y=70, anchor='nw', width=60, height=50)
btn_dobalenie = Button(window, text="Добавить слово", command=window_dobavlenie)
btn_dobalenie.grid(column=150, row=120)
btn_dobalenie.place(x=10, y=10, width=160, height=50)
btn_poisk = Button(window, text = "Поиск",command= window_poisk)
btn_poisk.grid(column=150, row=120)
btn_poisk.place(x = 180, y=10, width= 60, height=50)
btn_ydalit = Button(window, text = "Удалить слово", command = window_ydalenie)
btn_ydalit.grid(column=150, row= 120)
btn_ydalit.place(x = 250, y = 10, width=160, height=50 )
btn_vivod = Button(window, text= "Вывод всего словаря", command= window_vivod)
btn_vivod.grid(column=150,row=120)
btn_vivod.place(x = 10, y = 70, width=260, height=50)
btn_vyxod = Button(window, text = "Выход", command = vyxod_def)
btn_vyxod.grid(column=150, row = 120)
btn_vyxod.place(x = 350, y = 70, width=60, height=50)
window.mainloop()

