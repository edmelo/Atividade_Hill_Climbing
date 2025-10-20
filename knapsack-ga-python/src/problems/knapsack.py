import random
from typing import List, Tuple


class KnapsackProblem:
    """Representa uma instância do problema knapsack.

    weights, values: listas de tamanho num_items
    capacity: capacidade máxima da mochila
    """

    def __init__(self, weights: List[int], values: List[int], capacity: int):
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.num_items = len(weights)

    def fitness(self, solution: List[int]) -> int:
        total_weight = sum(w * s for w, s in zip(self.weights, solution))
        total_value = sum(v * s for v, s in zip(self.values, solution))

        # Penalidade simples: fitness 0 se ultrapassar capacidade
        if total_weight > self.capacity:
            return 0
        return total_value

    def is_solution_valid(self, solution: List[int]) -> bool:
        return sum(w * s for w, s in zip(self.weights, solution)) <= self.capacity

    def get_random_solution(self) -> List[int]:
        return [1 if random.random() < 0.5 else 0 for _ in range(self.num_items)]

    def get_best_solution(self, population: List[List[int]]) -> Tuple[List[int], int]:
        best_solution = max(population, key=lambda sol: self.fitness(sol))
        return best_solution, self.fitness(best_solution)