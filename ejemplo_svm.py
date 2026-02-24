# =============================================================================
# Ejemplo de algoritmo SVM (Support Vector Machine) - Máquina de Vectores de Soporte
# Clasificación del dataset Iris usando SVM
# =============================================================================

# Importamos numpy, la librería fundamental para cálculo numérico en Python
import numpy as np

# Importamos el dataset Iris, un conjunto de datos clásico con 3 especies de flores
from sklearn.datasets import load_iris

# Importamos train_test_split para dividir los datos en entrenamiento y prueba
from sklearn.model_selection import train_test_split

# Importamos SVC (Support Vector Classifier), la implementación de SVM para clasificación
from sklearn.svm import SVC

# Importamos StandardScaler para normalizar/escalar las características (mejora el rendimiento del SVM)
from sklearn.preprocessing import StandardScaler

# Importamos métricas para evaluar el rendimiento del modelo
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# -----------------------------------------------------------------------------
# 1. CARGA DE DATOS
# -----------------------------------------------------------------------------

# Cargamos el dataset Iris (150 muestras, 4 características, 3 clases)
iris = load_iris()

# X contiene las características (largo/ancho de sépalo y pétalo) - matriz de 150x4
X = iris.data

# y contiene las etiquetas/clases (0=setosa, 1=versicolor, 2=virginica) - vector de 150
y = iris.target

# Guardamos los nombres de las clases para mostrarlos después
nombres_clases = iris.target_names

# Guardamos los nombres de las características para referencia
nombres_caracteristicas = iris.feature_names

# Mostramos información básica del dataset
print("=" * 60)
print("EJEMPLO DE SVM - CLASIFICACIÓN DEL DATASET IRIS")
print("=" * 60)

# Mostramos la forma (dimensiones) de la matriz de características
print(f"\nForma del dataset: {X.shape}")  # (150, 4)

# Mostramos cuántas muestras hay de cada clase
print(f"Clases disponibles: {nombres_clases}")

# Mostramos los nombres de las 4 características medidas
print(f"Características: {nombres_caracteristicas}")

# -----------------------------------------------------------------------------
# 2. DIVISIÓN DE DATOS EN ENTRENAMIENTO Y PRUEBA
# -----------------------------------------------------------------------------

# Dividimos los datos: 80% para entrenar el modelo y 20% para probarlo
# random_state=42 asegura que la división sea reproducible (siempre la misma)
# stratify=y mantiene la proporción de clases en ambos conjuntos
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
    X, y,                   # Datos de entrada y etiquetas
    test_size=0.2,          # 20% de los datos para prueba
    random_state=42,        # Semilla para reproducibilidad
    stratify=y              # Mantiene la proporción de cada clase
)

# Mostramos cuántas muestras quedaron en cada conjunto
print(f"\nMuestras de entrenamiento: {X_entrenamiento.shape[0]}")
print(f"Muestras de prueba: {X_prueba.shape[0]}")

# -----------------------------------------------------------------------------
# 3. ESCALADO/NORMALIZACIÓN DE DATOS
# -----------------------------------------------------------------------------

# Creamos un escalador que transformará los datos para que tengan media=0 y desviación=1
# SVM es sensible a la escala de las características, por eso normalizamos
escalador = StandardScaler()

# fit_transform: primero aprende la media y desviación del conjunto de entrenamiento,
# luego transforma esos mismos datos
X_entrenamiento_escalado = escalador.fit_transform(X_entrenamiento)

# transform: usa la media y desviación aprendidas para transformar los datos de prueba
# (NO se hace fit de nuevo para evitar "data leakage" / fuga de datos)
X_prueba_escalado = escalador.transform(X_prueba)

# -----------------------------------------------------------------------------
# 4. CREACIÓN Y ENTRENAMIENTO DEL MODELO SVM
# -----------------------------------------------------------------------------

# Creamos el modelo SVM con los siguientes parámetros:
# - kernel='rbf': función de base radial (Gaussian), permite separar clases no lineales
# - C=1.0: parámetro de regularización (controla el equilibrio entre margen y errores)
#   Valores altos de C → menos errores pero posible sobreajuste
#   Valores bajos de C → margen más amplio pero más errores permitidos
# - gamma='scale': controla cuánta influencia tiene una sola muestra de entrenamiento
#   'scale' usa 1/(n_caracteristicas * varianza) como valor por defecto
modelo_svm = SVC(
    kernel='rbf',           # Kernel Gaussiano (el más usado)
    C=1.0,                  # Parámetro de regularización
    gamma='scale',          # Factor de influencia de cada muestra
    random_state=42         # Semilla para reproducibilidad
)

# Entrenamos el modelo con los datos de entrenamiento escalados
# El modelo aprende los "vectores de soporte" que definen los límites entre clases
modelo_svm.fit(X_entrenamiento_escalado, y_entrenamiento)

