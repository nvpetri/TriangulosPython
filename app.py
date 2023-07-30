import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.withdraw()

messagebox.showinfo("Tipos de Triângulo", "Vamos descobrir se você tem e qual é o triângulo de acordo com as informações inseridas!!")

ladoA = simpledialog.askinteger("Vamos lá...", "Qual o valor de A? ")
ladoB = simpledialog.askinteger("Continuando...", "Qual o valor de B? ")
ladoC = simpledialog.askinteger("Para finalizar...", "Qual o valor de C? ")

if ladoC < ladoA + ladoB and ladoB < ladoA + ladoC and ladoA < ladoB + ladoC:
    messagebox.showinfo("null", "Parabéns, você possui um triângulo!! \n Clique em OK para saber o tipo...")
    if ladoA == ladoB and ladoB == ladoC:
        messagebox.showinfo("null", "Este é um triângulo Equilátero!")
    elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
        messagebox.showinfo("null", "Este é um triângulo Isósceles!")
    else:
        messagebox.showinfo("null", "Este é um triângulo Escaleno!")
else:
    messagebox.showinfo("Poxa!", "Infelizmente os dados não equivalem a um triângulo!!")
