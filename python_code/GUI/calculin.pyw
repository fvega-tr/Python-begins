
from tkinter import *

raiz=Tk()

raiz.title("¡¡CALCULÍN!!")

miFrame=Frame(raiz)

miFrame.pack()

operacion = ""
memoriaSuma = 0
memoriaResta = 0
memoriaMulti = 1
memoriaDivi = 1

#--------------------------PANTALLA-------------------------------

numeroPantalla=StringVar(value="0")

pantalla=Entry(miFrame,textvariable=numeroPantalla,width=35)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background="white",fg="green",justify="right")

#-------------------------PULSACIONES TECLADO---------------------

def numeroPulsado(num):
    if numeroPantalla.get() == "0" and num == "0":
        numeroPantalla.set("0")
    elif numeroPantalla.get() == "0" and num == ".":
        numeroPantalla.set("0.")
    elif numeroPantalla.get() == "0" and num != "0":
        numeroPantalla.set(num)
    else:
        if numeroPantalla.get().count(".") == 0:
            numeroPantalla.set(numeroPantalla.get() + num)
        elif numeroPantalla.get().count(".") >= 1 and num == ".":
            numeroPantalla.get()
        else:
            numeroPantalla.set(numeroPantalla.get() + num)

#------------------------BORRAR-----------------------------------

def borra():
    borrado = numeroPantalla.get()
    numeroPantalla.set(borrado[0:-1])
    
#----------------------------OPERACIONES--------------------------

def suma():
    global operacion
    global memoriaSuma
    global memoriaResta
    global memoriaMulti
    global memoriaDivi
    operacion = "suma"

    if memoriaResta == 0 and memoriaMulti == 1 and memoriaDivi == 1:
        memoriaSuma = memoriaSuma + float(numeroPantalla.get())
        numeroPantalla.set("0")
                
    else:
        if memoriaResta != 0:
            memoriaSuma = memoriaResta - float(numeroPantalla.get())
            numeroPantalla.set("0")
            memoriaResta = 0
        elif memoriaMulti != 1:
            memoriaSuma = memoriaMulti * float(numeroPantalla.get())
            numeroPantalla.set("0")
            memoriaMulti = 1
        else:
            memoriaSuma = memoriaDivi / float(numeroPantalla.get())
            numeroPantalla.set("0")
            memoriaDivi = 1
            
    print ("memoriaSuma ",memoriaSuma)
    print ("memoriaResta ",memoriaResta)
    print ("memoriaMulti ",memoriaMulti)
    print ("memoriaDivi ",memoriaDivi)
    
def resta():
    global operacion
    global memoriaResta
    global memoriaSuma
    global memoriaMulti
    global memoriaDivi
    operacion = "resta"

    if memoriaSuma == 0 and memoriaMulti == 1 and memoriaDivi == 1:
        if memoriaResta == 0:
            memoriaResta = float(numeroPantalla.get()) - memoriaResta
        else:
            memoriaResta = memoriaResta - float(numeroPantalla.get())

    else:
        if memoriaSuma != 0:
            memoriaResta = memoriaSuma + float(numeroPantalla.get())
            numeroPantalla.set("0")
            memoriaSuma = 0
        elif memoriaMulti != 1:
            memoriaResta = memoriaMulti * float(numeroPantalla.get())
            numeroPantalla.set("0")
            memoriaMulti = 1
        else:
            memoriaResta = memoriaDivi / float(numeroPantalla.get())
            numeroPantalla.set("0")
            memoriaDivi = 1
        
    numeroPantalla.set("0")
    
    print ("memoriaSuma ",memoriaSuma)
    print ("memoriaResta ",memoriaResta)
    print ("memoriaMulti ",memoriaMulti)
    print ("memoriaDivi ",memoriaDivi)
    

def multi():
    global operacion
    global memoriaMulti
    global memoriaSuma
    global memoriaResta
    global memoriaDivi
    operacion = "multi"
    
    if memoriaSuma == 0 and memoriaResta == 0 and memoriaDivi == 1:
        memoriaMulti = float(numeroPantalla.get()) * memoriaMulti
        numeroPantalla.set("0")
    else:
        if memoriaSuma != 0:
            memoriaMulti = memoriaSuma + float(numeroPantalla.get())
            numeroPantalla.set("0")
            memoriaSuma = 0
        elif memoriaResta != 0:
            memoriaMulti = memoriaResta - float(numeroPantalla.get())
            numeroPantalla.set("0")
            memoriaResta = 0
        else:
            memoriaMulti = memoriaDivi / float(numeroPantalla.get())
            numeroPantalla.set("0")
            memoriaDivi = 1
    
    print ("memoriaSuma ",memoriaSuma)
    print ("memoriaResta ",memoriaResta)
    print ("memoriaMulti ",memoriaMulti)
    print ("memoriaDivi ",memoriaDivi)

