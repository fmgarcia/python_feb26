import pandas as pd
import numpy as np

semilla = 42
np.random.seed(semilla)
# Crear una serie de números aleatorios entre 0 y 1
serie_aleatoria = pd.Series(np.random.random(size=6))
print("Serie de números aleatorios con semilla fija:")
print(serie_aleatoria)