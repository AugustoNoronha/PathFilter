# PathFilter

## Contribuidores

- [Augusto Noronha](https://github.com/AugustoNoronha)
- [Gabriel Lourenço](https://github.com/gabrielreisresende)
- [Pedro Máximo](https://github.com/pedromaximocampos)

## Descrição do Projeto

PathFilter é um projeto que implementa o algoritmo A\* para encontrar o caminho mais curto em um labirinto 2D. O algoritmo utiliza a distância de Manhattan como heurística para otimizar a busca do caminho ideal entre um ponto inicial e um ponto final no labirinto.

## Problema Resolvido

O projeto resolve o problema de encontrar o caminho mais curto em um labirinto 2D, onde:

- O labirinto é representado por uma matriz 2D
- 0 representa caminhos livres
- 1 representa paredes/obstáculos
- É necessário encontrar o caminho mais curto do ponto inicial até o ponto final, evitando obstáculos

## Algoritmo A\*

O algoritmo A\* implementado combina:

1. **Custo do Caminho (g)**: Soma dos custos de cada movimento desde o início
2. **Heurística (h)**: Distância de Manhattan até o objetivo
   - Fórmula: |x1 - x2| + |y1 - y2|
3. **Função de Avaliação (f)**: f = g + h

O algoritmo mantém duas listas:

- Lista Aberta: Nós a serem explorados
- Lista Fechada: Nós já visitados

### Funcionamento do Algoritmo

1. Inicia com o nó inicial na lista aberta
2. Seleciona o nó com menor valor f
3. Expande os vizinhos válidos (não são paredes)
4. Calcula g, h e f para cada vizinho
5. Atualiza as listas aberta e fechada
6. Repete até encontrar o objetivo ou esgotar todas as possibilidades

## Configuração e Execução

### Pré-requisitos

- Python 3.x

### Como Executar

1. Clone o repositório:

   ```
   git clone https://github.com/AugustoNoronha/PathFilter.git
   ```

2. Navegue até o diretório do projeto:

   ```
   cd PathFilter
   ```

3. Execute o programa:
   ```
   python main.py
   ```

## Exemplos de Uso

O programa inclui três exemplos diferentes para demonstrar o funcionamento do algoritmo A\*:

### Exemplo 1: Labirinto Simples

```
Labirinto Original:
S 0 1 0 0
0 0 1 0 1
1 0 1 0 0
1 0 0 E 1

Menor caminho encontrado:
S * 1 0 0
* * 1 0 1
1 * 1 0 0
1 * * E 1
```

### Exemplo 2: Labirinto Sem Solução

```
Labirinto Original:
S 1 0 0 0
1 1 1 0 1
0 0 1 0 0
1 1 1 E 1

Sem solução.
```

### Exemplo 3: Labirinto com Múltiplos Caminhos

```
Labirinto Original:
S 0 0 0 0
1 1 0 1 0
0 0 0 0 0
0 1 1 1 E

Menor caminho encontrado:
S * * * *
1 1 * 1 *
* * * * *
0 1 1 1 E
```

Legenda:

- S: Ponto inicial
- E: Ponto final
- 0: Caminho livre
- 1: Parede/obstáculo
- \*: Caminho encontrado pelo algoritmo
