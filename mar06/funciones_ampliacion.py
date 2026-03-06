def func(a, b, /, c): # Uso de parámetros SOLO POSICIONALES a la izquierda de la barra (/). A la derecha de la barra, los parámetros pueden ser posicionales o por nombre.
    pass

def func2(a, b, *, c): # Uso de parámetros SOLO POR NOMBRE a la derecha del asterisco (*). A la izquierda del asterisco, los parámetros pueden ser posicionales o por nombre.
    pass

def func3(a, b, /, c, *, d, e): # Uso combinado de parámetros SOLO POSICIONALES a la izquierda de la barra (/) y SOLO POR NOMBRE a la derecha del asterisco (*). Esto permite una mayor flexibilidad en la forma en que se pueden pasar los argumentos a la función, ya que algunos argumentos deben ser pasados por posición y otros deben ser pasados por nombre, lo que puede mejorar la claridad y la legibilidad del código al hacer explícito cómo se deben proporcionar los argumentos al llamar a la función.
    pass

def func4(*args): # Parámetro *args para aceptar un número variable de argumentos posicionales. Esto permite que la función func4 pueda recibir cualquier cantidad de argumentos posicionales, los cuales se almacenan en una tupla llamada args dentro de la función. Esto es útil cuando no se sabe de antemano cuántos argumentos se van a pasar a la función, o cuando se desea permitir una cantidad flexible de argumentos sin tener que definir un número fijo de parámetros en la función.
    return sum(args) # Devuelve la suma de todos los argumentos posicionales recibidos, utilizando la función sum() para calcular la suma de los elementos en la tupla args. Esto permite que la función func4 realice una operación de suma sobre un número variable de argumentos posicionales, lo que puede ser útil en situaciones donde se desea realizar cálculos o agregaciones sobre una cantidad flexible de datos sin tener que definir un número fijo de parámetros en la función.

def func5(**kwargs): # Parámetro **kwargs para aceptar un número variable de argumentos por nombre. Esto permite que la función func5 pueda recibir cualquier cantidad de argumentos por nombre, los cuales se almacenan en un diccionario llamado kwargs dentro de la función. Esto es útil cuando no se sabe de antemano cuántos argumentos por nombre se van a pasar a la función, o cuando se desea permitir una cantidad flexible de argumentos por nombre sin tener que definir un número fijo de parámetros en la función.
    for key, value in kwargs.items(): # Itera sobre los pares clave-valor en el diccionario kwargs utilizando el método items(), lo que permite acceder tanto a las claves como a los valores de los argumentos por nombre recibidos en la función func5. Esto es útil para procesar o manipular los argumentos por nombre de manera dinámica dentro de la función, ya que se pueden realizar operaciones específicas basadas en las claves y valores proporcionados por el usuario al llamar a la función.
        print(f"{key}: {value}") # Imprime cada par clave-valor del diccionario kwargs utilizando f-string para formatear la salida de manera legible. Esto permite mostrar claramente los argumentos por nombre recibidos en la función func5, lo que puede ser útil para depurar o verificar los datos proporcionados por el usuario al llamar a la función.

def func6(fijo, *args, **kwargs):
    pass

func(1, 2, c=3)
func2(1, 2, c=3)
func3(1, 2, c=3, d=4, e=5)
func4(1, 2, 3, 4) 
func5(nombre="Alice", edad=30, ciudad="Madrid")
func6(fijo=1)
func6(1)
func6(1, 2, 3, nombre="Alice", edad=30)