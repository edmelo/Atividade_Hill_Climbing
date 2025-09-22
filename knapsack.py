def _knapsack_constants(dim):
    GANHOS = []
    PESOS = []
    CAPACIDADE_MAXIMA = 0

    if dim == 10:
        GANHOS = [55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
        PESOS = [95, 4, 60, 32, 23, 72, 80, 62, 65, 46]
        CAPACIDADE_MAXIMA = 269

    if dim == 20:
        # Mantém os 10 primeiros itens da instância anterior e adiciona mais 10 itens
        GANHOS = [
            55, 10, 47, 5, 4, 50, 8, 61, 85, 87,  # itens originais
            39, 23, 52, 11, 44, 36, 58, 29, 63, 41  # novos itens
        ]
        PESOS = [
            95, 4, 60, 32, 23, 72, 80, 62, 65, 46,  # itens originais
            55, 12, 41, 18, 37, 40, 59, 22, 57, 33   # novos itens
        ]
        # Capacidade ~ metade do peso total para manter o problema interessante
        CAPACIDADE_MAXIMA = 456

    return GANHOS, PESOS, CAPACIDADE_MAXIMA


def knapsack(solution, dim=20):
    """
    Avalia uma seleção de itens para o problema da mochila.
    https://en.wikipedia.org/wiki/Knapsack_problem

    Args:
        solution: lista binária [0,1,0,1,...] indicando quais itens foram selecionados
        dim: quantidade de itens na instância (suporta 10 ou 20)

    Returns:
        tuple: (valor_total, peso_total, é_válido)
    """

    # A instância implementada considera 10 ou 20 dimensões
    assert len(solution) == dim, f"A solução deve ter exatamente {dim} dimensões."

    # Valores dos itens (benefícios)
    GANHOS, PESOS, CAPACIDADE_MAXIMA = _knapsack_constants(dim)

    # Calcula valor total e peso total dos itens selecionados
    ganho_total = 0
    peso_total = 0

    for i in range(len(solution)):
        if solution[i] == 1:  # Item foi selecionado
            ganho_total += GANHOS[i]
            peso_total += PESOS[i]

    # Verifica se a solução é válida (não excede a capacidade)
    eh_valido = peso_total <= CAPACIDADE_MAXIMA

    if not eh_valido:
        ganho_total = 0

    return ganho_total, peso_total, eh_valido


# Exemplos de uso:
def test_knapsack(dim=20):
    print("=== EXEMPLOS DE USO ===\n")

    # Exemplo 1: Selecionar apenas o item 1 (índice 1)
    selecao1 = [0] * dim
    selecao1[1] = 1
    valor, peso, valido = knapsack(selecao1, dim=dim)
    print(f"Seleção: {selecao1}")
    print(f"Valor: {valor}, Peso: {peso}, Válido: {valido}\n")

    # Exemplo 2: Selecionar alguns itens leves
    selecao2 = [0] * dim
    for idx in [1, 4, 6]:
        if idx < dim:
            selecao2[idx] = 1
    valor, peso, valido = knapsack(selecao2, dim=dim)
    print(f"Seleção: {selecao2}")
    print(f"Valor: {valor}, Peso: {peso}, Válido: {valido}\n")

    # Exemplo 3: Tentar selecionar muitos itens (pode exceder capacidade)
    selecao3 = [1] * dim
    valor, peso, valido = knapsack(selecao3, dim=dim)
    print(f"Seleção: {selecao3}")
    print(f"Valor: {valor}, Peso: {peso}, Válido: {valido}\n")

    # Mostra informações dos itens
    print("=== INFORMAÇÕES DOS ITENS ===")
    ganhos, pesos, cap = _knapsack_constants(dim)

    print("Item | Valor | Peso | Razão Valor/Peso")
    print("-" * 35)
    for i in range(dim):
        razao = ganhos[i] / pesos[i]
        print(f"{i:4d} | {ganhos[i]:5d} | {pesos[i]:4d} | {razao:.3f}")

    print(f"\nCapacidade máxima da mochila: {cap}")


# Executar exemplos
if __name__ == "__main__":
    test_knapsack(dim=20)

    # Dica: para usar em outros módulos, chame knapsack(solucao, dim=20)