def divi():
    global operacion
    global memoriaDivi
    global memoriaSuma
    global memoriaResta
    global memoriaMulti
    operacion = "divi"

    if memoriaSuma == 0 and memoriaResta == 0 and memoriaMulti == 1:
        memoriaDivi = float(numeroPantalla.get()) / memoriaDivi
        numeroPantalla.set("0")
    else:
        if memoriaSuma != 0:
            memoriaDivi = memoriaSuma + float(numeroPantalla.get())
            numeroPantalla.set("0")
            memoriaSuma = 0
        elif memoriaResta != 0:
            memoriaDivi = memoriaResta - float(numeroPantalla.get())
            numeroPantalla.set("0")
            memoriaResta = 0
        else:
            memoriaDivi = memoriaMulti * float(numeroPantalla.get())
            numeroPantalla.set("0")
            memoriaMulti = 1
    
    print ("memoriaSuma ",memoriaSuma)
    print ("memoriaResta ",memoriaResta)
    print ("memoriaMulti ",memoriaMulti)
    print ("memoriaDivi ",memoriaDivi)

def igual():
    global operacion
    global memoriaSuma
    global memoriaResta
    global memoriaMulti
    global memoriaDivi
    
    if operacion == "suma":
        numeroPantalla.set(memoriaSuma + float(numeroPantalla.get()))
        memoriaSuma = 0
    elif operacion == "resta":
        numeroPantalla.set(memoriaResta - float(numeroPantalla.get()))
        memoriaResta = 0
    elif operacion == "multi":
        numeroPantalla.set(memoriaMulti * float(numeroPantalla.get()))
        memoriaMulti = 1
    else:
        numeroPantalla.set(memoriaDivi / float(numeroPantalla.get()))
        memoriaDivi = 1

    print ("memoriaSuma ",memoriaSuma)
    print ("memoriaResta ",memoriaResta)
    print ("memoriaMulti ",memoriaMulti)
    print ("memoriaDivi ",memoriaDivi)
        
#----------------------------FILA 1-------------------------------

boton7=Button(miFrame,text="7",width=9,height=3,background="grey",fg="white",command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text="8",width=9,height=3,background="grey",fg="white",command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text="9",width=9,height=3,background="grey",fg="white",command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=3)
botonDiv=Button(miFrame,text="/",width=9,height=3,background="white",command=lambda:divi())
botonDiv.grid(row=2,column=4)

#--------------------------FILA 2---------------------------------

boton4=Button(miFrame,text="4",width=9,height=3,background="grey",fg="white",command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1)
boton5=Button(miFrame,text="5",width=9,height=3,background="grey",fg="white",command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)
boton6=Button(miFrame,text="6",width=9,height=3,background="grey",fg="white",command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)
botonMult=Button(miFrame,text="X",width=9,height=3,background="white",command=lambda:multi())
botonMult.grid(row=3,column=4)

#---------------------------FILA 3-------------------------------

boton1=Button(miFrame,text="1",width=9,height=3,background="grey",fg="white",command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1)
boton2=Button(miFrame,text="2",width=9,height=3,background="grey",fg="white",command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)
boton3=Button(miFrame,text="3",width=9,height=3,background="grey",fg="white",command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3)
botonRest=Button(miFrame,text="-",width=9,height=3,background="white",command=lambda:resta())
botonRest.grid(row=4,column=4)

#---------------------------FILA 4---------------------------------

boton0=Button(miFrame,text="0",width=9,height=3,background="grey",fg="white",command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=1)
botonComa=Button(miFrame,text=".",width=9,height=3,background="yellow",command=lambda:numeroPulsado("."))
botonComa.grid(row=5,column=2)
botonIgual=Button(miFrame,text="=",width=9,height=3,background="green",command=lambda:igual())
botonIgual.grid(row=5,column=3)
botonSuma=Button(miFrame,text="+",width=9,height=3,background="white",command=lambda:suma())
botonSuma.grid(row=5,column=4)

#-----------------------------FILA 5-----------------------------------

botonBorra=Button(miFrame,text="BORRAR",width=18,height=3,fg="black",background="red",command=lambda:borra())
botonBorra.grid(row=6,column=2,columnspan=2,pady=10)


raiz.mainloop()

