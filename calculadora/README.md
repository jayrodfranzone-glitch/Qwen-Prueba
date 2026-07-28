# Calculadora

Una calculadora básica implementada en Python que permite realizar operaciones aritméticas fundamentales.

## Estructura del Proyecto

```
calculadora/
├── main.py          # Punto de entrada principal con la interfaz de usuario
├── operaciones.py   # Módulo con las funciones de operaciones matemáticas
└── README.md        # Este archivo de documentación
```

## Características

- **Suma**: Suma dos números
- **Resta**: Resta dos números
- **Multiplicación**: Multiplica dos números
- **División**: Divide dos números (con validación para división por cero)

## Requisitos

- Python 3.x

## Uso

1. Navega al directorio del proyecto:
   ```bash
   cd calculadora
   ```

2. Ejecuta la calculadora:
   ```bash
   python main.py
   ```

3. Sigue el menú interactivo para seleccionar la operación deseada.

## Ejemplo de Uso

```
=== Calculadora ===
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
Selecciona una opción (1-5): 1
Ingresa el primer número: 10
Ingresa el segundo número: 5

Resultado: 10.0 + 5.0 = 15.0
```

## Módulos

### `operaciones.py`

Contiene las funciones básicas:
- `sumar(a, b)` - Devuelve la suma de a y b
- `restar(a, b)` - Devuelve la resta de a y b
- `multiplicar(a, b)` - Devuelve la multiplicación de a y b
- `dividir(a, b)` - Devuelve la división de a entre b (lanza error si b es 0)

### `main.py`

Contiene la lógica principal:
- Menú interactivo
- Validación de entrada
- Manejo de errores

## Autor

Proyecto creado como ejemplo educativo.

## Licencia

Este proyecto es de código abierto y puede ser utilizado libremente.
