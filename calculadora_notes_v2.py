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

Label(left_frame, text="Ejercicio 1:", bg=COLOR3, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), justify=RIGHT, width=10).grid(row=0, column=0)
Label(left_frame, text="Ejercicio 2:", bg=COLOR3, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), justify=RIGHT, width=10).grid(row=1, column=0)
Label(left_frame, text="Ejercicio 3:", bg=COLOR3, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), justify=RIGHT, width=10).grid(row=2, column=0)
Label(left_frame, text="Ejercicio 4:", bg=COLOR3, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), justify=RIGHT, width=10).grid(row=3, column=0)
Label(left_frame, text="Ejercicio 5:", bg=COLOR3, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), justify=RIGHT, width=10).grid(row=4, column=0)
Label(left_frame, text="Ejercicio 6:", bg=COLOR3, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), justify=RIGHT, width=10).grid(row=5, column=0)
Label(left_frame, text="Ejercicio 7:", bg=COLOR3, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), justify=RIGHT, width=10).grid(row=6, column=0)
Label(left_frame, text="Ejercicio 8:", bg=COLOR3, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), justify=RIGHT, width=10).grid(row=7, column=0)
Label(left_frame, text="Ejercicio 9:", bg=COLOR3, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), justify=RIGHT, width=10).grid(row=8, column=0)
Label(left_frame, text="Ejercicio 10:", bg=COLOR3, font=(TIPOGRAFIA, DIM_TIPO_SECUNDARIO), justify=RIGHT, width=10).grid(row=9, column=0)

Label(center_frame, text="Puntos max:", bg=COLOR1, font=(TIPOGRAFIA, DIM_TIPO_PRINCIPAL), justify=RIGHT, width=10).grid(row=0, column=0)
Label(center_frame, text="Nota sobre:", bg=COLOR1, font=(TIPOGRAFIA, DIM_TIPO_PRINCIPAL), justify=RIGHT, width=10).grid(row=1, column=0)

entrada_ej_1 = Entry(left_frame,
                font = (TIPOGRAFIA, DIM_TIPO_SECUNDARIO),
                width=3,
                justify=CENTER,
                bg=COLOR5,
                fg=COLOR_LETRA,
                )
entrada_ej_1.grid(row=0, column=1)

entrada_ej_2 = Entry(left_frame,
                font = (TIPOGRAFIA, DIM_TIPO_SECUNDARIO),
                width=3,
                justify=CENTER,
                bg=COLOR5,
                fg=COLOR_LETRA,
                )
entrada_ej_2.grid(row=1, column=1)
entrada_ej_3 = Entry(left_frame,
                font = (TIPOGRAFIA, DIM_TIPO_SECUNDARIO),
                width=3,
                justify=CENTER,
                bg=COLOR5,
                fg=COLOR_LETRA,
                )
entrada_ej_3.grid(row=2, column=1)
entrada_ej_4 = Entry(left_frame,
                font = (TIPOGRAFIA, DIM_TIPO_SECUNDARIO),
                width=3,
                justify=CENTER,
                bg=COLOR5,
                fg=COLOR_LETRA,
                )
entrada_ej_4.grid(row=3, column=1)
entrada_ej_5 = Entry(left_frame,
                font = (TIPOGRAFIA, DIM_TIPO_SECUNDARIO),
                width=3,
                justify=CENTER,
                bg=COLOR5,
                fg=COLOR_LETRA,
                )
entrada_ej_5.grid(row=4, column=1)
entrada_ej_6 = Entry(left_frame,
                font = (TIPOGRAFIA, DIM_TIPO_SECUNDARIO),
                width=3,
                justify=CENTER,
                bg=COLOR5,
                fg=COLOR_LETRA,
                )
entrada_ej_6.grid(row=5, column=1)
entrada_ej_7 = Entry(left_frame,
                font = (TIPOGRAFIA, DIM_TIPO_SECUNDARIO),
                width=3,
                justify=CENTER,
                bg=COLOR5,
                fg=COLOR_LETRA,
                )
entrada_ej_7.grid(row=6, column=1)
entrada_ej_8 = Entry(left_frame,
                font = (TIPOGRAFIA, DIM_TIPO_SECUNDARIO),
                width=3,
                justify=CENTER,
                bg=COLOR5,
                fg=COLOR_LETRA,
                )
entrada_ej_8.grid(row=7, column=1)
entrada_ej_9 = Entry(left_frame,
                font = (TIPOGRAFIA, DIM_TIPO_SECUNDARIO),
                width=3,
                justify=CENTER,
                bg=COLOR5,
                fg=COLOR_LETRA,
                )
entrada_ej_9.grid(row=8, column=1)
entrada_ej_10 = Entry(left_frame,
                font = (TIPOGRAFIA, DIM_TIPO_SECUNDARIO),
                width=3,
                justify=CENTER,
                bg=COLOR5,
                fg=COLOR_LETRA,
                )
entrada_ej_10.grid(row=9, column=1)

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

Button(center_frame, text="Calcular", font=(TIPOGRAFIA, 20), bg=COLOR3, command=lambda : calcular()).grid(row=3, column=0)
Label(center_frame, text="Nota final:", font=(TIPOGRAFIA, DIM_TIPO_PRINCIPAL), bg=COLOR1, justify="right").grid(row=2, column=0)
nota_final = Entry(center_frame, font = (TIPOGRAFIA, DIM_TIPO_PRINCIPAL), width= 4, bg=COLOR5)
nota_final.grid(row=2, column=1)

def calcular():
    nota_final.delete(0, END)
    total_ejer= total_ejer= int(entrada_ej_1.get())+int(entrada_ej_2.get())+int(entrada_ej_3.get())+int(entrada_ej_4.get())+int(entrada_ej_5.get())+int(entrada_ej_6.get())+int(entrada_ej_7.get())+int(entrada_ej_8.get())+int(entrada_ej_9.get())+int(entrada_ej_10.get())
    total = total_ejer*int(entrada_const.get())/int(entrada_nota_total.get())
    total =(f"{total:.2f}")
    nota_final.insert(0, total)



main.mainloop()