"""
Simulación de Difusión de Calor 2D en terminal (esquema explícito).

Ecuación implementada:
	∂u/∂t = α ( ∂²u/∂x² + ∂²u/∂y² )

Características clave de esta implementación:
1) Malla cuadrada N x N con condiciones de contorno de Dirichlet fijas.
2) Cálculo automático de dt usando condición de estabilidad CFL para 2D explícito.
3) Renderizado en terminal sin librerías pesadas (solo NumPy + colorama opcional).
4) Arquitectura limpia orientada a métodos: inicializar, actualizar_paso, renderizar_terminal.
"""

from __future__ import annotations

import argparse
import os
import time
from dataclasses import dataclass

import numpy as np

try:
	from colorama import Fore, Style, init as colorama_init

	COLORAMA_DISPONIBLE = True
except ImportError:
	COLORAMA_DISPONIBLE = False


@dataclass(frozen=True)
class ConfiguracionSimulacion:
	"""Configuración principal del modelo numérico y del renderizado."""

	n: int = 20
	alpha: float = 1.0
	dx: float = 1.0
	pasos: int = 500
	cada_render: int = 5
	pausa: float = 0.03
	factor_seguridad_cfl: float = 0.95

	# Condiciones de contorno (Dirichlet)
	t_arriba: float = 100.0
	t_abajo: float = 0.0
	t_izquierda: float = 30.0
	t_derecha: float = 30.0


class DifusionCalor2D:
	"""Motor de simulación numérica para difusión de calor en 2D."""

	def __init__(self, cfg: ConfiguracionSimulacion) -> None:
		self.cfg = cfg
		self.dt = self._calcular_dt_estable()
		self.r = self.cfg.alpha * self.dt / (self.cfg.dx**2)
		self.u = self.inicializar_placa()
		self.iteracion = 0

		if COLORAMA_DISPONIBLE:
			colorama_init(autoreset=True)

	def _calcular_dt_estable(self) -> float:
		"""
		Para esquema explícito 2D:
			r = α dt / dx² <= 1/4
		-> dt <= dx² / (4α)
		"""
		dt_max = (self.cfg.dx**2) / (4.0 * self.cfg.alpha)
		return self.cfg.factor_seguridad_cfl * dt_max

	def inicializar_placa(self) -> np.ndarray:
		"""Inicializa la malla con interior a 0 y contornos fijos (Dirichlet)."""
		u = np.zeros((self.cfg.n, self.cfg.n), dtype=np.float64)
		self._aplicar_contornos(u)
		return u

	def _aplicar_contornos(self, matriz: np.ndarray) -> None:
		"""Aplica condiciones de contorno fijas sobre los 4 bordes."""
		matriz[0, :] = self.cfg.t_arriba
		matriz[-1, :] = self.cfg.t_abajo
		matriz[:, 0] = self.cfg.t_izquierda
		matriz[:, -1] = self.cfg.t_derecha

	def actualizar_paso(self) -> None:
		"""
		Actualiza un paso temporal usando diferencias finitas explícitas:
		u_new[i,j] = u[i,j] + r*(u[i+1,j] + u[i-1,j] + u[i,j+1] + u[i,j-1] - 4u[i,j])
		"""
		u_new = self.u.copy()
		u_new[1:-1, 1:-1] = self.u[1:-1, 1:-1] + self.r * (
			self.u[2:, 1:-1]
			+ self.u[:-2, 1:-1]
			+ self.u[1:-1, 2:]
			+ self.u[1:-1, :-2]
			- 4.0 * self.u[1:-1, 1:-1]
		)

		self._aplicar_contornos(u_new)
		self.u = u_new
		self.iteracion += 1

	def _bloque_por_temperatura(self, temp: float, t_min: float, t_max: float) -> str:
		"""Mapea temperatura a bloque visual con color ANSI (o escala gris ASCII)."""
		if t_max <= t_min:
			nivel = 0.0
		else:
			nivel = (temp - t_min) / (t_max - t_min)
			nivel = float(np.clip(nivel, 0.0, 1.0))

		# Dos caracteres para compensar aspecto rectangular de la terminal.
		bloque = "██"

		if not COLORAMA_DISPONIBLE:
			escala = " .:-=+*#%@"
			idx = min(int(nivel * (len(escala) - 1)), len(escala) - 1)
			return escala[idx] * 2

		if nivel < 0.15:
			return Fore.BLUE + bloque + Style.RESET_ALL
		if nivel < 0.30:
			return Fore.CYAN + bloque + Style.RESET_ALL
		if nivel < 0.50:
			return Fore.GREEN + bloque + Style.RESET_ALL
		if nivel < 0.70:
			return Fore.YELLOW + bloque + Style.RESET_ALL
		if nivel < 0.85:
			return Fore.LIGHTRED_EX + bloque + Style.RESET_ALL
		return Fore.RED + bloque + Style.RESET_ALL

	def renderizar_terminal(self) -> None:
		"""Limpia consola y dibuja el estado actual de la placa."""
		os.system("cls" if os.name == "nt" else "clear")

		t_min = float(np.min(self.u))
		t_max = float(np.max(self.u))
		t_media = float(np.mean(self.u))

		print("SIMULACIÓN DIFUSIÓN DE CALOR 2D (Diferencias Finitas Explícitas)")
		print(
			f"Iteración: {self.iteracion:4d} | N={self.cfg.n} | "
			f"alpha={self.cfg.alpha:.4f} | dx={self.cfg.dx:.4f} | dt={self.dt:.6f} | r={self.r:.4f}"
		)
		print(f"Temperaturas -> min: {t_min:.2f}°C | media: {t_media:.2f}°C | max: {t_max:.2f}°C")
		print("Contornos: arriba=100°C, abajo=0°C, izquierda=30°C, derecha=30°C")
		print()

		filas_render = []
		for fila in self.u:
			render_fila = "".join(self._bloque_por_temperatura(float(temp), t_min, t_max) for temp in fila)
			filas_render.append(render_fila)
		print("\n".join(filas_render))

		print("\nLeyenda visual: frío -> azul/cian, templado -> verde/amarillo, caliente -> rojo")
		if not COLORAMA_DISPONIBLE:
			print("Nota: colorama no detectado. Render en escala ASCII de intensidad.")

	def ejecutar(self) -> None:
		"""Ejecuta la simulación temporal y renderiza cada X iteraciones."""
		for _ in range(self.cfg.pasos):
			self.actualizar_paso()

			if self.iteracion % self.cfg.cada_render == 0 or self.iteracion == 1:
				self.renderizar_terminal()
				time.sleep(self.cfg.pausa)

		self.renderizar_terminal()
		print("\nSimulación finalizada.")


