import tkinter as tk
from tkinter import *
import time
import csv

window = tk.Tk()  # selve vunduet
window.title('My Window')
window.geometry('350x200')  # størrelsen på vinduet
background = Frame(window, bg='white', width=350, height=200)  # en frame der fylder baggrunden
background.place(x=0, y=0)

l = tk.Label(window, bg='white', text='Velkommen til programmet')  # label øverst på siden
l.place(bordermode="inside")

timenow = ''

clock = Label(window, bd=3, text=timenow, bg='white')  # label til tiden
clock.place(x=175, y=75)


def timer():  # henter tiden i real time
    global timenow
    newtime = time.strftime('%c')
    if newtime != timenow:
        timenow = newtime
        clock.config(text=timenow)
    clock.after(200, timer)
    return timenow

timer()

def fornavn():  # henter fornavn og efternavn
    fornavn1 = e1.get()
    print(fornavn1)
    return fornavn1

def medlemsnummer():  # henter medlemsnummer
    medlemsnummer1 = e2.get()
    print(medlemsnummer1)
    return medlemsnummer1

var1 = tk.IntVar()  # laver inputtet om til en variable
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()

c1 = tk.Checkbutton(window, text='Møde ind', variable=var1, bg='white')  # hvordan og hvad der skal stå i checkboksene
c2 = tk.Checkbutton(window, text='gå hjem til fyraften', variable=var2, bg='white')
c3 = tk.Checkbutton(window, text='gå hjem pga. sygdom', variable=var3, bg='white')
c4 = tk.Checkbutton(window, text='gå hjem pga. barns sygdom', variable=var4, bg='white')

c1.place(x=0, y=100, bordermode="inside")  # x og y på placering, på hvor knapperne skal være
c2.place(x=150, y=100, bordermode="inside")
c3.place(x=0, y=125, bordermode="inside")
c4.place(x=150, y=125, bordermode="inside")

l1 = tk.Label(window, bg='white', text="Fornavn og efternavn").place(x=0, y=25, bordermode="inside")
l2 = tk.Label(window, bg='white', text="Medarbejdenummer").place(x=0, y=50, bordermode="inside")

e1 = tk.Entry(window, border=3)  # input feltet til tekst
e2 = tk.Entry(window, border=3)

e1.place(x=150, y=25, bordermode="inside")  # placering på den
e2.place(x=150, y=50, bordermode="inside")


def print_selection():  # definition som man henter i knappen
    b = tk.Label(window, bg='white')  # en label til en hilsen
    b.place(x=0, y=75)
    if (var1.get() + var2.get() + var3.get() + var4.get()) == 1:
        if (var1.get() == 1):  # ser om der er kryds i den første, osv.
            b.config(text='Super! God arbejdsdag ')
            kryds = "Mødt ind"
        elif (var2.get() == 1):
            b.config(text='Bare i orden. God fyraften')
            kryds = "gået hjem til fyraften"
        elif (var3.get() == 1):
            b.config(text='Det er jeg ked af at høre ')
            kryds = "gået hjem pga. sygdom"
        elif (var4.get() == 1):
            b.config(text='Det er jeg ked af at høre ')
            kryds = "gået hjem pga. barns sygdom"

    elif (var1.get() + var2.get() + var3.get() + var4.get()) != int(1):
        print("hej")
        b.config(text='Det passer vist ikke helt')
        return

    with open('fraveard.csv', 'a', encoding='UTF8') as f:  # tilføjer inputtet til en csv fil
        writer = csv.writer(f, delimiter=';')
        data = [fornavn(), medlemsnummer(), timenow, kryds]
        writer.writerow(data)

# Buttons
tk.Button(window, text='Submit', command=print_selection).place(x=150, y=150)  # laver en knap med funktionen print_selection
tk.Button(window, text='Quit', fg='red', command=window.quit).place(x=50, y=150)  # laver en knap som lukker prgrammet

window.mainloop()  # kører det i loop ind til andet er sagt
