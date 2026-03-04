from functools import reduce

def ejercicioQ3():
    palabras = ["hola", "mundo", "python", "programacion"]
    palabras_mayusculas = list(map(lambda palabra: palabra.upper(), palabras)) # Map para convertir cada palabra a mayúsculas
    print("Palabras en mayúsculas:", palabras_mayusculas)

def ejercicioQ4():
    numeros1al100 = list(range(1, 101)) # Lista de números del 1 al 100
    suma_con_reduce = reduce(lambda x, y: x + y, numeros1al100) # Suma de los números del 1 al 100 usando reduce
    print("Suma con reduce:", suma_con_reduce)
    
def ejercicioQ1pag218():
    scores = [100,90,95,90,80,70,0,80,90,90,0,90,100,75,20,30,50,90]
    
    # 1. Agrupas las notas por estudiante. Crearé una lista de listas, donde cada sublista contiene las notas de un estudiante (3 notas por estudiante)
    estudiantes = [scores[i:i+3] for i in range(0, len(scores), 3)]
    print("Notas agrupadas por estudiante:", estudiantes)
    # 2. Calcular el total de estudiantes.
    print("Estudiantes totales:", len(estudiantes))
    # 3. Filtras los estudiantes que no tienen un 0 en sus notas (se presentaron a todos los exámenes).
    estudiantes_completos = [estudiante for estudiante in estudiantes if 0 not in estudiante] # List comprehension para filtrar los estudiantes que no tienen un 0 en sus notas
    print("Estudiantes completos (sin ceros):", estudiantes_completos)
    # 4. Cantidad de estudiantes que se presentaron a todos los exámenes.
    print("Cantidad de estudiantes completos:", len(estudiantes_completos))
    
def ejercicioQ1pag218conPF():
    scores = [100,90,95,90,80,70,0,80,90,90,0,90,100,75,20,30,50,90]
    
    # 1. Agrupas las notas por estudiante. Crearé una lista de listas, donde cada sublista contiene las notas de un estudiante (3 notas por estudiante)
    estudiantes = list(map(lambda i: scores[i:i+3], range(0, len(scores), 3))) # Map para agrupar las notas por estudiante
    print("Notas agrupadas por estudiante:", estudiantes)
    # 2. Calcular el total de estudiantes.
    print("Estudiantes totales:", len(estudiantes))
    # 3. Filtras los estudiantes que no tienen un 0 en sus notas (se presentaron a todos los exámenes).
    estudiantes_completos = list(filter(lambda estudiante: 0 not in estudiante, estudiantes)) # Filter para filtrar los estudiantes que no tienen un 0 en sus notas
    print("Estudiantes completos (sin ceros):", estudiantes_completos)
    # 4. Cantidad de estudiantes que se presentaron a todos los exámenes.
    print("Cantidad de estudiantes completos:", len(estudiantes_completos))

#ejercicioQ3()
#ejercicioQ4()
#ejercicioQ1pag218()
ejercicioQ1pag218conPF()
