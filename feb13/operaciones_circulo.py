# la fórmula del área de un círculo es A = π * r^2, donde A es el área, π es una constante aproximadamente igual a 3.14159, y r es el radio del círculo.
# la fórmula de la circunferencia de un círculo es C = 2 * π * r, donde C es la circunferencia, π es una constante aproximadamente igual a 3.14159, y r es el radio del círculo.
PI = 3.14159 # constante para el valor de π
radio = float(input("Introduce el radio del círculo: ")) # radio del círculo
area = PI * (radio ** 2) # cálculo del área utilizando la fórmula A = π * r^2
circunferencia = 2 * PI * radio # cálculo de la circunferencia utilizando la fórmula C = 2 * π * r
print(f"El área del círculo con radio {radio} es: {area}") # imprime el área del círculo utilizando f-string para insertar las variables directamente en la cadena
print(f"La circunferencia del círculo con radio {radio} es: {circunferencia}") # imprime la circunferencia del círculo utilizando f-string para insertar las variables directamente en la cadena