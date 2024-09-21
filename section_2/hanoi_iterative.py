# Número de discos en el problema de las Torres de Hanoi
NUMBER_OF_DISKS = 4

# Número total de movimientos necesarios para resolver el problema
number_of_moves = 2 ** NUMBER_OF_DISKS - 1

# Diccionario que representa las varillas y los discos en cada una
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),  # Varilla A con los discos en orden descendente
    'B': [],  # Varilla B vacía
    'C': []   # Varilla C vacía
}

# Función para realizar un movimiento permitido entre dos varillas
def make_allowed_move(rod1, rod2):
    forward = False
    # Si la varilla de destino está vacía, el movimiento es permitido
    if not rods[rod2]:
        forward = True
    # Si la varilla de origen no está vacía y el disco superior es menor que el de la varilla de destino
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        forward = True
    # Realizar el movimiento en la dirección permitida
    if forward:
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
        rods[rod2].append(rods[rod1].pop())
    else:
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        rods[rod1].append(rods[rod2].pop())
    
    # Imprimir el estado actual de las varillas
    print(rods, '\n')

# Función principal para mover los discos usando un enfoque iterativo
def move(n, source, auxiliary, target):
    # Imprimir el estado inicial de las varillas
    print(rods, '\n')
    # Iterar sobre el número total de movimientos necesarios
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        # Determinar el movimiento permitido basado en el número de discos y el paso actual
        # Determinar el movimiento permitido basado en el número de discos y el paso actual
        if remainder == 1:
            if n % 2 != 0:
            # Si el número de discos es impar, mover entre la varilla de origen y la varilla de destino
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            else:
            # Si el número de discos es par, mover entre la varilla de origen y la varilla auxiliar
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
        elif remainder == 2:
            if n % 2 != 0:
            # Si el número de discos es impar, mover entre la varilla de origen y la varilla auxiliar
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
            else:
            # Si el número de discos es par, mover entre la varilla de origen y la varilla de destino
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
        elif remainder == 0:
            # Mover entre la varilla auxiliar y la varilla de destino
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target)

# Llamar a la función principal para resolver el problema
move(NUMBER_OF_DISKS, 'A', 'B', 'C')