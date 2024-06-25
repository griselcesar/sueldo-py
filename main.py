from tkinter import *
from tkinter import ttk #importamos esta librería para usar el ComboBox
from tkinter.messagebox import * #importamos los MessageBox

root = Tk()
root.title("Calcular Sueldo")
root.iconbitmap('./assets/img/favicon.ico')
root.geometry("300x360")
root.resizable(0,0)

# Se establecen las constantes
CARGOS = ["DOCENTE","ADMINISTRATIVO","OBRERO","VIGILANTE"]
SUELDOS = [250,212,130,180]
TURNOS = ["DIURNO","NOCTURNO"]
BONO_NOCTURNO = 0.45 # Esto es equivalente al 45% de cualquier monto
HORA_EXTRA = 40

logo = PhotoImage(file="./assets/img/Icon.png")
bills = PhotoImage(file="./assets/img/Report.png")

#Estilos comunes entre widgets
fuente_general = ["Roboto",10]
fuente_títulos = ["Roboto",12,"bold"]
fuente_header = ["Roboto",10,"bold"]

#Función auxiliar para obtener el sueldo según su cargo
def obtener_sueldo_base(cargo):
  match cargo:
    case "DOCENTE":
      return SUELDOS[0]
    case "ADMINISTRATIVO":
      return SUELDOS[1]
    case "OBRERO":
      return SUELDOS[2]
    case "VIGILANTE":
      return SUELDOS[3]

#Función encargada de validar y Realizar los cálculos salariales
def calcular_sueldo():

  cargo = cargo_seccionado.get()
  turno = turno_seccionado.get()
  extras_str = horas_extras.get()
  

  sueldo_base = 0
  pago_horas_nocturnas = 0
  pago_horas_extras = 0
  sueldo_neto = 0

  if not cargo or not turno or not extras_str:
    showinfo(title="Campos Requeridos",message="Debe llenar todos los campos")
    return
    
  extras = int(extras_str)

  sueldo_base = obtener_sueldo_base(cargo)
  #showinfo(title="Sueldo",message=f"Su sueldo como {cargo} es {sueldo_base}")

  if turno == TURNOS[1]:
    pago_horas_nocturnas = sueldo_base * BONO_NOCTURNO
    #showinfo(title="Bono Nocturno",message=f"Tienes un Bono Nocturno por {pago_horas_nocturnas}")
  
  if extras > 0:
    pago_horas_extras = extras * HORA_EXTRA
    #showinfo(title="Horas Extras",message=f"Tienes una asignación por horas extras de {pago_horas_extras}")
  
  sueldo_neto = sueldo_base + pago_horas_nocturnas + pago_horas_extras
  #showinfo(title="Total a Pagar",message=f"Su sueldo neto es {sueldo_neto}")
  
  reporte = Toplevel()
  reporte.title("Recibo de Pago")
  reporte.resizable(0,0)
  reporte.iconbitmap('./assets/img/favicon.ico')
  reporte.geometry("300x360")

  report_frame = LabelFrame(reporte,text="Resumen de Pago",labelanchor="n",font=fuente_títulos,padx=10,pady=20)
  report_frame.grid(row=1,column=1,padx=5,pady=5)

  total_frame = LabelFrame(reporte,text="Total a Cancelar",labelanchor="n",font=fuente_títulos,padx=10,pady=20)
  total_frame.grid(row=1,column=2,padx=5,pady=5)

  Label(report_frame,text="Tipo de Empleado",font=fuente_header).pack()
  Label(report_frame,text=cargo,fg="#c92c2c",font=fuente_header).pack()

  Label(report_frame,text="Sueldo Base",font=fuente_header).pack()
  Label(report_frame,text=f"$ {sueldo_base}",fg="#5c483a",font=["Roboto",12,"bold"]).pack()
  
  Label(report_frame,text="Turno",font=fuente_header).pack()
  Label(report_frame,text=turno, fg="#6743a5",font=fuente_header).pack()

  Label(report_frame,text="Bono Nocturno",font=fuente_header).pack()
  Label(report_frame,text=f"$ {pago_horas_nocturnas}",fg="#2d6073",font="Roboto 12 bold").pack()

  Label(report_frame,text="Horas Extras",font=fuente_header).pack()
  Label(report_frame,text=extras,fg="#d39679",font=["Roboto",12,"bold"]).pack()

  Label(report_frame,text="Monto Horas Extras",font=fuente_header).pack()
  Label(report_frame,text=f"$ {pago_horas_extras}",fg="#10898b",font=["Roboto",12,"bold"]).pack()

  Label(total_frame,image=bills).pack()
  Label(total_frame,text="Sueldo Neto",font=fuente_header).pack()
  Label(total_frame,text=f"$ {sueldo_neto}",fg="#10898b",font=["Roboto",14,"bold"]).pack(pady=5)
  Button(total_frame,text="Aceptar",command=reporte.destroy,bg="#ff7f2a",font=fuente_header,fg="#fff").pack(ipadx=15)





main_frame = LabelFrame(root,text="Asignación de Pago",labelanchor="n",font=fuente_títulos)
main_frame.pack(ipadx=25,ipady=40,padx=40,pady=10)

Label(main_frame,image=logo).pack()


Label(main_frame,text="Tipo de Personal",font=fuente_header).pack(pady=5)
cargo_seccionado = ttk.Combobox(main_frame,state="readonly",values=CARGOS,font=fuente_general)
cargo_seccionado.pack()

Label(main_frame,text="Turno Laboral",font=fuente_header).pack(pady=5)
turno_seccionado = ttk.Combobox(main_frame,state="readonly",values=TURNOS,font=fuente_general)
turno_seccionado.pack()

Label(main_frame,text="Horas Extras:",font=fuente_header).pack(pady=5)
horas_extras = Entry(main_frame,justify="center",font=fuente_general)
horas_extras.pack()

Button(main_frame,text="Calcular Sueldo",command=calcular_sueldo, bg="#fc0",padx=40,pady=5,font=fuente_header).pack(pady=10)
Button(main_frame,text="Salir",command=root.destroy,bg="#be4c54",pady=5,padx=40,font=fuente_header,fg="#fff").pack()



mainloop()