def merge_sort(array):
    # SI el array tiene un solo elemento o está vacío, no se hace nada
    if len(array) <= 1:
        return
    
    # Vamos a dividir el array en dos partes
    middle_point = len(array) // 2
    # Con SLICIN asignamos una a mitad izquierda y otra a mitad derecha
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Llamamos recursivamente a merge_sort para cada mitad
    merge_sort(left_part)
    merge_sort(right_part)

    # Inicializamos los índices para recorrer las dos mitades
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Vamos a comparar los elementos de las dos mitades y los vamos a ordenar
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        # Si el elemento de la mitad izquierda es menor, lo ponemos en la posición sorted_index
        if left_part[left_array_index] < right_part[right_array_index]:
            # Asignamos el elemento de la mitad izquierda al array
            array[sorted_index] = left_part[left_array_index]
            # Incrementamos el índice de la mitad izquierda
            left_array_index += 1
        else:
            # Asignamos el elemento de la mitad derecha al array
            array[sorted_index] = right_part[right_array_index]
            # Incrementamos el índice de la mitad derecha
            right_array_index += 1
        # Incrementamos el índice del array ordenado
        sorted_index += 1

    # Si quedan elementos en la mitad izquierda o derecha, los añadimos al array ordenado
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

# Ejemplo de uso
# Si ejecutamos este archivo, se ordenará el array numbers
if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print(f'Unsorted array:{numbers}')
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers))