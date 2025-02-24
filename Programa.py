###
# programa en Python que permite ingresar el nombre de un estudiante
# y sus 5 notas. El programa calculará el promedio acumulado y
#  dirá si el estudiante está en riesgo (si el promedio es menor a 3.0).
# 
# ###

# Función para calcular el promedio
def calcular_promedio(notas):
    return sum(notas) / len(notas)
# Solicitar el nombre del estudiante
nombre = input("Ingresa el nombre del estudiante: ")

# Solicitar las 5 notas del estudiante
notas = []
for i in range(1, 6):
    nota = float(input(f"Ingrese la nota {i}: "))
    notas.append(nota)

# Calcular el promedio
promedio = calcular_promedio(notas)

# Mostrar el resultado
print(f"\nEstudiante: {nombre}")
print(f"Promedio: {promedio:.2f}")

# Verificar si está en riesgo
if promedio < 3.0:
    print("¡Este estudiante está en riesgo!")
else:
    print("¡El estudiante no está en riesgo!")