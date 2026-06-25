#1. Ejercicio

# Preguntar los datos al usuario
cantidad = float(input("Ingrese la cantidad a invertir: "))
interes = float(input("Ingrese el interés anual (%): "))
años = int(input("Ingrese el número de años: "))
# Calcular el capital final
capital = cantidad * (1 + interes/100) ** años
# Mostrar el resultado redondeado a dos decimales
print(f"El capital obtenido en la inversión es: {capital:.2f}")

2.
# Definir los pesos de cada producto
peso_payaso = 112   # gramos
peso_muñeca = 75    # gramos
# Pedir al usuario la cantidad de cada producto
num_payasos = int(input("Ingrese el número de payasos vendidos: "))
num_muñecas = int(input("Ingrese el número de muñecas vendidas: "))
# Calcular el peso total
peso_total = (num_payasos * peso_payaso) + (num_muñecas * peso_muñeca)
# Mostrar el resultado
print(f"El peso total del paquete es: {peso_total} gramos")

# ---- #
#Bucles.

#3. 
# Pedir al usuario un número entero positivo
n = int(input("Ingrese un número entero positivo: "))
# Generar los números impares desde 1 hasta n
impares = []
for i in range(1, n+1):
    if i % 2 != 0:   # condición para que sea impar
        impares.append(str(i))  # convertir a texto para unir luego
# Mostrar los números separados por comas
print(", ".join(impares))

#4.
# Almacenar la contraseña en una variable
contraseña = "secreta"
# Pedir al usuario que ingrese la contraseña
entrada = input("Introduce la contraseña: ")
# Repetir hasta que sea correcta
while entrada != contraseña:
    print("Contraseña incorrecta, inténtalo de nuevo.")
    entrada = input("Introduce la contraseña: ")
print("¡Contraseña correcta! Acceso concedido.")

# -- -- #

#Pandas

#5. 
import pandas as pd

# Pedir al usuario el rango de años
inicio = int(input("Ingrese el año inicial: "))
fin = int(input("Ingrese el año final: "))
# Crear una lista de años
años = list(range(inicio, fin + 1))
# Pedir las ventas para cada año
ventas = []
for año in años:
    venta = float(input(f"Ingrese las ventas del año {año}: "))
    ventas.append(venta)
# Crear la serie con los datos de ventas
serie_ventas = pd.Series(ventas, index=años)
# Mostrar la serie original
print("\nVentas originales:")
print(serie_ventas)
# Aplicar descuento del 10%
serie_descuento = serie_ventas * 0.9
# Mostrar la serie con descuento
print("\nVentas con descuento del 10%:")
print(serie_descuento)

#6.

import pandas as pd

def resumen_notas(dic_notas):
    # Convertir el diccionario en una Serie de pandas
    serie_notas = pd.Series(dic_notas)
    # Calcular estadísticas
    resumen = pd.Series({
        "Nota mínima": serie_notas.min(),
        "Nota máxima": serie_notas.max(),
        "Nota media": serie_notas.mean(),
        "Desviación típica": serie_notas.std()
    })
    return resumen
# Ejemplo de uso
notas = {
    "Ana": 8.5,
    "Luis": 7.0,
    "María": 9.2,
    "Pedro": 6.8
}
print("Notas de los alumnos:")
print(pd.Series(notas))
print("\nResumen estadístico:")
print(resumen_notas(notas))

# - - - - #

#Matplotlib

#7. 

import matplotlib.pyplot as plt
# Preguntamos por el año inicial
inicio = int(input('Introduce el año inicial: '))
# Preguntamos por el año final
fin = int(input('Introduce el año final: '))
# Definimos un diccionario vacío para guardar las ventas de cada año
ventas = {}
# Bucle iterativo para preguntar las ventas de cada año y guardarlas en el diccionario
# i toma como valores los años desde el año de inicio hasta el año final
for i in range(inicio, fin+1):
    # Preguntamos por las ventas del año i y las guardamos en el diccionario con la clave el año y el valor las ventas
    ventas[i] = float(input('Introduce las ventas del año ' + str(i) +': '))
# Definimos la figura y los ejes del gráfico con Matplotlib
fig, ax = plt.subplots()
# Dibujamos la línea con las ventas a partir del diccionario
ax.plot(ventas.keys(), ventas.values())
# Mostarmos el gráfico por pantalla
plt.show()

"""
Ejercicios Solucion. 
-------
1: # Ejercicio 2: Tabla de multiplicar
num = int(input("Ingrese un número entero: "))

print(f"Tabla de multiplicar del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
-------
# Ejercicio 2: Número mayor
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

mayor = max(a, b, c)

print(f"El número mayor es: {mayor}")
"""
