#py Programa para calcular la nota final de un estudiante en el curso de Python

# Mensaje de bienvenida
print("¡Bienvenido al programa de cálculo de nota final de Coderhouse!")

# Solicitar al usuario que ingrese las tres notas
nota_1 = float(input("Ingresa la primera nota (20%): "))
nota_2 = float(input("Ingresa la segunda nota (30%): "))
nota_3 = float(input("Ingresa la tercera nota (50%): "))

# Calcular la nota final usando los porcentajes dados
nota_final = (nota_1 * 0.2) + (nota_2 * 0.3) + (nota_3 * 0.5)

# Mostrar la nota final
print(f"Tu nota final del curso de Python es: {nota_final:.2f}")
