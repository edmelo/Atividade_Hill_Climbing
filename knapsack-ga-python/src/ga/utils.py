import random
from typing import List, Tuple


def generate_random_population(size: int, dimensions: int) -> List[List[int]]:
    return [[random.randint(0, 1) for _ in range(dimensions)] for _ in range(size)]


def calculate_fitness(individual: List[int], values: List[int], weights: List[int], capacity: int) -> int:
    total_value = sum(v * i for v, i in zip(values, individual))
    total_weight = sum(w * i for w, i in zip(weights, individual))
    if total_weight > capacity:
        return 0
    return total_value


def select_best_individuals(population: List[List[int]], fitnesses: List[float], num_best: int) -> List[List[int]]:
    sorted_population = [ind for _, ind in sorted(zip(fitnesses, population), key=lambda x: x[0], reverse=True)]
    return sorted_population[:num_best]


def crossover_one_point(parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


def crossover_two_points(parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
    point1 = random.randint(1, len(parent1) - 2)
    point2 = random.randint(point1 + 1, len(parent1) - 1)
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return child1, child2


def crossover_uniform(parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
    child1 = [random.choice([g1, g2]) for g1, g2 in zip(parent1, parent2)]
    child2 = [random.choice([g1, g2]) for g1, g2 in zip(parent1, parent2)]
    return child1, child2


def bit_flip_mutation(individual: List[int], mutation_rate: float) -> List[int]:
    return [gene if random.random() > mutation_rate else 1 - gene for gene in individual]
