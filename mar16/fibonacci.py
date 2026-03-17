def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
    


# Con programación dinámica: Guardamos los resultados de las llamadas anteriores para evitar cálculos repetidos.    
memoria = {0 : 0, 1 : 1}
def fibonacci_memorizado(n):
    if n in memoria: # Si el resultado ya está en la memoria, lo devuelve directamente.
        return memoria[n]
    else:
        memoria[n] = fibonacci_memorizado(n - 1) + fibonacci_memorizado(n - 2)
        return memoria[n]
    
def fibonacci_memorizado_con_funcion(n, param_memoria={}):
    if n in param_memoria:
        return param_memoria[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        param_memoria[n] = fibonacci_memorizado_con_funcion(n - 1, param_memoria) + fibonacci_memorizado_con_funcion(n - 2, param_memoria)
        return param_memoria[n]

if __name__ == "__main__":
    n = 10
    resultado_recursivo = fibonacci_recursivo(n)
    print(f"El {n}-ésimo número de Fibonacci (recursivo) es: {resultado_recursivo}")
    
    resultado_memorizado = fibonacci_memorizado(n)
    print(f"El {n}-ésimo número de Fibonacci (memorizado) es: {resultado_memorizado}")
    
    resultado_memorizado_con_funcion = fibonacci_memorizado_con_funcion(n)
    print(f"El {n}-ésimo número de Fibonacci (memorizado con función) es: {resultado_memorizado_con_funcion}")