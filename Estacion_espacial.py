import turtle
import math
import random
import tkinter as tk
from tkinter import ttk

rondas=0 
ventana2 = turtle.Screen()
ventana2 .setup(width=600, height=600)
ventana2.title("Estación Espacial") 
ventana2.bgcolor("black")
ventana2.tracer(0)

# Registrar nuevas figuras
player_vertices = ((0,10),(15,0),(15,-10),(10,-5),(5,-5),(0,-15),(-5,-5),(-10,-5),(-15,-10),(-15,0)) #creeamos la figura con vertices que dispara 
ventana2.register_shape("player", player_vertices) #insertamos un nueva shape a turtle 


asteroid_vertices = ((-5, 10), (5, 10), (10,5), (10,-5), (5, -10), (-10, -10), (-15, 0)) #creamos los asteroides 
ventana2.register_shape("asteroid", asteroid_vertices)

#aminar los movimientos del juego 

class Sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        # Maxima velocidad de la animación
        self.speed(0.2)
        self.penup() #no dejar rastro

#definimos la direccion en va a apuntar la nave         
def direccion_cabeza(t1, t2):
    x1 = t1.xcor()
    y1 = t1.ycor()
    
    x2 = t2.xcor()
    y2 = t2.ycor()
    
    heading = math.atan2(y1 - y2, x1 - x2) #pendiente
    heading = heading * 180.0 / 3.14159 #en grados
    
    return heading

#creamos la nave   
player = Sprite()
player.color("white")
player.shape("player")
puntaje= 0
record= 0


misiles = [] # es una lista ya que van a ir unos de tras de otro
for _ in range(3): #cantidad de misiles a lanzar por click
    misil = Sprite()
    misil.color("red")  #color
    misil.shape("arrow") #orma
    misil.speed = 1 #velocidad
    misil.state = "ready"
    misil.hideturtle() #ocultamos el misil para que no se vea sobre la figura
    misiles.append(misil) #unimos los misiles en la lista


texto = Sprite()
texto.color("white")
texto.hideturtle()
texto.goto(0, 250)
texto.write("Puntaje: 0      Record: 0", False, align = "center", font = ("Input Mono Condensed", 24, "normal"))

asteroids = [] #lista paraa los asteroides

#definir los asteroides

for _ in range(5):  #cantidad de asteroides a destruir   
    asteroid = Sprite()
    asteroid.color("brown")
    asteroid.shape("asteroid")
    asteroid.speed = 0.06 #velocidad del asteroide
    asteroid.goto(0, 0) #posicion hacia donde se dirigiran 
    heading = random.randint(0, 260) #aparicion de los asteroides en una posicion random entre un rango 
    distancia = random.randint(300, 400) #distancia entre ellos
    asteroid.setheading(heading) #cambiar la direccion de los asteroides
    asteroid.fd(distancia) #mover el asteroide a la posicion lejana de la nave
    asteroid.setheading(direccion_cabeza(player, asteroid)) #dirigir los asteroides a la nave
    asteroids.append(asteroid) #ir agregando los asteroides a la lista para que sigan el movimiento continuo

#rotacion de la nave

def rotate_left(): #izquierda
    player.lt(20)
    
def rotate_right(): #derecha
    player.rt(20)
    
def disparar_misil(): #direccion de los misiles con la nave 
    for misil in misiles:
        if misil.state == "ready":
            misil.goto(0, 0)
            misil.showturtle() #mostrar los misiles lanzados
            misil.setheading(player.heading()) #definir el angulo de lanzamiento respecto a la nave
            misil.state = "disparar"
            break

#Conectar el teclado al programa

ventana2.listen()
ventana2.onkey(rotate_left, "Left")
ventana2.onkey(rotate_right, "Right")
ventana2.onkey(disparar_misil, "space") #tecla para lanzar los misiles

#iniciar el juego 
Game_Over = False
while True:
    # actualizacion del juego 
    ventana2.update()
    player.goto(0, 0) 
    
    # Mover el misil
    for misil in misiles:
        if misil.state == "disparar":
            misil.fd(misil.speed)
        
        # Difinicion de los misiles con borde
        if misil.xcor() > 300 or misil.xcor() < -300 or misil.ycor() > 300 or misil.ycor() < -300:
            misil.hideturtle()
            misil.state = "ready"

    #iterar los asteroides
    for asteroid in asteroids:    
        # mover el asteroide 
        asteroid.fd(asteroid.speed)
        
        # Colisiones
        # Asteroide y misil
        for misil in misiles:
            if asteroid.distance(misil) < 20: #definir la distancia entre el asteroide y el misil <20pixels
                # Reiniciar asteroides
                heading = random.randint(0, 260)
                distancia = random.randint(600, 800)
                asteroid.setheading(heading)
                asteroid.fd(distancia) #revisar la distancia entre entre el asteroide y el misil 
                asteroid.setheading(direccion_cabeza(player, asteroid)) #crear nuevos asteroides
                asteroid.speed += 0.01 #velocidad del asteroide
                
                # Reiniciar Missile 
                misil.goto(600, 600)
                misil.hideturtle() #escoder misilis ya usados
                misil.state = "ready"
                player.color("white")
                
                # aumentar puntaje
                puntaje += 10

                if puntaje > record:
                    record = puntaje 
                texto.clear() #borrar para que no se sobre-escribra
                texto.write("Puntaje: {}     Record: {}".format(puntaje,record), False, align = "center", font = ("Input Mono Condensed", 24, "normal"))

        # Asteroide y jugador
        if asteroid.distance(player) < 22:
            # Riniciar asteroide
            heading = random.randint(0, 260)
            distancia = random.randint(600, 800)
            asteroid.setheading(heading)
            asteroid.fd(distancia)
            asteroid.setheading(direccion_cabeza(player, asteroid))
            asteroid.speed += 0.06
            Game_Over = True #el juego termino 
            puntaje=0
            texto.clear() 
            texto.write("Puntaje: {}     Record: {}".format(puntaje,record), False, align = "center", font = ("Input Mono Condensed", 24, "normal"))
    if Game_Over == True:
        player.color("red") #toma este color cuando pierde
        rondas+=1
        Game_Over = False #se reinicia automaticamente
        if rondas==3:
            rondas==0
            ventana2.bye()

            def finalizar():
                pregunta.destroy()

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




            pregunta=tk.Tk()
            pregunta.title("Gacias por jugar") #Cambiar el nombre de la ventana
            pregunta.geometry("600x350") #Configurar tamaño
            pregunta.resizable(width=False, height=False)
            pregunta.config(bg="white") #Cambiar color de fondo
            fin = tk.Label(pregunta, text='Haz perdido tus 3 rondas 😥', bg='white', font=("Input Mono Condensed", 14,), width=30, height=3)
            gracias= tk.Label(pregunta, text='Gracias por jugar', bg='white', font=("Input Mono Condensed", 12,), width=30, height=3)
            botn1 = ttk.Button(pregunta,text="Finalizar", command=finalizar)
            botn2= ttk.Button(pregunta,text="Referencias", command=referencias)
            botn3= ttk.Button(pregunta,text="Integrantes", command=integrantes)
            botn1.place(x=260, y=200)
            botn2.place(x=260, y=170)
            botn3.place(x=260, y=140)
            fin.pack()
            gracias.pack()
            pregunta.mainloop()
            break

