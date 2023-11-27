# Calcular la nota de niños poniendo el número maximo de puntuación y la puntuación obtenida, al final poner el numero de de la puntuación del 0 al 10 truncando la nota

from tkinter import *



main=Tk()

# constantes

TIPOGRAFIA = "Helvetica"
DIM_TIPO_PRINCIPAL = 31
DIM_TIPO_SECUNDARIO = 15
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

# labels

left_frame = Frame(main, bg=COLOR1)
center_frame = Frame(main, bg=COLOR1)
right_frame = Frame(main, bg=COLOR1)
left_frame.grid(row=0, column=0)
center_frame.grid(row=0,column=1)
right_frame.grid(row=0,column=2)

# entradas

numero_ejercicios  = 5
entrada = []
for ejercicio in range(numero_ejercicios):
    Label(left_frame, text=f"Ejercicio {ejercicio+1}:", bg=COLOR1, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO)).grid(row=ejercicio, column=0)

    en = Entry(left_frame, bg = COLOR5, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO),fg=COLOR_LETRA, width=3, justify=CENTER)
    en.grid(row=ejercicio, column=1)
    entrada.append(en)

Label(center_frame, text="Puntos max:", bg=COLOR1, font=(TIPOGRAFIA, DIM_TIPO_PRINCIPAL), justify=RIGHT, width=10).grid(row=0, column=0, sticky=W)
Label(center_frame, text="Nota sobre:", bg=COLOR1, font=(TIPOGRAFIA, DIM_TIPO_PRINCIPAL), justify=RIGHT, width=10).grid(row=1, column=0, sticky=W)


entrada_nota_total = Entry(center_frame,
                font = (TIPOGRAFIA, DIM_TIPO_PRINCIPAL),
                width=4,
                justify=CENTER,
                bg=COLOR5,
                fg=COLOR_LETRA,
                )
entrada_nota_total.grid(row=0, column=1)

entrada_const = Entry(center_frame,
                font = (TIPOGRAFIA, DIM_TIPO_PRINCIPAL),
                width=4,
                justify=CENTER,
                bg=COLOR5,
                fg=COLOR_LETRA,
                )
entrada_const.grid(row=1, column=1)

# Checkbuttons




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

chk_2 = Checkbutton(center_frame,
                    bg=COLOR1,
                    command=des_lbl_3,
                    variable=chk_var_3,
                    onvalue=1,
                    offvalue=0,
                    )
chk_3 = Checkbutton(center_frame,
                    bg=COLOR1,
                    command=des_lbl_2,
                    variable=chk_var_2,
                    onvalue=1,
                    offvalue=0,
                    )

chk_2.grid(row=0, column=2)
chk_3.grid(row=1, column=2)

# calcular

Button(center_frame, text="Calcular", font=(TIPOGRAFIA, 20), bg=COLOR3, command=lambda : calcular()).grid(row=4, column=0)
Label(center_frame, text="Nota final:", font=(TIPOGRAFIA, DIM_TIPO_PRINCIPAL), bg=COLOR1, anchor="e", justify=LEFT).grid(row=3, column=0)
nota_final = Entry(center_frame, font = (TIPOGRAFIA, DIM_TIPO_PRINCIPAL), width= 4, bg=COLOR5)
nota_final.grid(row=3, column=1)
Label(center_frame, text="Puntuación:", font=(TIPOGRAFIA, DIM_TIPO_PRINCIPAL), bg=COLOR1, anchor="e", justify=LEFT).grid(row=2, column=0)
puntuacion = Entry(center_frame, font = (TIPOGRAFIA, DIM_TIPO_PRINCIPAL), width= 4, bg=COLOR5)
puntuacion.grid(row=2, column=1)

def calcular():
    nota_final.delete(0, END)
    puntuacion.delete(0, END)
    total_ejer = 0
    for nota in entrada:
        total_ejer = total_ejer + int(nota.get())
    total = total_ejer*int(entrada_const.get())/int(entrada_nota_total.get())
    total =(f"{total:.2f}")
    nota_final.insert(0, total)
    puntuacion.insert(0, total_ejer)



main.mainloop()