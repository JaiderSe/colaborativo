###
# programa en Python que permite ingresar el nombre de un estudiante
# y sus 5 notas. El programa calculará el promedio acumulado y
#  dirá si el estudiante está en riesgo (si el promedio es menor a 3.0).
# 
# ###

# Función para calcular el promedio
def calcular_promedio(notas):
    return sum(notas) / len(notas)
