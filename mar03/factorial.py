def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
    
def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
    
print(factorial(10))  # Salida: 3628800
print(factorial_iterativo(10))  # Salida: 3628800