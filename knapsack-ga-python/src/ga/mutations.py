import random
from typing import List


def bit_flip_mutation(individual: List[int], mutation_rate: float) -> List[int]:
    mutated = individual.copy()
    for i in range(len(mutated)):
        if random.random() < mutation_rate:
            mutated[i] = 1 - mutated[i]
    return mutated
