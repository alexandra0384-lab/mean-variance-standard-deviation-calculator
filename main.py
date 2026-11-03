import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matriz = np.array(list).reshape(3, 3)

    def resumen(funcion):
        # [eje 0 (columnas), eje 1 (filas), matriz aplanada]
        return [
            funcion(matriz, axis=0).tolist(),
            funcion(matriz, axis=1).tolist(),
            funcion(matriz).tolist(),
        ]

    calculations = {
        'mean': resumen(np.mean),
        'variance': resumen(np.var),
        'standard deviation': resumen(np.std),
        'max': resumen(np.max),
        'min': resumen(np.min),
        'sum': resumen(np.sum),
    }

    return calculations
