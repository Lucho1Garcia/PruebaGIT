# Programa para calcular la nota final de un estudiante en el curso de Python

# Mensaje de bienvenida
print("¡Bienvenido al programa de cálculo de nota final de Coderhouse! Intentaremos hacerlo lo mejor posible")

# Mensaje intermedio
print("Necesitamos tus notas para calcular cuanto será tu promedio del curso")

# Solicitar al usuario que ingrese las tres notas
nota_1 = float(input("No la hagas larga e ingresa la primera nota wey (20%): "))
nota_2 = float(input("Dale papi apurate e ingresa la segunda nota cumpa (30%): "))
nota_3 = float(input("Capo dale manija e ingresa la tercera nota maquina (50%): "))

# Calcular la nota final usando los porcentajes dados
nota_final = (nota_1 * 0.2) + (nota_2 * 0.3) + (nota_3 * 0.5)

# Mensaje antes de mostrar la nota
print("En breve te mostraremos el resultado, no te vayas")

# Mostrar la nota final

print(f"Tu nota final del curso de Python es: {nota_final:.2f}! ")

if nota_final == 1:
    # Mensaje específico para nota 1
    print ("No puedes haberte equivocado tanto ponte a estudiar")
elif nota_final > 6:
    # Mensaje para notas mayores a 6
    print ("Felicitaciones! Aprobaste el curso")
else:
    # Mensaje para notas menores o iguales a 6 pero diferentes de 1
    print ("Desaprobaste pero no te desanimes")