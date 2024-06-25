from tkinter import *
from tkinter import ttk #importamos esta librería para usar el ComboBox
from tkinter.messagebox import * #importamos los MessageBox

root = Tk()
root.title("Calcular Sueldo")
root.iconbitmap('./assets/img/favicon.ico')
root.geometry("500x300")
root.resizable(0,0)

# Se establecen las constantes
CARGOS = ["DOCENTE","ADMINISTRATIVO","OBRERO","VIGILANTE"]
SUELDOS = [250,212,130,180]
TURNOS = ["DIURNO","NOCTURNO"]
BONO_NOCTURNO = 0.45 # Esto es equivalente al 45% de cualquier monto
HORA_EXTRA = 40


#Estilos comunes entre widgets
fuente1 = ["Roboto",10,"bold"]

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
  showinfo(title="Sueldo",message=f"Su sueldo como {cargo} es {sueldo_base}")

  if turno == TURNOS[1]:
    pago_horas_nocturnas = sueldo_base * BONO_NOCTURNO
    showinfo(title="Bono Nocturno",message=f"Tienes un Bono Nocturno por {pago_horas_nocturnas}")
  
  if extras > 0:
    pago_horas_extras = extras * HORA_EXTRA
    showinfo(title="Horas Extras",message=f"Tienes una asignación por horas extras de {pago_horas_extras}")
  
  sueldo_neto = sueldo_base + pago_horas_nocturnas + pago_horas_extras
  showinfo(title="Total a Pagar",message=f"Su sueldo neto es {sueldo_neto}")
  return

cargo_seccionado = ttk.Combobox(root,state="readonly",values=CARGOS,font=fuente1)
cargo_seccionado.pack()

turno_seccionado = ttk.Combobox(root,state="readonly",values=TURNOS,font=fuente1)
turno_seccionado.pack()

horas_extras = Entry(root,justify="center",font=fuente1)
horas_extras.pack(pady=5)

Button(root,text="Calcular Sueldo",command=calcular_sueldo).pack()
Button(root,text="Salir",command=root.destroy).pack(pady=3,ipadx=10,ipady=3)



mainloop()