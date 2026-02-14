"""
calculadora_imc.py

Aplicación de consola para cálculo avanzado de IMC con:
- Entrada validada y valores por defecto.
- Clasificación OMS estándar.
- Ajuste de umbrales para mayores de 65 años (normal: 23-28).
- Recomendaciones personalizadas según categoría.
"""

from __future__ import annotations


def pedir_texto(mensaje: str, valor_por_defecto: str) -> str:
	"""Solicita texto al usuario y aplica valor por defecto si no escribe nada."""
	valor = input(f"{mensaje} [{valor_por_defecto}]: ").strip()
	return valor if valor else valor_por_defecto


def pedir_float(mensaje: str, valor_por_defecto: float, minimo: float = 0.0) -> float:
	"""Solicita un número float con validación y valor por defecto."""
	while True:
		entrada = input(f"{mensaje} [{valor_por_defecto}]: ").strip().replace(",", ".")
		if not entrada:
			return valor_por_defecto

		try:
			valor = float(entrada)
			if valor <= minimo:
				print(f"⚠️  El valor debe ser mayor que {minimo}.")
				continue
			return valor
		except ValueError:
			print("⚠️  Entrada no válida. Introduce un número.")


def pedir_int(mensaje: str, valor_por_defecto: int, minimo: int = 0) -> int:
	"""Solicita un entero con validación y valor por defecto."""
	while True:
		entrada = input(f"{mensaje} [{valor_por_defecto}]: ").strip()
		if not entrada:
			return valor_por_defecto

		try:
			valor = int(entrada)
			if valor <= minimo:
				print(f"⚠️  El valor debe ser mayor que {minimo}.")
				continue
			return valor
		except ValueError:
			print("⚠️  Entrada no válida. Introduce un número entero.")


def pedir_genero(mensaje: str = "Género (M/F)", valor_por_defecto: str = "M") -> str:
	"""Solicita género M/F y normaliza la entrada."""
	while True:
		entrada = input(f"{mensaje} [{valor_por_defecto}]: ").strip().upper()
		if not entrada:
			return valor_por_defecto
		if entrada in {"M", "F"}:
			return entrada
		print("⚠️  Valor no válido. Escribe 'M' o 'F'.")


def calcular_imc(peso_kg: float, altura_m: float) -> float:
	"""Calcula el Índice de Masa Corporal."""
	return peso_kg / (altura_m**2)


def clasificar_imc(imc: float, edad: int) -> str:
	"""
	Clasifica el IMC:
	- Adulto estándar (OMS):
	  <18.5 Bajo peso | 18.5-24.9 Normal | 25.0-29.9 Sobrepeso | >=30 Obesidad
	- Mayores de 65 años:
	  <23 Bajo peso | 23-28 Normal | >28 Sobrepeso/Obesidad
	"""
	if edad > 65:
		if imc < 23:
			return "Bajo peso"
		if imc <= 28:
			return "Normal"
		return "Sobrepeso/Obesidad"

	if imc < 18.5:
		return "Bajo peso"
	if imc < 25:
		return "Normal"
	if imc < 30:
		return "Sobrepeso"
	return "Obesidad"


def generar_recomendaciones(categoria: str) -> str:
	"""Genera recomendaciones personalizadas según la categoría de IMC."""
	recomendaciones = {
		"Bajo peso": (
			"Consulta con nutricionista para valoración completa y plantea "
			"una dieta hipercalórica controlada junto con fortalecimiento muscular."
		),
		"Normal": (
			"Mantén hábitos actuales, equilibrio energético y ejercicio regular; "
			"realiza chequeos periódicos."
		),
		"Sobrepeso": (
			"Reduce azúcares y ultraprocesados, incrementa actividad cardiovascular "
			"de forma progresiva y realiza seguimiento profesional."
		),
		"Obesidad": (
			"Prioriza supervisión médica, plan nutricional estructurado y aumento "
			"progresivo de actividad física con control clínico."
		),
		"Sobrepeso/Obesidad": (
			"Reduce azúcares, aumenta actividad cardiovascular y realiza supervisión "
			"médica para un plan integral adaptado a tu edad."
		),
	}
	return recomendaciones.get(categoria, "Consulta con un profesional de salud para valoración personalizada.")


def mostrar_resumen(nombre: str, genero: str, edad: int, peso: float, altura: float, imc: float, categoria: str) -> None:
	"""Muestra un resumen limpio y elegante del resultado."""
	print("\n" + "=" * 62)
	print("        RESUMEN DE EVALUACIÓN DE ÍNDICE DE MASA CORPORAL")
	print("=" * 62)
	print(f"Paciente  : {nombre}")
	print(f"Género    : {genero}")
	print(f"Edad      : {edad} años")
	print(f"Peso      : {peso:.2f} kg")
	print(f"Altura    : {altura:.2f} m")
	print("-" * 62)
	print(f"IMC       : {imc:.2f}")
	print(f"Categoría : {categoria}")
	print("-" * 62)
	print("Recomendación:")
	print(generar_recomendaciones(categoria))
	print("=" * 62)


def main() -> None:
	"""Función principal que orquesta el flujo completo del programa."""
	print("Calculadora Avanzada de IMC\n")

	nombre = pedir_texto("Nombre", "Paciente")
	peso = pedir_float("Peso en kg", 70.0, minimo=0.0)
	altura = pedir_float("Altura en metros", 1.75, minimo=0.0)
	edad = pedir_int("Edad", 30, minimo=0)
	genero = pedir_genero("Género (M/F)", "M")

	imc = calcular_imc(peso, altura)
	categoria = clasificar_imc(imc, edad)

	mostrar_resumen(nombre, genero, edad, peso, altura, imc, categoria)


if __name__ == "__main__":
	main()
