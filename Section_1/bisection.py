# Script para calcular la raíz cuadrada de un número usando el método de bisección
#* El método de bisección es un método numérico para encontrar raíces de ecuaciones no lineales
#* El principio del método es dividir el intervalo en dos partes y seleccionar el subintervalo 
#* que contiene la raíz

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    
    # Bloque para manejar errores y operaciones especiales
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')
    # Bloque principal
    # ejemplo de uso: square_root_bisection(64)
    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2 
            square_mid = mid**2
            # Condición de parada
            if abs(square_mid - square_target) < tolerance:
            # Si la diferencia entre el cuadrado de mid y el objetivo es menor que la tolerancia, entonces mid es la raíz
                root = mid
                # Salimos del bucle
                break
            # Actualizar los límites del intervalo
            elif square_mid < square_target:
                # Si el cuadrado de mid es menor que el objetivo, entonces la raíz está en el intervalo [mid, high]
                low = mid
            else:
                # Si el cuadrado de mid es mayor que el objetivo, entonces la raíz está en el intervalo [low, mid]
                high = mid
        # Mensaje de error si no se encuentra la raíz
        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
        # Mensaje de éxito si se encuentra la raíz
        else:   
            print(f'The square root of {square_target} is approximately {root:-2f}')
    
    return root

N = 64
square_root_bisection(N)

