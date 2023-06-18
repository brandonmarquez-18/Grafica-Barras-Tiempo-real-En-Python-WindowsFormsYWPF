try:
    from tkinter import *

except:
    from Tkinter import *
from matplotlib import pyplot
principal = Tk()
principal.geometry("816x220")

Label(principal, text = "INGRESE LA CANTIDAD DE ALUMNOS PARA CADA CARRERA:", font = ("Arial", 14), fg="black").place(x=105, y=30)


#GRUPOS
vg1 = IntVar()
txtg1 = Entry(principal, textvariable = vg1, font = ("Verdana",14), width = 9)
txtg1.place(x = 85, y = 80)
Label(principal, text = "ISW", font = ("Arial", 14), fg="black").place(x=85, y=110)

vg2 = IntVar()
txtg2 = Entry(principal, textvariable = vg2, font = ("Verdana",14), width = 9)
txtg2.place(x = 255, y = 80)
Label(principal, text = "IBT", font = ("Arial", 14), fg="black").place(x=255, y=110)

vg3 = IntVar()
txtg3 = Entry(principal, textvariable = vg3, font = ("Verdana",14), width = 9)
txtg3.place(x = 425, y = 80)
Label(principal, text = "ILT", font = ("Arial", 14), fg="black").place(x=425, y=110)

vg4 = IntVar()
txtg4 = Entry(principal, textvariable = vg4, font = ("Verdana",14), width = 9)
txtg4.place(x = 595, y = 80)
Label(principal, text = "IMT", font = ("Arial", 14), fg="black").place(x=595, y=110)


btnGraficar = Button(principal, text = "Ver la gráfica...", font = ("Arial", 14), width = 56, height = 1, fg = "blue")
btnGraficar.place(x = 85, y = 150)

def Graficar(event):
    carreras = ["ISW", "IBT", "ILT", "IMT"]
    valores = [vg1.get(),vg2.get(),vg3.get(),vg4.get()]
    colores = ["blue","red","green","gray"]
    pyplot.title("Carreras")
    pyplot.bar(carreras, height=valores, color=colores, width=0.5)
    pyplot.ylabel("UPP")
    pyplot.show()

btnGraficar.bind("<Button-1>",Graficar)

principal.mainloop()
