from ast import Delete
import turtle 
#metodo grafico para ventanas graficas
import time
#retrasar la velocidad del programa
import random
#posicion random
import tkinter as tk
#ventanas
from tkinter import ttk


posponer = 0.1 #pospone el programa 

puntaje=0  #El juego inicia coon puntaje 0
record=0
rondas=0

#Configuracion/Crear de la ventana o aspecto grafico

ventana3 = turtle.Screen()  #crea la ventana
ventana3.title("Proyecto: Juego de Snake") #titulo de la ventana
ventana3.bgcolor("black")  #color del fondo de la pantalla
ventana3.setup(width = 600, height = 600)  #dimensiones de la ventana
ventana3.tracer(0)  #Animacion mas fluida

#Crear la Cabeza de la Serpiente

cabeza = turtle.Turtle() #creamos la figura(turtle)
cabeza.speed(0) #cuando inicie la figura ya este ahi
cabeza.shape("square") #forma de la cabeza
cabeza.color("white") #color de la cabeza
cabeza.penup() #cuando se mueva no deja un rastro
cabeza.goto(0,0) #posición en pantalla(centro de la pantalla)
cabeza.direction = "stop" #al inicio este detenida

#Crear la Comida para la Serpiente, igual es un objeto se crea igual que la cabeza
comida = turtle.Turtle()
comida.speed(0)
comida.shape("turtle")
comida.color("green")
comida.penup()
comida.goto(0,100)

#Cuerpo de la Serpiente(son segmentos)

serpiente = [] #declaramos una lista para que cada vez que coma crezca

#Texto para pantalla

texto = turtle.Turtle()
texto.speed(0)
texto.color("blue")
texto.penup() #para que ya este pintado
texto.hideturtle()
texto.goto(0,-260)
texto.write("Puntaje: 0      Record: 0", align = "center",
            font=("Input Mono Condensed", 24, "normal"))

#Funciones (Para que se mueva)

def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"

#conectar teclado al programa

ventana3.listen() #estar atento al teclado 
ventana3.onkeypress(arriba, "Up") #funcion que se activa y tecla que se llamo
ventana3.onkeypress(abajo, "Down")
ventana3.onkeypress(izquierda, "Left")
ventana3.onkeypress(derecha, "Right")

def movimiento():
    if cabeza.direction == "up":
        y = cabeza.ycor() #coordenada inicial y
        cabeza.sety(y + 20)        #Se mueve 20 pixeles con cada movimiento hacia arriba
    elif cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20) #movimiento hacia abajo
    elif cabeza.direction == "left": 
        x = cabeza.xcor() #coordenada inicial x
        cabeza.setx(x - 20) #Moviemiento izquierda
    elif cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20) #movimiento derecha

