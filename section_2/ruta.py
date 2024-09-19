# Definimos el grafo como un diccionario donde cada nodo tiene una lista de tuplas
# Cada tupla contiene un nodo adyacente y el peso de la arista que los conecta
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target=''):
    # Lista de nodos no visitados
    unvisited = list(graph)
    
    # Diccionario para almacenar las distancias desde el nodo inicial a cada nodo
    # Inicializamos la distancia al nodo inicial como 0 y al resto como infinito
    distances = {node: 0 if node == start else float('inf') for node in graph}
    
    # Diccionario para almacenar los caminos más cortos hacia cada nodo
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    # Mientras haya nodos no visitados
    while unvisited:
        # Seleccionamos el nodo no visitado con la menor distancia acumulada
        current = min(unvisited, key=distances.get)
        
        # Recorremos los nodos adyacentes y sus distancias
        for node, distance in graph[current]:
            # Si encontramos una distancia más corta hacia el nodo adyacente, la actualizamos
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                
                # Actualizamos el camino más corto hacia el nodo adyacente
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        
        # Marcamos el nodo actual como visitado
        unvisited.remove(current)
    
    # Si se especifica un nodo objetivo, solo imprimimos la ruta hacia ese nodo
    # De lo contrario, imprimimos las rutas hacia todos los nodos
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths

# Llamamos a la función para encontrar la ruta más corta desde el nodo 'A' al nodo 'F'
shortest_path(my_graph, 'A', 'F')