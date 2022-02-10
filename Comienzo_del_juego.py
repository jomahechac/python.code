import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Zona de juego") #Cambiar el nombre de la ventana
ventana.geometry("600x450") #Configurar tamaño
ventana.resizable(width=False, height=False)
ventana.config(bg="white") #Cambiar color de fondo

bienvenida = tk.Label(ventana, text='¡Hola! esta es tu Zona de juego', bg='white', font=("Input Mono Condensed", 14,), width=30, height=3)
introduccion= tk.Label(ventana, text="En este espacio encontraras 2 juegos a los cuales puedes ingresar \n\n" + "1. Serpiente \n" + "Usa las flechas para moverte\n\n" + "2. Estación espacial \n" + "Usa las flechas der e izq para rotar y espacio para disparar \n\n\n " + "¿Cual desea jugar?", bg='white', font=('Input Mono Condensed', 12), width=80, height=10)
regla = tk.Label(ventana, text="Solo tienes 3 rondas, luego tu juego terminará", bg='white', font=("Input Mono Condensed", 14,), width=50, height=25)
bienvenida.pack()
introduccion.pack()
regla.pack()

def serpiente():
    ventana.destroy()
    import Serpiente
    

def estacion_espacial():
    ventana.destroy()
    import Estacion_espacial
    
 
boton = ttk.Button(ventana,text="Serpiente", command=serpiente)
boton2 = ttk.Button(ventana,text="Estacion espacial", command=estacion_espacial)
boton.place(x=260, y=270)
boton2.place(x=248, y=300)
 
            
ventana.mainloop()
