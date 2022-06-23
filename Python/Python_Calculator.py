from cgitb import text
from sqlite3 import Row
from tkinter import *
raiz = Tk()
raiz.title("Calculadora")
raiz.iconbitmap("calc.ico")
raiz.configure(background="#666666")

i = 0

#Entrada de texto
texto = Entry(raiz, font=("Calibri 20"), bg="#A4A4A4")
texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

#Funciones
def click_btn(valor):
    global i
    texto.insert(i, valor)
    i += 1

def borrar():
    texto.delete(0, 'end')
    i = 0

def operacion():
    ecuacion = texto.get()
    resultado = eval(ecuacion)
    texto.delete(0, 'end')
    texto.insert(0, resultado)
    i = 0

#Botones
btn1 = Button(raiz, text = "1", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn(1))
btn2 = Button(raiz, text = "2", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn(2))
btn3 = Button(raiz, text = "3", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn(3))
btn4 = Button(raiz, text = "4", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn(4))
btn5 = Button(raiz, text = "5", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn(5))
btn6 = Button(raiz, text = "6", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn(6))
btn7 = Button(raiz, text = "7", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn(7))
btn8 = Button(raiz, text = "8", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn(8))
btn9 = Button(raiz, text = "9", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn(9))
btn0 = Button(raiz, text = "0", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn(0))

btn_borrar = Button(raiz, text = "AC", bg="#A4A4A4", width = 5, height = 2, command = lambda: borrar())
btn_parentesis1 = Button(raiz, text = "(", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn("("))
btn_parentesis2 = Button(raiz, text = ")", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn(")"))
btn_punto = Button(raiz, text = ".", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn(""))

btn_div = Button(raiz, text = "/", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn("/"))
btn_mult = Button(raiz, text = "x", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn("*"))
btn_sum = Button(raiz, text = "+", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn("+"))
btn_rest = Button(raiz, text = "-", bg="#A4A4A4", width = 5, height = 2, command = lambda: click_btn("-"))
btn_igual = Button(raiz, text = "=", bg="#A4A4A4", width = 16, height = 2, command = lambda: operacion())

#Botones en pantalla
btn_borrar.grid(row = 1, column = 0, padx = 5, pady = 5)
btn_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
btn_parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
btn_div.grid(row = 1, column = 3, padx = 5, pady = 5)

btn7.grid(row = 2, column = 0, padx = 5, pady = 5)
btn8.grid(row = 2, column = 1, padx = 5, pady = 5)
btn9.grid(row = 2, column = 2, padx = 5, pady = 5)
btn_mult.grid(row = 2, column = 3, padx = 5, pady = 5)

btn4.grid(row = 3, column = 0, padx = 5, pady = 5)
btn5.grid(row = 3, column = 1, padx = 5, pady = 5)
btn6.grid(row = 3, column = 2, padx = 5, pady = 5)
btn_sum.grid(row = 3, column = 3, padx = 5, pady = 5)

btn1.grid(row = 4, column = 0, padx = 5, pady = 5)
btn2.grid(row = 4, column = 1, padx = 5, pady = 5)
btn3.grid(row = 4, column = 2, padx = 5, pady = 5)
btn_rest.grid(row = 4, column = 3, padx = 5, pady = 5)

btn0.grid(row = 5, column = 0, padx = 5, pady = 5)
btn_punto.grid(row = 5, column = 1, padx = 5, pady = 5)
btn_igual.grid(row = 5, column = 2, columnspan = 2, padx = 5, pady = 5)

raiz.mainloop()