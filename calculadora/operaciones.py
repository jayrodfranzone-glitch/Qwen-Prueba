"""Módulo con las operaciones básicas de la calculadora."""


def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b


def restar(a, b):
    """Devuelve la resta de dos números."""
    return a - b


def multiplicar(a, b):
    """Devuelve la multiplicación de dos números."""
    return a * b


def dividir(a, b):
    """Devuelve la división de dos números. Lanza error si se divide por cero."""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
