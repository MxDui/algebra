def search_in_graph(G, start_vertex):
    C = []
    colored = set()
    i = 0

    # Selecciona el vértice de inicio y colorea de negro
    r = start_vertex
    colored.add(r)
    C.append(r)
    print(f"Inicializando con vértice {r}")

    while C:
        r = C[0]
        neighbors = G[r]
        found_uncolored = False
        
        for y in neighbors:
            if y not in colored:
                i += 1
                colored.add(y)
                C.append(y)
                print(f"Vértice {y} coloreado y agregado a C")
                found_uncolored = True
                break
        
        if not found_uncolored:
            C.remove(r)
            print(f"Vértice {r} removido de C")

    print(f"Terminado. Todos los vértices han sido coloreados.")

# Gráfica G
G = {
    'u': ['x','y'],
    'v': ['x', 'w', 'y', 'z'],
    'w': ['v', 'x', 's','z'],
    'x': ['v', 'w', 'u'],
    'y': ['u', 'z', 'v'],
    'z': ['y', 's','v','w'],
    's': ['w', 'z']
}

# Ejecutar el algoritmo
search_in_graph(G, 'u')
