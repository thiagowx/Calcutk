#Importar biblioteca/libreria Tkinter y para funciones matematicas
from tkinter import*
from math import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import Button, Tk, Frame, Entry

#Crear ventana para la calculadora
ventana = tk.Tk()
ventana.title("CALCULADORA")
ventana.geometry("282x448")
ventana.config(bg = "gray10")
ventana.resizable(0,0)

class HoverButton(Button):
 def __init__(self, master, **kw):
  Button.__init__(self, master = master, **kw)
  self.defaultBackground = self ["background"]
  self.bind("<Enter>", self.on_enter)
  self.bind("<Leave>", self.on_leave)

 def on_enter(self, e):
  self ["background"] = self ["activebackground"]

 def on_leave(self, e):
  self ["background"] = self.defaultBackground

tk.Button(ventana, text = "", height = 20, width = 20)

#Definir nuevas funciones, nombre (parametros)

c = 0
def add_number(num):
    global c
    c+= 1 
    entrada.insert(c, num) #1. posicion y 2. cadena

def operacion():
 global c
  
 kt = entrada.get()
 if c!= 0:
     try:  
         resultado = str(eval(kt))
         entrada.delete(0, END)
         entrada.insert(0, resultado) 
         calculador = len(resultado)
         i = calculador
     except:
         resultado = ("ERROR")
         entrada.delete(0, END)
         entrada.insert(0, resultado)
 else:
     pass
 
def clear():
  global c
  if c==-1:
     pass
  else:
     entrada.delete(c, last=None)
     c-=1

def clear_entrada():
    entrada.delete(0, END)
    c=0

#Crear una variable de texto para ingresar los datos 
entrada = Entry(ventana, font = ("Arial", 17), bg = "powder blue")
entrada.grid(row = 0, column = 0, columnspan = 4, padx = 6, pady = 6, ipadx = 3, ipady = 15)

  

#Crear botones y agregar funciones a la variable add number, señalar boton de color por encima del cursor
boton1 = HoverButton(ventana, text = "1", width = 4, height = 2, font = ("Arial", 15), activebackground = "tan1", bg = "gray55", fg = "white", command = lambda : add_number(1))
boton2 = HoverButton(ventana, text = "2", width = 4, height = 2, font = ("Arial", 15), activebackground = "tan1", bg = "gray55", fg = "white", command = lambda : add_number(2))
boton3 = HoverButton(ventana, text = "3", width = 4, height = 2, font = ("Arial", 15), activebackground = "tan1", bg = "gray55", fg = "white", command = lambda : add_number(3))
boton4 = HoverButton(ventana, text = "4", width = 4, height = 2, font = ("Arial", 15), activebackground = "tan1", bg = "gray55", fg = "white", command = lambda : add_number(4))
boton5 = HoverButton(ventana, text = "5", width = 4, height = 2, font = ("Arial", 15), activebackground = "tan1", bg = "gray55", fg = "white", command = lambda : add_number(5))
boton6 = HoverButton(ventana, text = "6", width = 4, height = 2, font = ("Arial", 15), activebackground = "tan1", bg = "gray55", fg = "white", command = lambda : add_number(6))
boton7 = HoverButton(ventana, text = "7", width = 4, height = 2, font = ("Arial", 15), activebackground = "tan1", bg = "gray55", fg = "white", command = lambda : add_number(7))
boton8 = HoverButton(ventana, text = "8", width = 4, height = 2, font = ("Arial", 15), activebackground = "tan1", bg = "gray55", fg = "white", command = lambda : add_number(8))
boton9 = HoverButton(ventana, text = "9", width = 4, height = 2, font = ("Arial", 15), activebackground = "tan1", bg = "gray55", fg = "white", command = lambda : add_number(9))
boton0 = HoverButton(ventana, text = "0", width = 4, height = 2, font = ("Arial", 15), activebackground = "tan1", bg = "gray55", fg = "white", command = lambda : add_number(0))
botondelete = HoverButton(ventana, text = "AC", width = 4, height = 2, font = ("NeoSans", 15), activebackground = "floral white", bg = "light slate gray", fg = "orange red", command = lambda : clear_entrada())
botondelete1 = HoverButton(ventana, text = "C", width = 4, height = 2, font = ("NeoSans", 15), activebackground = "chocolate3", bg = "light slate gray", fg = "white", command = lambda : clear())
botondecimal = HoverButton(ventana, text = ".", width = 4, height = 2, font = ("Arial", 15), activebackground = "cyan3", bg = "gray55", fg="white", command = lambda : add_number("."))
boton_parentesis1 = HoverButton(ventana, text = "(", width = 4, height = 2, font = ("Arial", 15), activebackground = "steel blue", bg = "gray20", fg = "white", command = lambda : add_number("("))
boton_parentesis2 = HoverButton(ventana, text = ")", width = 4, height = 2, font = ("Arial", 15), activebackground = "steel blue", bg = "gray20", fg = "white", command = lambda : add_number(")"))
boton_suma = HoverButton(ventana, text = "+", width = 4, height = 2, font = ("Arial", 15), activebackground = "hot pink", bg = "light slate gray", fg = "white", command = lambda : add_number("+"))
boton_resta = HoverButton(ventana, text = "-", width = 4, height = 2, font = ("Arial", 15), activebackground = "hot pink", bg = "light slate gray", fg = "white", command = lambda : add_number("-"))
boton_multipicacion = HoverButton(ventana, text = "×", width = 4, height = 2, font = ("Arial", 15), activebackground = "hot pink", bg = "light slate gray", fg = "white", command = lambda:add_number("*"))
boton_division = HoverButton(ventana, text = "÷", width = 4, height = 2, font = ("Arial", 15), activebackground = "hot pink", bg = "light slate gray", fg = "white", command = lambda : add_number("/"))
boton_igual = HoverButton(ventana, text = "=", width = 4, height = 2, font = ("Arial", 15), activebackground = "gold", bg = "orange red", fg="white", command = lambda : operacion())

#Botones en la ventana
boton7.grid(row=1, column=0, padx=6, pady=6)
boton8.grid(row=1, column=1, padx=6, pady=6)
boton9.grid(row=1, column=2, padx=6, pady=6)
boton_division.grid(row=2, column=3, padx=6, pady=6)
boton4.grid(row=2, column=0, padx=6, pady=6)
boton5.grid(row=2, column=1, padx=6, pady=6)
boton6.grid(row=2, column=2, padx=6, pady=6)
boton_multipicacion.grid(row=3, column=3, padx=6, pady=6)
boton1.grid(row=3, column=0, padx=6, pady=6)
boton2.grid(row=3, column=1, padx=6, pady=6)
boton3.grid(row=3, column=2, padx=6, pady=6)
boton_resta.grid(row=4, column=3, padx=6, pady=6)
boton0.grid(row=4, column=0, padx=6, pady=6)
boton_parentesis1.grid(row=5, column=0, padx=6, pady=6)
boton_parentesis2.grid(row=5, column=1, padx=6, pady=6)
boton_suma.grid(row=4, column=2, padx=6, pady=6)
boton_igual.grid(row=5, column=3, padx=6, pady=6)
botondelete1.grid(row=1, column=3, padx=6, pady=6)
botondelete.grid(row=5, column=2, padx=6, pady=6)
botondecimal.grid(row=4, column=1, padx=6, pady=6)

ventana.mainloop()