# Librerías:
from tkinter import *
from tkinter import ttk
from timeit import default_timer
#from playsound import playsound
import threading
import time
import winsound







def start():
    global ventana
    ventana = Tk()
    ventana.geometry("1500x768")
    ventana.title("Mi primera interfaz")
    ventana.iconbitmap("Programming.ico")
    ventana.resizable(False, False)
    Principal()


def Principal():

    #Canvas:
    canvas_Personal = Canvas(ventana, width=1050, height=760, bg="#86D5D2").place(x=450, y=2)
    canvas_Fibonacci = Canvas(ventana, width=450, height=760, bg="#E8BCF0").place(x=0, y=1)

    #Etiquetas
    label1 = Label(canvas_Personal, text="Datos del programador:",font=("Bahnschrift SemiBold SemiConden", 22),bg="#86D5D2", fg="#000000").place(x=880, y=5)
    label2 = Label(canvas_Personal, text="Nombre: Noemí Vargas Soto",font=("Bahnschrift SemiBold SemiConden", 22),bg="#86D5D2", fg="#000000").place(x=480, y=55)
    label3= Label(canvas_Personal, text="Carnet: 2021082564",font=("Bahnschrift SemiBold SemiConden", 22),bg="#86D5D2", fg="#000000").place(x=480, y=110)
    label4 = Label(canvas_Personal, text="Género: Femenino",font=("Bahnschrift SemiBold SemiConden", 22),bg="#86D5D2", fg="#000000").place(x=480, y=165)
    label5 = Label(canvas_Personal, text="Edad: 18 años",font=("Bahnschrift SemiBold SemiConden", 22),bg="#86D5D2", fg="#000000").place(x=480, y=220)
    label6 = Label(canvas_Personal, text="Dirección:",font=("Bahnschrift SemiBold SemiConden", 22),bg="#86D5D2", fg="#000000").place(x=480, y=275)
    label7 = Label(canvas_Personal, text="Canadá es un barrio de la zona de Turrialba, especificamente del distrito de La Suiza.",font=("Bahnschrift SemiBold SemiConden", 22),bg="#86D5D2", fg="#000000").place(x=480, y=310)
    label8 = Label(canvas_Personal, text="Lo primero que podemos observar son sus extensas áreas verdes en medio de los",font=("Bahnschrift SemiBold SemiConden", 22),bg="#86D5D2", fg="#000000").place(x=480, y=345)
    label9 = Label(canvas_Personal, text="hogares que yacen aquí. Sus calles de lastre aportan todavía más a su aspecto rural,",font=("Bahnschrift SemiBold SemiConden", 22),bg="#86D5D2", fg="#000000").place(x=480, y=380)
    label10 = Label(canvas_Personal, text="sumado a animales que vagan por pastizales y recintos.",font=("Bahnschrift SemiBold SemiConden", 22),bg="#86D5D2", fg="#000000").place(x=480, y=418)
    label11= Label(canvas_Fibonacci, text="Sucesión Fibonacci:", font=("Bahnschrift SemiBold SemiConden", 22), bg="#E8BCF0", fg="#000000").place(x=113, y=5)
    label21= Label(canvas_Fibonacci, text="Ingresa un número: ", font=("Bahnschrift SemiBold SemiConden", 19), bg="#E8BCF0", fg="#000000").place(x=15, y=70)

    #Imagenes pantalla principal
    mapa_imagen = PhotoImage(file = "Mapa_Canada.png")
    mapa = Label(canvas_Personal, image = mapa_imagen).place(x=1130, y= 460)
    noemi_imagen = PhotoImage(file = "personal.png")
    noemi = Label(canvas_Personal, image = noemi_imagen).place(x=1200, y= 60)
    fib_imagen = PhotoImage(file = "fibonacci.png")
    fib = Label(canvas_Fibonacci, image = fib_imagen).place(x=22, y= 480)

    #Entrada
    dato = StringVar()
    numero = Entry(canvas_Fibonacci, width=25, textvariable = dato).place(x=140, y=110)
    
    

    #Boton 1
    def fib():
        fib = int(dato.get())
        texto1="El resultado de ese número es: " + str(fibonacci(fib))
        texto2="El total de llamadas recursivas es: " + str(llamadas(fib, 0))
        texto3="El tiempo que se duró en la ejecución fue: " + str(tiempo(fib))
        labelFibo = Label(canvas_Fibonacci, text=texto1, font=("Bahnschrift SemiBold SemiConden", 13),bg="#E8BCF0", fg="#000000").place(x=15, y=310)
        labelConeto= Label(canvas_Fibonacci, text=texto2, font=("Bahnschrift SemiBold SemiConden", 13),bg="#E8BCF0", fg="#000000").place(x=15, y=345)
        labelTiempo= Label(canvas_Fibonacci, text=texto3, font=("Bahnschrift SemiBold SemiConden", 12),bg="#E8BCF0", fg="#000000").place(x=15, y=380)
        
        
            
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else: 
            return (fibonacci(n-1)+ fibonacci(n-2))

        
    def llamadas(n, conteo):
        if n == 0 or n == 1:
            return conteo
        else:
            return llamadas(n-1, conteo + 1)+ llamadas(n-2, conteo)
            

    def tiempo(n):
        inicio = default_timer()
        fibonacci(n)
        fin = default_timer()
        return (fin - inicio)

        
        
    boton1 = Button(canvas_Fibonacci, text="Ver resultados",command=fib).place(x=175, y=140)


    coldplay_imagen=PhotoImage(file="coldplay.png")
    natacion_imagen=PhotoImage(file="natacion.png")
    #Boton 2
    def gustos():
            canva2 = Canvas(ventana, width=1500, height=768,bg="#F69D9D")
            canva2.place(x=0, y=0)
            musica= Label(canva2, text="Gusto Musical:", font=("Bahnschrift SemiBold SemiConden", 22),bg="#F69D9D", fg="#000000").place(x=230, y=5)
            
            coldplay = Label(canva2, image = coldplay_imagen).place(x=10, y=60)
            genero = Label(canva2, text="Géneros:",font=("Bahnschrift SemiBold SemiConden", 22),bg="#F69D9D", fg="#000000").place(x=50, y=500)
            genero1 = Label(canva2, text="Britpop",font=("Bahnschrift SemiBold SemiConden", 22),bg="#F69D9D", fg="#000000").place(x=120, y=545)
            genero2 = Label(canva2, text="Dance/Electrónica",font=("Bahnschrift SemiBold SemiConden", 22),bg="#F69D9D", fg="#000000").place(x=120, y=589)
        
            deporte= Label(canva2, text="Deporte favorito:", font=("Bahnschrift SemiBold SemiConden", 22),bg="#F69D9D", fg="#000000").place(x=1100, y=5)
            natacion = Label(canva2, image = natacion_imagen).place(x=870, y=60)
            descripcion = Label(canva2, text="La natación es un deporte que consiste en el", font=("Bahnschrift SemiBold SemiConden", 22),bg="#F69D9D", fg="#000000").place(x=930, y=500)
            descripcion2 = Label(canva2, text="desplazamiento de una persona en el agua,", font=("Bahnschrift SemiBold SemiConden", 22),bg="#F69D9D", fg="#000000").place(x=930, y=550)
            descripcion3 = Label(canva2, text="sin que esta toque el suelo.​", font=("Bahnschrift SemiBold SemiConden", 22),bg="#F69D9D", fg="#000000").place(x=930, y=600)

                
            def play():
                winsound.PlaySound('hymn-for-the-weekend.wav', winsound.SND_FILENAME)
            
            reproducir = Button(canva2, width =16, height=1, font=("Bahnschrift SemiBold SemiConden", 15), text="Reproducir canción", command = play).place(x=250, y=670)

            def regresar():
                    Principal()


            
            regreso1 = Button(canva2, width =15, height=1, font=("Bahnschrift SemiBold SemiConden", 15), text="Regresar", command=regresar).place(x=670, y=700)

            canva2.create_image(10,60, image = coldplay_imagen, anchor = NW)
            canva2.create_image(870,60, image = natacion_imagen, anchor = NW)
                
    boton2 = Button(canvas_Personal, width =15, height=3, font=("Bahnschrift SemiBold SemiConden", 15), text="Gustos del\nprogramador", command=gustos).place(x=630, y=490)


    #Botón 3
    class Name:
        def __init__(self, canva):
            self.canva = canva
            self.shape = canva.create_text(100, 100, font= ("arial", 40), fill = "darkblue", text = "Mimí")
            self.ci = 0
            self.speedx = 9
            self.speedy = 9
            self.active = True
            self.move_active()
                
        def color_index(self):
            self.ci+=1
            if self.ci>8:
                self.ci = 0
                return self.ci

        def name_update(self):
                self.canva.move(self.shape, self.speedx, self.speedy)
                pos = self.canva.bbox(self.shape)                   
                if pos[2] >= 1500 or pos[0] <= 0:
                    self.speedx *= -1
                if pos[3] >= 768 or pos[1] <= 0:
                    self.speedy *= -1

        def move_active(self):
            if self.active:
                self.name_update()
                self.canva.after(40, self.move_active)

    

    def linea():
        canva3= Canvas(ventana, width=1500, height=768,bg="#F9F4A3")
        canva3.pack(expand=YES, fill=BOTH)

        def regresar():
            Principal()
                    
        regreso2 = Button(canva3, width =15, height=1, font=("Bahnschrift SemiBold SemiConden", 15), text="Regresar", command=regresar).place(x=670, y=700)
        
        line = Name(canva3)
        
        
    boton3 = Button(canvas_Personal, width =15, height=3, font=("Bahnschrift SemiBold SemiConden", 15), text="Animación", command = linea).place(x=630, y=630)

    ventana.mainloop()
start()
