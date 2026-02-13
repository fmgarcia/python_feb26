"""
Aplicación de consola: Operaciones geométricas básicas y avanzadas.

Este script implementa una calculadora de geometría con enfoque modular:
1) Módulo de utilidades de entrada/salida y validación.
2) Módulo de fórmulas geométricas (2D y 3D).
3) Módulo de casos de uso (acciones del menú).
4) Módulo de presentación (menú interactivo por consola).

Se prioriza claridad, mantenibilidad y separación de responsabilidades,
siguiendo una estructura profesional en un único archivo .py.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable, Dict, List, Tuple


# ============================================================
# MÓDULO 1: UTILIDADES DE ENTRADA/SALIDA Y VALIDACIÓN
# ============================================================
# Este bloque encapsula toda la interacción de lectura segura
# con el usuario (números positivos y selección de menú).

def pedir_flotante_positivo(mensaje: str) -> float:
	"""Solicita un número real positivo y valida la entrada."""
	while True:
		valor_str = input(mensaje).strip().replace(",", ".")
		try:
			valor = float(valor_str)
			if valor <= 0:
				print("⚠️  El valor debe ser mayor que 0. Inténtalo de nuevo.")
				continue
			return valor
		except ValueError:
			print("⚠️  Entrada no válida. Escribe un número (ej. 12.5).")


def pedir_opcion_valida(opciones_validas: List[str]) -> str:
	"""Solicita una opción al usuario y comprueba que sea válida."""
	opciones_set = set(opciones_validas)
	while True:
		opcion = input("Selecciona una opción: ").strip()
		if opcion in opciones_set:
			return opcion
		print("⚠️  Opción no válida. Vuelve a intentarlo.")


def imprimir_resultados(titulo: str, resultados: Dict[str, float]) -> None:
	"""Muestra resultados formateados con 4 decimales."""
	print(f"\n--- {titulo} ---")
	for nombre_operacion, valor in resultados.items():
		print(f"{nombre_operacion}: {valor:.4f}")
	print("-" * (len(titulo) + 8))


# ============================================================
# MÓDULO 2: FÓRMULAS GEOMÉTRICAS
# ============================================================
# Este bloque concentra exclusivamente las fórmulas matemáticas.
# No contiene lógica de menú ni lectura de datos.

class Geometria2D:
	"""Fórmulas de figuras planas (2D)."""

	@staticmethod
	def cuadrado(lado: float) -> Dict[str, float]:
		return {
			"Área": lado**2,
			"Perímetro": 4 * lado,
		}

	@staticmethod
	def rectangulo(base: float, altura: float) -> Dict[str, float]:
		return {
			"Área": base * altura,
			"Perímetro": 2 * (base + altura),
		}

	@staticmethod
	def triangulo(base: float, altura: float, lado1: float, lado2: float) -> Dict[str, float]:
		return {
			"Área": (base * altura) / 2,
			"Perímetro": base + lado1 + lado2,
		}

	@staticmethod
	def circulo(radio: float) -> Dict[str, float]:
		return {
			"Área": math.pi * radio**2,
			"Circunferencia": 2 * math.pi * radio,
		}

	@staticmethod
	def rombo(diagonal_mayor: float, diagonal_menor: float, lado: float) -> Dict[str, float]:
		return {
			"Área": (diagonal_mayor * diagonal_menor) / 2,
			"Perímetro": 4 * lado,
		}

	@staticmethod
	def trapecio(base_mayor: float, base_menor: float, altura: float, lado1: float, lado2: float) -> Dict[str, float]:
		return {
			"Área": ((base_mayor + base_menor) * altura) / 2,
			"Perímetro": base_mayor + base_menor + lado1 + lado2,
		}


class Geometria3D:
	"""Fórmulas de sólidos geométricos (3D)."""

	@staticmethod
	def cubo(lado: float) -> Dict[str, float]:
		return {
			"Área total": 6 * lado**2,
			"Volumen": lado**3,
		}

	@staticmethod
	def prisma_rectangular(largo: float, ancho: float, alto: float) -> Dict[str, float]:
		return {
			"Área total": 2 * (largo * ancho + largo * alto + ancho * alto),
			"Volumen": largo * ancho * alto,
		}

	@staticmethod
	def cilindro(radio: float, altura: float) -> Dict[str, float]:
		return {
			"Área lateral": 2 * math.pi * radio * altura,
			"Área total": 2 * math.pi * radio * (radio + altura),
			"Volumen": math.pi * radio**2 * altura,
		}

	@staticmethod
	def esfera(radio: float) -> Dict[str, float]:
		return {
			"Área": 4 * math.pi * radio**2,
			"Volumen": (4 / 3) * math.pi * radio**3,
		}

	@staticmethod
	def cono(radio: float, altura: float, generatriz: float) -> Dict[str, float]:
		return {
			"Área lateral": math.pi * radio * generatriz,
			"Área total": math.pi * radio * (radio + generatriz),
			"Volumen": (math.pi * radio**2 * altura) / 3,
		}


# ============================================================
# MÓDULO 3: CASOS DE USO (ACCIONES DEL MENÚ)
# ============================================================
# Cada función de este bloque representa una acción concreta
# que orquesta lectura de datos, cálculo y presentación.

def accion_cuadrado() -> None:
	lado = pedir_flotante_positivo("Introduce el lado del cuadrado: ")
	imprimir_resultados("Cuadrado", Geometria2D.cuadrado(lado))


def accion_rectangulo() -> None:
	base = pedir_flotante_positivo("Introduce la base del rectángulo: ")
	altura = pedir_flotante_positivo("Introduce la altura del rectángulo: ")
	imprimir_resultados("Rectángulo", Geometria2D.rectangulo(base, altura))


def accion_triangulo() -> None:
	base = pedir_flotante_positivo("Introduce la base del triángulo: ")
	altura = pedir_flotante_positivo("Introduce la altura del triángulo: ")
	lado1 = pedir_flotante_positivo("Introduce el lado 1 del triángulo: ")
	lado2 = pedir_flotante_positivo("Introduce el lado 2 del triángulo: ")
	imprimir_resultados("Triángulo", Geometria2D.triangulo(base, altura, lado1, lado2))


def accion_circulo() -> None:
	radio = pedir_flotante_positivo("Introduce el radio del círculo: ")
	imprimir_resultados("Círculo", Geometria2D.circulo(radio))


def accion_rombo() -> None:
	diagonal_mayor = pedir_flotante_positivo("Introduce la diagonal mayor del rombo: ")
	diagonal_menor = pedir_flotante_positivo("Introduce la diagonal menor del rombo: ")
	lado = pedir_flotante_positivo("Introduce el lado del rombo: ")
	imprimir_resultados("Rombo", Geometria2D.rombo(diagonal_mayor, diagonal_menor, lado))


def accion_trapecio() -> None:
	base_mayor = pedir_flotante_positivo("Introduce la base mayor del trapecio: ")
	base_menor = pedir_flotante_positivo("Introduce la base menor del trapecio: ")
	altura = pedir_flotante_positivo("Introduce la altura del trapecio: ")
	lado1 = pedir_flotante_positivo("Introduce el lado 1 del trapecio: ")
	lado2 = pedir_flotante_positivo("Introduce el lado 2 del trapecio: ")
	imprimir_resultados("Trapecio", Geometria2D.trapecio(base_mayor, base_menor, altura, lado1, lado2))


def accion_cubo() -> None:
	lado = pedir_flotante_positivo("Introduce el lado del cubo: ")
	imprimir_resultados("Cubo", Geometria3D.cubo(lado))


def accion_prisma_rectangular() -> None:
	largo = pedir_flotante_positivo("Introduce el largo del prisma: ")
	ancho = pedir_flotante_positivo("Introduce el ancho del prisma: ")
	alto = pedir_flotante_positivo("Introduce el alto del prisma: ")
	imprimir_resultados("Prisma rectangular", Geometria3D.prisma_rectangular(largo, ancho, alto))


def accion_cilindro() -> None:
	radio = pedir_flotante_positivo("Introduce el radio del cilindro: ")
	altura = pedir_flotante_positivo("Introduce la altura del cilindro: ")
	imprimir_resultados("Cilindro", Geometria3D.cilindro(radio, altura))


def accion_esfera() -> None:
	radio = pedir_flotante_positivo("Introduce el radio de la esfera: ")
	imprimir_resultados("Esfera", Geometria3D.esfera(radio))


def accion_cono() -> None:
	radio = pedir_flotante_positivo("Introduce el radio del cono: ")
	altura = pedir_flotante_positivo("Introduce la altura del cono: ")
	generatriz = pedir_flotante_positivo("Introduce la generatriz del cono: ")
	imprimir_resultados("Cono", Geometria3D.cono(radio, altura, generatriz))


# ============================================================
# MÓDULO 4: MENÚ INTERACTIVO Y ORQUESTACIÓN
# ============================================================
# Este bloque conecta las opciones de menú con sus acciones.

@dataclass(frozen=True)
class OpcionMenu:
	codigo: str
	descripcion: str
	accion: Callable[[], None]


def construir_menu() -> Tuple[List[OpcionMenu], Dict[str, OpcionMenu]]:
	"""Define todas las operaciones disponibles en la aplicación."""
	opciones = [
		OpcionMenu("1", "Cuadrado (área y perímetro)", accion_cuadrado),
		OpcionMenu("2", "Rectángulo (área y perímetro)", accion_rectangulo),
		OpcionMenu("3", "Triángulo (área y perímetro)", accion_triangulo),
		OpcionMenu("4", "Círculo (área y circunferencia)", accion_circulo),
		OpcionMenu("5", "Rombo (área y perímetro)", accion_rombo),
		OpcionMenu("6", "Trapecio (área y perímetro)", accion_trapecio),
		OpcionMenu("7", "Cubo (área total y volumen)", accion_cubo),
		OpcionMenu("8", "Prisma rectangular (área total y volumen)", accion_prisma_rectangular),
		OpcionMenu("9", "Cilindro (áreas y volumen)", accion_cilindro),
		OpcionMenu("10", "Esfera (área y volumen)", accion_esfera),
		OpcionMenu("11", "Cono (áreas y volumen)", accion_cono),
	]
	opciones_por_codigo = {opcion.codigo: opcion for opcion in opciones}
	return opciones, opciones_por_codigo


def mostrar_menu(opciones: List[OpcionMenu]) -> None:
	"""Imprime el menú principal de operaciones geométricas."""
	print("\n================ CALCULADORA GEOMÉTRICA ================")
	print("Selecciona la figura geométrica y su operación básica:")
	for opcion in opciones:
		print(f"{opcion.codigo}. {opcion.descripcion}")
	print("0. Salir")
	print("========================================================")


def ejecutar_aplicacion() -> None:
	"""Bucle principal de la app de consola."""
	opciones, opciones_por_codigo = construir_menu()
	codigos_validos = [opcion.codigo for opcion in opciones] + ["0"]

	print("Bienvenido/a a la Calculadora Geométrica profesional.\n")

	while True:
		mostrar_menu(opciones)
		opcion = pedir_opcion_valida(codigos_validos)

		if opcion == "0":
			print("\nGracias por usar la aplicación. ¡Hasta la próxima!")
			break

		accion = opciones_por_codigo[opcion].accion
		accion()


# ============================================================
# PUNTO DE ENTRADA
# ============================================================

if __name__ == "__main__":
	ejecutar_aplicacion()
