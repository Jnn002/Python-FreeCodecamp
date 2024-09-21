# Número de discos que queremos mover
NUMBER_OF_DISKS = 3

A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []  # Torre auxiliar vacía
C = []  # Torre destino vacía

# Mostrar el estado inicial de la lista A
print(f'Estado inicial lista 1: {A}\n')

# Función recursiva para mover los discos entre las torres
# n: número de discos a mover
# source: torre de origen
# auxiliary: torre auxiliar
# target: torre destino
def move(n, source, auxiliary, target):
    # Caso base: si no hay discos que mover, salir de la función
    if n <= 0:
        return
    
    # Paso 1: mover n-1 discos de la torre de origen a la torre auxiliar
    move(n - 1, source, target, auxiliary)
    
    # Paso 2: mover el disco n de la torre de origen a la torre destino
    target.append(source.pop())  # Pop elimina el disco superior de la torre de origen y lo añade a la torre destino
    
    # Imprimir el estado actual de las torres después de cada movimiento
    print(f'LISTA 1: {A}, LISTA 2: {B}, LISTA 3: {C}')
    
    # Paso 3: mover los n-1 discos desde la torre auxiliar a la torre destino
    move(n - 1, auxiliary, source, target)

# Llamada a la función para mover todos los discos desde A (origen) a C (destino)
move(NUMBER_OF_DISKS, A, B, C)
