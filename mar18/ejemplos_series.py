import pandas as pd
import numpy as np

# Creación de Series en pandas

# 1. Crear una serie a partir de una lista
datos = [10, 20, 30, 40, 50]
s_lista = pd.Series(datos)
print("Serie a partir de una lista:")
print(s_lista)

# 2.Crear una serie a partir de una lista con un índice personalizado
s_indice = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print("\nSerie con índice personalizado:")
print(s_indice)

# 3. Crear una serie a partir de un diccionario
s_dict = pd.Series({'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50})
print("\nSerie a partir de un diccionario:")
print(s_dict)

# 4. Crear una serie a partir de un array de NumPy. Muy eficiente para grandes conjuntos de datos.
s_numpy = pd.Series(np.array([1.5, 2.5, 3.5, 4.5, 5.5]))
print("\nSerie a partir de un array de NumPy:")
print(s_numpy)
s_numpy2= pd.Series(np.arange(1, 6))
print("\nSerie a partir de un rango de números:")
print(s_numpy2)
s_numpy3 = pd.Series(np.random.random(size=5))
print("\nSerie a partir de números aleatorios:")
print(s_numpy3)

# 5. Crear una serie a partir de un escalar (un solo value). El value se repetirá para cada índice.
s_escalar = pd.Series(42, index=['a', 'b', 'c', 'd', 'e'])
print("\nSerie a partir de un escalar:")
print(s_escalar)


# Creación de series con diferentes tipos de datos
# 6. Crear una serie a partir de un rango de fechas. Muy útil para series temporales.
fechas = pd.date_range(start='2024-01-01', periods=5, freq='D')
s_fechas = pd.Series(fechas)
print("\nSerie a partir de un rango de fechas:")
print(s_fechas)

# 7. Crear una serie a partir de una lista de cadenas de texto.
s_cadenas = pd.Series(['Python', 'Pandas', 'Series', 'Data', 'Analysis'])
print("\nSerie a partir de una lista de cadenas de texto:") 
print(s_cadenas)

# 8. Crear una serie a partir de una lista de valores booleanos.
s_booleanos = pd.Series([True, False, True, False, True])
print("\nSerie a partir de una lista de valores booleanos:")
print(s_booleanos)

# 9. Crear una serie a partir de una lista de objetos mixtos (diferentes tipos de datos).
s_mixta = pd.Series([10, 'Python', 3.14, True, pd.Timestamp('2024-01-01')])
print("\nSerie a partir de una lista de objetos mixtos:")
print(s_mixta)

# 10. Serie con tipos de datos categóricos. Muy útil para variables categóricas (muy eficiente en memoria, con datos repetidos).
s_categorica = pd.Series(['A', 'B', 'A', 'C', 'B'], dtype='category')
print("\nSerie con tipos de datos categóricos:")
print(s_categorica)

# Manipulación de Series y operaciones matemáticas

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([10, 20, 30, 40, 50])

# Suma de dos series
s_suma = s1 + s2
print("\nSuma de dos series:")
print(s_suma)

# Multiplicación de una serie por un escalar
s_multiplicacion = s1 * 2
print("\nMultiplicación de una serie por un escalar:")
print(s_multiplicacion)

# Aplicar una función a cada elemento de la serie (por ejemplo, el cuadrado)
s_cuadrado = s1.apply(lambda x: x**2)
print("\nSerie con los elementos al cuadrado:")
print(s_cuadrado)

# Funciones estadísticas integradas en series de pandas
print("\nMedia de la serie s1:", s1.mean())
print("Desviación estándar de la serie s1:", s1.std())
print("Valor máximo de la serie s1:", s1.max())
print("Valor mínimo de la serie s1:", s1.min())
print("LA mediana de la serie s1:", s1.median())

datos_numericos = pd.Series([1, 2, 3, 4, 5])
print("La media de la serie de datos numéricos es:", datos_numericos.mean())

# Filtrado y manejos de datos nulos (faltantes, representados por NaN)
s_con_nulos = pd.Series([1, 2, np.nan, 4, 5])
print("\nSerie con datos nulos:")
print(s_con_nulos)
print("Valores no nulos:")
print(s_con_nulos.dropna())
print("¿Hay datos nulos en la serie?", s_con_nulos.isnull().any())
s_nulos = s_con_nulos.isna() # Devuelve una serie booleana indicando dónde hay datos nulos (True) y dónde no (False)
s_no_nulos = s_con_nulos.notna() # Devuelve una serie booleana indicando dónde no hay datos nulos (True) y dónde sí (False)
print("Máscara booleana para datos nulos:")
print(s_nulos)
print("Máscara booleana para datos no nulos:")
print(s_no_nulos)
print("\nSerie con datos nulos:")
print(s_con_nulos)
s_sin_nulos = s_con_nulos.dropna()
print("Serie sin datos nulos:")
print(s_sin_nulos)
s2 = pd.Series([10, 20, 30, 40, 50])
# Filtrado con condiciones (máscaras booleanas)
s_filtrada = s2[s2 > 25] # type: ignore
print("\nSerie filtrada (valores mayores que 25):")
print(s_filtrada)
# Dar valores por defecto a los datos nulos
s_con_nulos_rellenada = s_con_nulos.fillna(0)
print("Serie con datos nulos rellenados con 0:")
print(s_con_nulos_rellenada)

serie_numerica_grande_con_nulos = pd.Series(np.random.rand(1000))
serie_numerica_grande_con_nulos[::10] = np.nan # Introducimos NaN cada 10 elementos
print("\nSerie numérica grande con datos nulos:")
print(serie_numerica_grande_con_nulos)
print("Número de datos nulos en la serie:", serie_numerica_grande_con_nulos.isna().sum())
print("La media de la serie sin datos nulos es:", serie_numerica_grande_con_nulos.dropna().mean())
# Rellenar los datos nulos con la media de la serie
media_sin_nulos = serie_numerica_grande_con_nulos.dropna().mean()
s_rellenada = serie_numerica_grande_con_nulos.fillna(media_sin_nulos)
print("Serie con datos nulos rellenados con la media:")
print(s_rellenada)
print("Número de datos nulos en la serie:", s_rellenada.isna().sum())
print("La media de la serie sin datos nulos es:", s_rellenada.dropna().mean())

# Acceso y ordenamiento de datos en series
serie = pd.Series([5, 2, 9, 1, 3], index=['a', 'b', 'c', 'd', 'e'])
print("\nSerie original:")
print(serie)
print("Acceso a elementos por índice:")
print("Elemento con índice 'c':", serie['c'])
print("Elemento en la posición 2:", serie.iloc[2])
print("Elemento con índice 'c' utilizando loc:", serie.loc['c'])
print("Ordenar la serie por valores:")
print(serie.sort_values()) # Ordena la serie por sus valores (de menor a mayor)
print(serie.sort_values(ascending=False)) # Ordena la serie por sus valores (de mayor a menor)
print("Ordenar la serie por índice:")
print(serie.sort_index())
print(serie.sort_index(ascending=False)) # Ordena la serie por sus índices (de mayor a menor)
serie_diez_numeros = pd.Series([10, 2, 9, 1, 3, 5, 7, 8, 4, 6])
print("\nSerie de diez números:")
print(serie_diez_numeros)
print(serie_diez_numeros[[0, 2, 4]]) # Acceso a elementos específicos por posición
# Filtrado de elementos mayores que 5
print(serie_diez_numeros[serie_diez_numeros > 5]) # type: ignore        aazzzzzzzzz
print(serie_diez_numeros[:5]) # 5 primeros elementos de la serie
print(serie_diez_numeros[-5:]) # 5 últimos elementos de la serie

# Ejemplos prácticos con series de pandas
ventas = pd.Series([100, 150, 120, 250, 200], index=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'])
print("\nVentas mensuales:")
print(ventas)
print("Ventas totales:", ventas.sum())
print("Promedio de ventas:", ventas.mean())
ventas_acumuladas = ventas.cumsum() # Suma acumulada de las ventas
print("Ventas acumuladas:")
print(ventas_acumuladas)

serie_nombres = pd.Series(['  Alice García  ', ' Bob', 'Charlie García ', 'David', ' Eve '])
print("\nSerie de nombres:")
print(serie_nombres)
print("Nombres con espacios en blanco eliminados:")
print(serie_nombres.str.strip()) # Limpiar espacios en blanco al inicio y al final de cada nombre
serie_garcias = serie_nombres[serie_nombres.str.contains('García')] # Filtrar nombres que contienen "García" (sin importar mayúsculas/minúsculas)
print("Nombres que contienen 'García':")
print(serie_garcias)
serie_garcias2 = serie_nombres.str.contains('García')
print("Máscara booleana para nombres que contienen 'García':")
print(serie_garcias2)
serie_garcias3 = serie_nombres.str.replace('García', 'Garcia') # Reemplazar "García" por "Garcia" (le quita la tilde)
print("Nombres con 'García' reemplazado por 'Garcia':")
print(serie_garcias3)
textos = pd.Series(['Python es genial', 'Me gusta pandas', 'Las series son útiles'])
serie_separada = textos.str.split() # Separar cada texto en palabras (devuelve una serie de listas)
print("\nSerie de textos separados en palabras:")
print(serie_separada)

# Análisis de frecuencias y valores únicos en series de pandas
encuestas = pd.Series(['Sí', 'No', 'Sí', 'Sí', 'Tal vez', 'Sí', 'No'])
# frecuencia de cada respuesta (frecuencia absoluta)
frecuencia = encuestas.value_counts()
print("\nFrecuencia de cada respuesta:")
print(frecuencia)
# frecuencia relativa de cada respuesta (proporción)
frecuencia_relativa = encuestas.value_counts(normalize=True)*100
print("\nFrecuencia relativa de cada respuesta (%):")
print(frecuencia_relativa)
# valores únicos en la serie
valores_unicos = encuestas.unique()
print("\nValores únicos en la serie de encuestas:")
print(valores_unicos)
# número de valores únicos en la serie
num_valores_unicos = encuestas.nunique()
print("\nNúmero de valores únicos en la serie de encuestas:")
print(num_valores_unicos)
print("\nElementos de la serie:", encuestas.count()) # Número total de elementos en la serie (sin contar los nulos)

# Mapeo y transformación de datos en series de pandas
# Mapeo de valores utilizando un diccionario
s_categorias = pd.Series(["Bajo", "Medio", "Alto", "Medio", "Bajo"])
diccionario_mapeo = {"Bajo": 1, "Medio": 2, "Alto": 3}
s_mapeada = s_categorias.map(diccionario_mapeo) # Reemplaza cada valor de la serie según el diccionario de mapeo (si el valor no está en el diccionario, se asigna NaN). Muy útil para Machine Learning (preprocesamiento de datos).
print("\nSerie mapeada:")
print(s_mapeada)
# Reemplazo de valores utilizando el método replace
s_reemplazada = s_categorias.replace(["Bajo","Medio"], "No Alto") # Similar a map pero con más opciones (puede reemplazar varios valores a la vez, también con regex)
print("\nSerie con valores reemplazados:")
print(s_reemplazada)

# Detección y manejo de valores duplicados en series de pandas
s_duplicados = pd.Series([1, 2, 2, 3, 4, 4, 5])
print("\nSerie con valores duplicados:")
print(s_duplicados)
print("Valores duplicados en la serie:")
duplicados = s_duplicados[s_duplicados.duplicated()] # Devuelve los valores que están duplicados (aparece más de una vez)
print(duplicados)
sin_duplicados = s_duplicados.drop_duplicates() # Elimina los valores duplicados, dejando solo la primera aparición de cada valor
print("Serie sin valores duplicados:")
print(sin_duplicados)

# Tareas específicas con Fechas (.dt)
# Crear una serie de fechas con fechas de ejemplo
fechas = pd.Series(pd.to_datetime(['2023-01-01', '2026-02-15', '2025-03-30', '2024-04-10', '2024-05-20']))
s_anyos = fechas.dt.year # Extraer el año de cada fecha
print("\nAños extraídos de las fechas:")
print(s_anyos)
s_meses = fechas.dt.month_name(locale='es_ES') # Extraer el nombre del mes de cada fecha
print("\nMeses extraídos de las fechas:")
print(s_meses)
s_dias_semana = fechas.dt.day_of_week # 0= lunes, 1 = martes, ..., 6 = domingo
print("\nDías de la semana extraídos de las fechas:")
print(s_dias_semana)

# Agrupaciones en rangos (binning-límites/Discretización)
edades = pd.Series([15, 22, 48, 35, 14, 9, 85])
limites = [0, 18, 35, 60, 100] # Definimos los límites de los grupos de edad (0-18, 19-35, 36-60, 61-100)
etiquetas = ['Niño', 'Joven', 'Adulto', 'Anciano']
s_grupos_edad = pd.cut(edades, bins=limites, labels=etiquetas) # Asigna a cada edad una etiqueta según el grupo al que pertenece (si la edad no cae en ningún grupo, se asigna NaN)
print("\nGrupos de edad asignados a cada edad:")
print(s_grupos_edad)
