import heapq

def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def encontrar_ponto(labirinto, valor):
    for i, linha in enumerate(labirinto):
        for j, celula in enumerate(linha):
            if celula == valor:
                return (i, j)
    return None

def vizinhos(pos, labirinto):
    direcoes = [(-1,0),(1,0),(0,-1),(0,1)]
    resultado = []
    for dx, dy in direcoes:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < len(labirinto) and 0 <= ny < len(labirinto[0]):
            if labirinto[nx][ny] != '1':
                resultado.append((nx, ny))
    return resultado

def reconstruir_caminho(caminho, atual):
    total = [atual]
    while atual in caminho:
        atual = caminho[atual]
        total.append(atual)
    total.reverse()
    return total

def a_estrela(labirinto):
    inicio = encontrar_ponto(labirinto, 'S')
    fim = encontrar_ponto(labirinto, 'E')

    if not inicio or not fim:
        print("Labirinto inválido: ponto S ou E não encontrado.")
        return

    fila = []
    heapq.heappush(fila, (0, inicio))
    caminho = {}
    g_score = {inicio: 0}
    f_score = {inicio: heuristica(inicio, fim)}

    while fila:
        _, atual = heapq.heappop(fila)

        if atual == fim:
            return reconstruir_caminho(caminho, atual)

        for viz in vizinhos(atual, labirinto):
            tentativo_g = g_score[atual] + 1
            if tentativo_g < g_score.get(viz, float('inf')):
                caminho[viz] = atual
                g_score[viz] = tentativo_g
                f_score[viz] = tentativo_g + heuristica(viz, fim)
                heapq.heappush(fila, (f_score[viz], viz))

    return None

def imprimir_labirinto(labirinto, caminho):
    labirinto_copia = [linha.copy() for linha in labirinto]
    for x, y in caminho:
        if labirinto_copia[x][y] == '0':
            labirinto_copia[x][y] = '*'
    for linha in labirinto_copia:
        print(" ".join(linha))

def main():
    labirinto = [
        ['S','0','1','0','0'],
        ['0','0','1','0','1'],
        ['1','0','1','0','0'],
        ['1','0','0','E','1']
    ]

    caminho = a_estrela(labirinto)
    if caminho:
        print("Menor caminho (em coordenadas):")
        caminho_rotulado = []
        for i, p in enumerate(caminho):
            if labirinto[p[0]][p[1]] == 'S':
                caminho_rotulado.append(f"s{p}")
            elif labirinto[p[0]][p[1]] == 'E':
                caminho_rotulado.append(f"e{p}")
            else:
                caminho_rotulado.append(str(p))
        print(caminho_rotulado)
        print("\nLabirinto com o caminho destacado:")
        imprimir_labirinto(labirinto, caminho)
    else:
        print("Sem solução.")

if __name__ == "__main__":
    main()