# Mostramos cuántos vectores de soporte encontró el modelo por cada clase
print(f"\nVectores de soporte por clase: {modelo_svm.n_support_}")

# Mostramos el número total de vectores de soporte
print(f"Total de vectores de soporte: {sum(modelo_svm.n_support_)}")

# -----------------------------------------------------------------------------
# 5. PREDICCIÓN Y EVALUACIÓN
# -----------------------------------------------------------------------------

# Usamos el modelo entrenado para predecir las clases de los datos de prueba
predicciones = modelo_svm.predict(X_prueba_escalado)

# Calculamos la precisión: porcentaje de predicciones correctas
precision = accuracy_score(y_prueba, predicciones)

# Mostramos la precisión del modelo (1.0 = 100% correcto)
print(f"\nPrecisión del modelo: {precision:.4f} ({precision*100:.2f}%)")

# -----------------------------------------------------------------------------
# 6. INFORME DETALLADO DE CLASIFICACIÓN
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("INFORME DE CLASIFICACIÓN")
print("=" * 60)

# classification_report muestra precisión, recall y f1-score por cada clase
# - Precision: de las que predijo como clase X, cuántas realmente lo eran
# - Recall: de las que eran clase X, cuántas identificó correctamente
# - F1-score: media armónica entre precision y recall
print(classification_report(
    y_prueba,                           # Etiquetas reales
    predicciones,                       # Etiquetas predichas
    target_names=nombres_clases         # Nombres legibles de las clases
))

# -----------------------------------------------------------------------------
# 7. MATRIZ DE CONFUSIÓN
# -----------------------------------------------------------------------------

# La matriz de confusión muestra cuántas muestras se clasificaron correcta e incorrectamente
# Las filas son las clases reales y las columnas son las predicciones
matriz = confusion_matrix(y_prueba, predicciones)

# Mostramos la matriz de confusión
print("MATRIZ DE CONFUSIÓN:")
print("-" * 40)

# Recorremos cada fila de la matriz para mostrarla con el nombre de la clase
for i, nombre in enumerate(nombres_clases):
    # Cada fila muestra cuántas muestras de esa clase fueron asignadas a cada categoría
    print(f"  {nombre:>12s}: {matriz[i]}")

# Explicación de cómo leer la matriz
print("\n(Filas = clase real, Columnas = clase predicha)")
print("Los valores en la diagonal son las predicciones correctas")

# -----------------------------------------------------------------------------
# 8. EJEMPLO DE PREDICCIÓN CON DATOS NUEVOS
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("PREDICCIÓN CON DATOS NUEVOS")
print("=" * 60)

# Creamos una muestra nueva ficticia con las 4 características de una flor
# [largo_sepalo, ancho_sepalo, largo_petalo, ancho_petalo] en centímetros
nueva_flor = np.array([[5.1, 3.5, 1.4, 0.2]])

# Escalamos la nueva muestra usando el mismo escalador que usamos con los datos de entrenamiento
nueva_flor_escalada = escalador.transform(nueva_flor)

# Predecimos la clase de la nueva flor
prediccion_nueva = modelo_svm.predict(nueva_flor_escalada)

# Mostramos las características de la flor introducida
print(f"\nCaracterísticas de la flor: {nueva_flor[0]}")

# Mostramos la clase predicha (convertimos el número a nombre)
print(f"Especie predicha: {nombres_clases[prediccion_nueva[0]]}")

# -----------------------------------------------------------------------------
# 9. COMPARACIÓN DE DIFERENTES KERNELS
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("COMPARACIÓN DE KERNELS")
print("=" * 60)

# Definimos una lista de kernels disponibles en SVM para compararlos
# - 'linear': separa las clases con un hiperplano recto (línea en 2D)
# - 'poly': usa funciones polinómicas para límites curvos
# - 'rbf': función de base radial, límites flexibles no lineales
# - 'sigmoid': similar a una red neuronal de una capa
kernels = ['linear', 'poly', 'rbf', 'sigmoid']

# Iteramos sobre cada tipo de kernel para comparar su rendimiento
for kernel in kernels:
    # Creamos un nuevo modelo SVM con el kernel actual
    modelo_temp = SVC(kernel=kernel, C=1.0, random_state=42)

    # Entrenamos el modelo con los datos de entrenamiento escalados
    modelo_temp.fit(X_entrenamiento_escalado, y_entrenamiento)

    # Predecimos con los datos de prueba
    pred_temp = modelo_temp.predict(X_prueba_escalado)

    # Calculamos la precisión de este kernel
    acc_temp = accuracy_score(y_prueba, pred_temp)

    # Mostramos el resultado de cada kernel con formato alineado
    print(f"  Kernel {kernel:>8s}: Precisión = {acc_temp:.4f} ({acc_temp*100:.2f}%)")

# Mensaje final
print("\n" + "=" * 60)
print("¡Ejemplo completado con éxito!")
print("=" * 60)
