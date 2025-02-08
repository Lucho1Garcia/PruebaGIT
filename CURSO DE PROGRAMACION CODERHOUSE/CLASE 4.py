'''
Escribir un programa que indique la generación correspondiente para un año de nacimiento indicado.
Importante: Para los años que no pertenezcan a ninguna generación, se deberá colocar: “No existe generación asociada”
1920 1940 Generacion Silenciosa
1946 1964 Baby Boomer
1965 1979 Generacion X
1980 2000 Generacion Y
2001 2010 Generacion Z
'''

'''
dato =int(input("ingrese su año de nacimiento:"))
if dato >= 1920 and dato <= 1940:
    print("Generacion Silenciosa")
elif dato >= 1946 and dato <= 1964:
    print("Baby Boomer")
elif dato >= 1965 and dato <= 1979:
    print("Generacion X")
elif dato >= 1980 and dato <= 2000:
    print("Generacion Y")
elif dato >= 2001 and dato <= 2010:
    print("Generacion Z")
else:
    print("No existe generacion asociada")
''' 
    
    
'''   
    Escribir un programa que indique la categoría de edad de una persona en función de su edad ingresada.
Importante: Para las edades que no pertenezcan a ninguna categoría definida, se deberá colocar: “Categoría no definida”.

0 a 12 años: Niño
13 a 17 años: Adolescente
18 a 35 años: Joven
36 a 60 años: Adulto
61 años en adelante: Adulto mayor
'''


'''
dato =int(input("ingrese su año de nacimiento:"))
if dato >= 0 and dato <= 12:
    print("Niño")
elif dato >= 13 and dato <= 7:
    print("Adolescente")
elif dato >= 18 and dato <= 35:
    print("Joven")
elif dato >= 36 and dato <= 60:
    print("Adulto")
elif dato >= 61:
    print("Adulto mayor")
else:
    print("Categoría no definida")

'''


'''
Para aprobar un crédito, el cliente debe ser mayor de edad. 
Además, debe tener una antigüedad en el sistema financiero de mínimo 3 años y un ingreso mayor a 2500 dólares.  
En caso no tenga la antigüedad suficiente, su ingreso mensual debe ser como mínimo 4000 dólares. 
Si no cumple ninguna de las condiciones, no se aprueba el crédito

edad = 15
antigüedad = 10
ingreso = 1500
'''

'''
edad = 15
antigüedad = 10
ingreso = 1500
'''
'''
edad = 18
antigüedad = 3
ingreso = 2500
'''

'''
edad = int(input("Ingrese su edad: "))
antigüedad = int(input("Ingrese su antigüedad en el sistema financiero (en años): "))
ingreso = int(input("Ingrese su ingreso mensual en dólares: "))
'''
'''
if edad <= 18:
    if antigüedad >= 3 and ingreso > 2500:
        print("Crédito aprobado.")
    elif antigüedad < 3 and ingreso >= 4000:
        print("Crédito aprobado por ingresos altos.")
    else:
        print("Crédito no aprobado.")
else:
    print("El cliente no es mayor de edad, crédito no aprobado.")
'''

'''
tomigay = input("¿el tomi es gay?:")

if tomigay == "si":
    print("el tomi es re gay")
elif tomigay == "no":
    print("es mentira loco, el tomi es re gay")
'''    
''' 
tatipiola = input("¿la tati es piola?:")
if tatipiola == "si":
    print("tenes razon maquina, es re piola la piba")
elif tatipiola == "no":
    print("chupala")
''' 
'''     
    Escribir una función a la que se le pase una cadena del nombre de una ciudad
y muestre por pantalla el saludo ¡hola bienvenidx a !.
''' 
'''
def ciudad (nombre):
    print(f"hola, bienvenido a {nombre}")
ciudad("San Juan")
'''




def calcular_media(lista_numeros):
    suma = sum(lista_numeros)  
    cantidad = len(lista_numeros)  
    return suma / cantidad  
resultado = calcular_media([10, 20, 30])
print(resultado)