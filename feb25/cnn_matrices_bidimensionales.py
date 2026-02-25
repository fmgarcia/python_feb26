# CNN - Red Neuronal Convolucional
# Entrenamiento con dataset MNIST (dígitos escritos a mano)
# Relacionando la estructura de capas con matrices bidimensionales

import numpy as np
import random

# ============================================================
# SIMULACIÓN DE DATOS (Matrices bidimensionales = imágenes)
# ============================================================
# Cada imagen es una MATRIZ BIDIMENSIONAL de filas x columnas
# igual que la matriz que generamos con números aleatorios

filas = 28       # píxeles de altura
columnas = 28    # píxeles de anchura
num_muestras = 100

print(f"Cada imagen es una matriz de {filas} filas x {columnas} columnas")
print(f"Igual que nuestra matriz aleatoria:\n")

# Generamos una imagen de ejemplo como matriz bidimensional (igual que el notebook)
imagen_ejemplo = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = random.randint(0, 255)  # Valor de píxel entre 0 y 255
        fila.append(valor)
    imagen_ejemplo.append(fila)

print("Fragmento de la imagen (primeras 5 filas y 5 columnas):")
for i in range(5):
    for j in range(5):
        print(f"{imagen_ejemplo[i][j]:4}", end=' ')
    print()

print("\n" + "="*60)
print("ESTRUCTURA DE LA RED NEURONAL CONVOLUCIONAL (CNN)")
print("="*60)

# ============================================================
# BLOQUE PRINCIPAL: ESTRUCTURA DE CAPAS DE LA CNN
# ============================================================
# Aquí se define la arquitectura (las "capas" de neuronas)
# Cada capa transforma la matriz bidimensional de entrada

try:
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras import layers

    # --- INICIO DE LA ESTRUCTURA DE CAPAS ---
    modelo = keras.Sequential([

        # CAPA 1 - Input + Primera Convolución
        # Recibe la imagen como matriz 2D de 28 filas x 28 columnas x 1 canal
        # Aplica 32 filtros de 3x3 → detecta bordes y texturas básicas
        layers.Conv2D(
            filters=32,
            kernel_size=(3, 3),   # Ventana 3x3 que recorre la matriz
            activation='relu',
            input_shape=(filas, columnas, 1),
            name="capa_conv_1"
        ),

        # CAPA 2 - MaxPooling (Reducción de la matriz)
        # Reduce la matriz a la mitad: de 26x26 → 13x13
        # Conserva solo el valor máximo de cada ventana 2x2
        layers.MaxPooling2D(
            pool_size=(2, 2),     # Ventana 2x2 sobre la matriz
            name="capa_pooling_1"
        ),

        # CAPA 3 - Segunda Convolución
        # Ahora detecta patrones más complejos (curvas, formas)
        # La matriz se reduce a 11x11 con 64 filtros
        layers.Conv2D(
            filters=64,
            kernel_size=(3, 3),
            activation='relu',
            name="capa_conv_2"
        ),

        # CAPA 4 - Segundo MaxPooling
        # Reduce la matriz de 11x11 → 5x5
        layers.MaxPooling2D(
            pool_size=(2, 2),
            name="capa_pooling_2"
        ),

        # CAPA 5 - Flatten (Aplanado)
        # Convierte la matriz 2D (5x5x64) en un vector 1D de 1600 valores
        # Es el puente entre las capas convolucionales y las densas
        layers.Flatten(
            name="capa_aplanado"
        ),

        # CAPA 6 - Capa Densa (Fully Connected)
        # 128 neuronas que aprenden combinaciones de los patrones detectados
        layers.Dense(
            units=128,
            activation='relu',
            name="capa_densa_1"
        ),

        # CAPA 7 - Dropout (Regularización)
        # Desactiva el 50% de neuronas aleatoriamente para evitar sobreajuste
        layers.Dropout(
            rate=0.5,
            name="capa_dropout"
        ),

        # CAPA 8 - Capa de Salida
        # 10 neuronas → una por cada dígito (0 al 9)
        # Softmax convierte los valores en probabilidades
        layers.Dense(
            units=10,
            activation='softmax',
            name="capa_salida"
        )
    ])
    # --- FIN DE LA ESTRUCTURA DE CAPAS ---

    # Compilación del modelo
    modelo.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    print("\nResumen de la arquitectura CNN:")
    print("(Cómo se transforma la matriz 28x28 en cada capa)\n")
    modelo.summary()

    # ============================================================
    # ENTRENAMIENTO (usando datos reales de MNIST)
    # ============================================================
    print("\nCargando dataset MNIST...")
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    # Normalizar píxeles (de 0-255 a 0-1) y añadir dimensión de canal
    x_train = x_train.astype("float32") / 255.0
    x_test  = x_test.astype("float32") / 255.0
    x_train = np.expand_dims(x_train, -1)
    x_test  = np.expand_dims(x_test, -1)

    print(f"Forma de cada imagen de entrenamiento: {x_train[0].shape}")
    print(f"→ {x_train[0].shape[0]} filas x {x_train[0].shape[1]} columnas\n")

    print("Entrenando la CNN...")
    historial = modelo.fit(
        x_train, y_train,
        epochs=5,
        batch_size=64,
        validation_split=0.1,
        verbose=1
    )

    # ============================================================
    # EVALUACIÓN
    # ============================================================
    perdida, precision = modelo.evaluate(x_test, y_test, verbose=0)
    print(f"\nResultados finales:")
    print(f"  Pérdida  : {perdida:.4f}")
    print(f"  Precisión: {precision * 100:.2f}%")

except ImportError:
    print("\nTensorFlow no está instalado.")
    print("Instálalo con: pip install tensorflow\n")

    # ============================================================
    # EXPLICACIÓN DE CAPAS SIN TENSORFLOW
    # ============================================================
    print("EXPLICACIÓN DE LAS CAPAS (sin ejecutar el modelo):\n")

    capas = [
        ["Conv2D (32 filtros 3x3)",  "28x28", "26x26x32", "Detecta bordes y texturas"],
        ["MaxPooling2D (2x2)",        "26x26", "13x13x32", "Reduce la matriz a la mitad"],
        ["Conv2D (64 filtros 3x3)",  "13x13", "11x11x64", "Detecta formas complejas"],
        ["MaxPooling2D (2x2)",        "11x11", "5x5x64",   "Reduce la matriz otra vez"],
        ["Flatten",                   "5x5x64","1600",      "Convierte 2D a vector 1D"],
        ["Dense (128 neuronas)",      "1600",  "128",       "Aprende combinaciones"],
        ["Dropout (50%)",             "128",   "128",       "Evita sobreajuste"],
        ["Dense - Salida (10)",       "128",   "10",        "Probabilidad de cada dígito"],
    ]

    print(f"{'CAPA':<28} {'ENTRADA':<10} {'SALIDA':<10} {'FUNCIÓN'}")
    print("-" * 70)
    for capa in capas:
        print(f"{capa[0]:<28} {capa[1]:<10} {capa[2]:<10} {capa[3]}")

print("\n¡Entrenamiento completado!")