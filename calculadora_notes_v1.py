# Calcular la nota de niños poniendo el número maximo de puntuación y la puntuación obtenida, al final poner el numero de de la puntuación del 0 al 10 truncando la nota

from tkinter import *



main=Tk()

# constantes

TIPOGRAFIA = "Helvetica"
DIM_TIPO_PRINCIPAL = 31
DIM_TIPO_SECUNDARIO = 19
COLOR1 = "#db5586"
COLOR2 = "#e46e9f"
COLOR3 = "#ed88b7"
COLOR4 = "#f6a1d0"
COLOR5 = "#ffbae8"
COLOR_LETRA ="Black"

# config general

main.configure(bg=COLOR1)
main.title("Calcula notas")
main.resizable(0,0)

# entradas

Label(text="Puntos:", bg=COLOR3, font=(TIPOGRAFIA, DIM_TIPO_PRINCIPAL), justify=RIGHT, width=10).grid(row=0, column=0)
Label(text="Puntos max:", bg=COLOR3, font=(TIPOGRAFIA, DIM_TIPO_PRINCIPAL), justify=RIGHT, width=10).grid(row=1, column=0)
Label(text="Nota sobre:", bg=COLOR3, font=(TIPOGRAFIA, DIM_TIPO_PRINCIPAL), justify=RIGHT, width=10).grid(row=2, column=0)

entrada_nota_alumno = Entry(main,
                font = (TIPOGRAFIA, DIM_TIPO_PRINCIPAL),
                width=3,
                justify=CENTER,
                bg=COLOR5,
                fg=COLOR_LETRA,
                )
entrada_nota_alumno.grid(row=0, column=1)

entrada_const = Entry(main,
                font = (TIPOGRAFIA, DIM_TIPO_PRINCIPAL),
                width=3,
                justify=CENTER,
                bg=COLOR5,
                fg=COLOR_LETRA,
                )
entrada_const.grid(row=2, column=1)

entrada_nota_total = Entry(main,
                font = (TIPOGRAFIA, DIM_TIPO_PRINCIPAL),
                width=3,
                justify=CENTER,
                bg=COLOR5,
                fg=COLOR_LETRA,
                )
entrada_nota_total.grid(row=1, column=1)

# Checkbuttons

def des_lbl_1():
    if chk_var_1.get() == 1:
        entrada_nota_alumno.configure(state= "disabled")
    else:
        entrada_nota_alumno.configure(state="normal")


def des_lbl_2():
    if chk_var_2.get() == 1:
        entrada_const.configure(state= "disabled")
    else:
        entrada_const.configure(state="normal")


def des_lbl_3():
    if chk_var_3.get() == 1:
        entrada_nota_total.configure(state= "disabled")
    else:
        entrada_nota_total.configure(state="normal")


chk_var_1 = IntVar()
chk_var_2 = IntVar()
chk_var_3 = IntVar()
chk_1 = Checkbutton(bg=COLOR1,
                    command=des_lbl_1,
                    variable=chk_var_1,
                    onvalue=1,
                    offvalue=0,
                    )
chk_2 = Checkbutton(bg=COLOR1,
                    command=des_lbl_3,
                    variable=chk_var_3,
                    onvalue=1,
                    offvalue=0,
                    )
chk_3 = Checkbutton(bg=COLOR1,
                    command=des_lbl_2,
                    variable=chk_var_2,
                    onvalue=1,
                    offvalue=0,
                    )
chk_1.grid(row=0, column=2)
chk_2.grid(row=1, column=2)
chk_3.grid(row=2, column=2)

# calcular

Button(text="Calcular", font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), bg=COLOR3, command=lambda : calcular()).grid(row=2, column=3)
Label(text="Nota final", font=(TIPOGRAFIA, DIM_TIPO_PRINCIPAL), bg=COLOR1).grid(row=0, column=3)
nota_final = Entry(main, font = (TIPOGRAFIA, DIM_TIPO_PRINCIPAL), width= 10, bg=COLOR5)
nota_final.grid(row=1, column=3)

def calcular():
    nota_final.delete(0, END)
    total = int(entrada_nota_alumno.get())*int(entrada_const.get())/int(entrada_nota_total.get())
    total =(f"{total:.2f}")
    nota_final.insert(0, total)



main.mainloop()