def parsear_argumentos() -> ConfiguracionSimulacion:
	"""Expone parámetros de simulación por línea de comandos."""
	parser = argparse.ArgumentParser(
		description="Simulación 2D de difusión de calor en placa cuadrada (esquema explícito)."
	)
	parser.add_argument("--n", type=int, default=20, help="Tamaño de rejilla N x N (default: 20)")
	parser.add_argument("--alpha", type=float, default=1.0, help="Coeficiente de difusión α (default: 1.0)")
	parser.add_argument("--dx", type=float, default=1.0, help="Espaciado espacial dx (default: 1.0)")
	parser.add_argument("--pasos", type=int, default=500, help="Número total de iteraciones (default: 500)")
	parser.add_argument(
		"--cada-render",
		type=int,
		default=5,
		dest="cada_render",
		help="Renderizar cada X pasos (default: 5)",
	)
	parser.add_argument("--pausa", type=float, default=0.03, help="Pausa entre renders en segundos (default: 0.03)")
	parser.add_argument(
		"--factor-cfl",
		type=float,
		default=0.95,
		dest="factor_seguridad_cfl",
		help="Factor de seguridad sobre dt_max de CFL, en (0,1] (default: 0.95)",
	)

	args = parser.parse_args()

	if args.n < 3:
		raise ValueError("N debe ser >= 3 para tener interior de la placa.")
	if args.alpha <= 0:
		raise ValueError("alpha debe ser > 0.")
	if args.dx <= 0:
		raise ValueError("dx debe ser > 0.")
	if args.pasos <= 0:
		raise ValueError("pasos debe ser > 0.")
	if args.cada_render <= 0:
		raise ValueError("cada-render debe ser > 0.")
	if not (0 < args.factor_seguridad_cfl <= 1.0):
		raise ValueError("factor-cfl debe estar en el rango (0, 1].")

	return ConfiguracionSimulacion(
		n=args.n,
		alpha=args.alpha,
		dx=args.dx,
		pasos=args.pasos,
		cada_render=args.cada_render,
		pausa=args.pausa,
		factor_seguridad_cfl=args.factor_seguridad_cfl,
	)


def main() -> None:
	"""Punto de entrada del script."""
	cfg = parsear_argumentos()
	simulador = DifusionCalor2D(cfg)
	simulador.ejecutar()


if __name__ == "__main__":
	main()