Game_Over = False
while True:
    ventana3.update()

    #Colision con el Borde del juego

    if cabeza.xcor()>270 or cabeza.xcor() <-270 or cabeza.ycor() > 270 or cabeza.ycor() < -270:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #Esconder el cuerpo muerto y limpiarlo de la serpiente

        for parte in serpiente:
            parte.goto(2000,2000) #mandar los segmentos a una parte oculta de la ventana
        serpiente.clear() #limpiar la lista de segmentos

        #Resetear el marcador

        puntaje = 0
        texto.clear()
        texto.write("Puntaje: {}      Record: {}".format(puntaje, record),
                    align = "center", font=("Input Mono Condensed", 24, "normal"))
        Game_Over = True #el juego termino
        

    #Colisiones con la Comida

    if cabeza.distance(comida)<20: #es 20 que tiene 20pixels x 20 pixels, si la distancia es menor, se tocaron
        x=random.randint(-280,280) #moverla a un lugar random, con un rango de valores
        y=random.randint(-280,280)
        comida.goto(x,y) #actualizar la posicion 
        
        #Se crea el Cuerpo de la Serpiente

        cuerpo = turtle.Turtle()
        cuerpo.speed(0)
        cuerpo.shape("square")
        cuerpo.color("grey")
        cuerpo.penup()
        cuerpo.direction = "stop"
        serpiente.append(cuerpo) #agregar al final de la lista

        #Puntaje
        puntaje += 5
        
        #Actualizar puntaje más alto
        if puntaje > record:
            record = puntaje
            
        texto.clear() #limipiar texto para que no se sobrepongan
        texto.write("Puntaje: {}      Record: {}".format(puntaje, record),
                    align = "center", font=("Input Mono Condensed", 24, "normal"))

    #Movimiento de la Serpiente para que se sigan uno detras de otro 

    totalserpiente = len(serpiente) #total segmentos del cuerpo
    for i in range(totalserpiente -1, 0, -1): #iterar entre cada uno sin tomar la cabeza
        x=serpiente[i - 1].xcor() #coordenadas del elemento anterior
        y=serpiente[i - 1].ycor()
        serpiente[i].goto(x,y) #mover el actual segun las coordenadas
    if totalserpiente > 0:
        x = cabeza.xcor() #si ya tengo elementos, moverse donde esta la cabeza
        y = cabeza.ycor()
        serpiente[0].goto(x,y)

        

    movimiento()

    #Colision con el cuerpo

    for parte in serpiente: #cada segmento del cuerpo de la serpiente
        if parte.distance(cabeza) < 20: #que la cabeza no este menos de 20pixels 
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            
            #escodemos si se tecaron 

            for parte in serpiente:
                parte.goto(1000,1000)
            serpiente.clear()

            puntaje = 0
            texto.clear()
            texto.write("Puntaje: {}      Record: {}".format(puntaje, record),
                    align = "center", font=("Input Mono Condensed", 24, "normal"))
            Game_Over = True #el juego termino
    if Game_Over == True:
        rondas+=1
        Game_Over = False #se reinicia automaticamente
        if rondas==3:
            rondas=0
            ventana3.bye()


            def finalizar():
                adios.destroy()
            
            def referencias():
                bibi=tk.Tk()
                bibi.title("Bibliografia de referencias") #Cambiar el nombre de la ventana
                bibi.geometry("1000x550") #Configurar tamaño
                bibi.resizable(width=False, height=False)
                bibi.config(bg="white")
                refe = tk.Label(bibi, text='REFERENCIAS', bg='white', font=("Input Mono Condensed", 14,), width=100, height=3)
                refe1= tk.Label(bibi, text='1. Cómo hacer un videojuego con Python (https://youtu.be/bW0o4g4cg1g)', bg='white', font=("Input Mono Condensed", 12,), width=100, height=2)
                refe2= tk.Label(bibi, text='2. turtle — Gráficos con Turtle (https://docs.python.org/es/3.9/library/turtle.html#turtle.addshape)', bg='white', font=("Input Mono Condensed", 12,), width=100, height=2)
                refe3= tk.Label(bibi, text='3. Live Python Coding - Space Station Defense Game (https://www.youtube.com/watch?v=QiZPWZum_q8)', bg='white', font=("Input Mono Condensed", 12,), width=100, height=2)
                refe4= tk.Label(bibi, text='4. Python / Pygame Tutorial: An introduction to sprites (https://www.youtube.com/watch?v=hDu8mcAlY4E)', bg='white', font=("Input Mono Condensed", 12,), width=100, height=2)
                refe5= tk.Label(bibi, text='5. Cómo hacer un videojuego con Python (https://youtu.be/bW0o4g4cg1g)', bg='white', font=("Input Mono Condensed", 12,), width=100, height=2)
                refe6= tk.Label(bibi, text='6. Gráficos: el módulo turtle (1) (https://www.mclibre.org/consultar/python/lecciones/python-turtle-1.html)', bg='white', font=("Input Mono Condensed", 12,), width=100, height=2)
                refe7= tk.Label(bibi, text='7. Python 3 - Tkinter tkMessageBox (https://www.tutorialspoint.com/python3/tk_messagebox.htm)', bg='white', font=("Input Mono Condensed", 12,), width=100, height=2)
                refe8= tk.Label(bibi, text='8. Python --- (diez) componente de la ventana de Tkinter (https://programmerclick.com/article/9657736117/)', bg='white', font=("Input Mono Condensed", 12,), width=100, height=2)
                refe9= tk.Label(bibi, text='9. Variables de control en Tkinter (https://python-para-impacientes.blogspot.com/2016/02/variables-de-control-en-tkinter.html)', bg='white', font=("Input Mono Condensed", 12,), width=100, height=2)
                refe10= tk.Label(bibi, text='10. Introducción a Tcl/Tk (tkinter) (https://recursospython.com/guias-y-manuales/introduccion-a-tkinter/)', bg='white', font=("Input Mono Condensed", 12,), width=100, height=2)
                refe.pack()
                refe1.pack()
                refe2.pack()
                refe3.pack()
                refe4.pack()
                refe5.pack()
                refe6.pack()
                refe7.pack()
                refe8.pack()
                refe9.pack()
                refe10.pack()

            def integrantes():
                integ=tk.Tk()
                integ.title("Integrantes") #Cambiar el nombre de la ventana
                integ.geometry("800x300") #Configurar tamaño
                integ.resizable(width=False, height=False)
                integ.config(bg="white")
                inte = tk.Label( integ, text='INTEGRANTES', bg='white', font=("Input Mono Condensed", 14,), width=100, height=2)
                inte0 = tk.Label( integ, text='Grupo 29', bg='white', font=("Input Mono Condensed", 12,), width=100, height=3)
                inte1= tk.Label( integ, text='Johann Santiago Mahecha - jomahechac@unal.edu.co - Ingeniería Civil', bg='white', font=("Input Mono Condensed", 12,), width=100, height=2)
                inte2= tk.Label( integ, text='Diana Valentina Rojas - dirojass@unal.edu.co - Ingeniería Civil', bg='white', font=("Input Mono Condensed", 12,), width=100, height=2)
                inte3= tk.Label( integ, text='Iveth Andrea Soto - iasotor@unal.edu.co - Ingeniería Civil', bg='white', font=("Input Mono Condensed", 12,), width=100, height=2)
                inte.pack()
                inte0.pack()
                inte1.pack()
                inte2.pack()
                inte3.pack()

            adios=tk.Tk()
            adios.title("Gacias por jugar") #Cambiar el nombre de la ventana
            adios.geometry("600x300") #Configurar tamaño
            adios.resizable(width=False, height=False)
            adios.config(bg="white") #Cambiar color de fondo
            fin = tk.Label(adios, text='Haz perdido tus 3 rondas 😥', bg='white', font=("Input Mono Condensed", 14,), width=30, height=3)
            gracias= tk.Label(adios, text='Gracias por jugar', bg='white', font=("Input Mono Condensed", 12,), width=30, height=3)
            botn1 = ttk.Button(adios,text="Finalizar", command=finalizar)
            botn2= ttk.Button(adios,text="Referencias", command=referencias)
            botn3= ttk.Button(adios,text="Integrantes", command=integrantes)
            botn1.place(x=260, y=200)
            botn2.place(x=260, y=170)
            botn3.place(x=260, y=140)
            fin.pack()
            gracias.pack()
            adios.mainloop()
            break
    time.sleep(posponer)


    
