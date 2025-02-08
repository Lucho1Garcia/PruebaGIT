'''
import tkinter as tk
from tkinter import messagebox

# Función para calcular la nota final y mostrar el mensaje
def calcular_nota():
    try:
        # Obtener las notas de las entradas
        nota1 = float(entry_nota1.get())
        nota2 = float(entry_nota2.get())
        nota3 = float(entry_nota3.get())
        
        # Calcular la nota final
        nota_final = (nota1 * 0.2) + (nota2 * 0.3) + (nota3 * 0.5)
        
        # Determinar el mensaje según la nota final
        if nota_final == 1:
            mensaje = "Nota exacta: 1. Necesitas mejorar mucho."
        elif nota_final > 6:
            mensaje = f"¡Aprobaste con una nota final de {nota_final:.2f}!"
        else:
            mensaje = f"No aprobaste. Tu nota final es {nota_final:.2f}."
        
        # Mostrar el mensaje en una ventana emergente
        messagebox.showinfo("Resultado", mensaje)
    except ValueError:
        # Mostrar un error si no se ingresaron números válidos
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos en todas las notas.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Nota Final")
ventana.geometry("400x300")
ventana.resizable(False, False)

# Etiquetas y campos de entrada para las notas
label_instruccion = tk.Label(ventana, text="Ingresa las notas y presiona calcular:", font=("Arial", 12))
label_instruccion.pack(pady=10)

frame_notas = tk.Frame(ventana)
frame_notas.pack(pady=10)

tk.Label(frame_notas, text="Nota 1 (20%):", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5)
entry_nota1 = tk.Entry(frame_notas, font=("Arial", 10))
entry_nota1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_notas, text="Nota 2 (30%):", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5)
entry_nota2 = tk.Entry(frame_notas, font=("Arial", 10))
entry_nota2.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_notas, text="Nota 3 (50%):", font=("Arial", 10)).grid(row=2, column=0, padx=5, pady=5)
entry_nota3 = tk.Entry(frame_notas, font=("Arial", 10))
entry_nota3.grid(row=2, column=1, padx=5, pady=5)

# Botón para calcular la nota
boton_calcular = tk.Button(ventana, text="Calcular Nota Final", font=("Arial", 12), bg="lightblue", command=calcular_nota)
boton_calcular.pack(pady=20)

# Iniciar el loop de la ventana
ventana.mainloop()

'''
'''
numero_correcto = 7
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (entre 1 y 10): "))
    
    if intento == numero_correcto:
        print("¡Correcto! Adivinaste el número.")
        adivinado = True
    else:
        print("Incorrecto. Intenta de nuevo.")
'''


for numero in range(1, 11):  # Números del 1 al 10
    if numero == 5:  # ¿Es el número 5?
        print("¡Número encontrado!")
        break  # Salir del bucle
    print(f"Buscando... (actual: {numero})")
