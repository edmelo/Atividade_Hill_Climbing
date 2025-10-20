import random
from typing import List, Tuple


def tournament_selection(population_with_fitness: List[Tuple[list, float]], tournament_size: int = 3) -> List[Tuple[list, float]]:
    """Seleciona indivíduos via torneio. Recebe lista de (individual, fitness) e retorna a lista de vencedores.

    O número de seleções é igual ao tamanho da população (roda torneios com reposição entre torneios).
    """
    selected = []
    pop = population_with_fitness
    pop_size = len(pop)

    for _ in range(pop_size):
        tournament = random.sample(pop, k=min(tournament_size, pop_size))
        winner = max(tournament, key=lambda t: t[1])
        selected.append(winner)

    return selected
