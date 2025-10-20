import random
from typing import List, Tuple

from ga.selection import tournament_selection
from ga.crossover import one_point_crossover, two_point_crossover, uniform_crossover
from ga.mutations import bit_flip_mutation


class GeneticAlgorithm:
    def __init__(
        self,
        problem,
        population_size: int = 50,
        generations: int = 500,
        tournament_size: int = 3,
        crossover_rate: float = 0.8,
        mutation_rate: float = 0.02,
        elitism_count: int = 2,
        crossover_type: str = "one_point",
    ):
        self.problem = problem
        self.population_size = population_size
        self.generations = generations
        self.tournament_size = tournament_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.elitism_count = elitism_count
        self.crossover_type = crossover_type

        self.population: List[List[int]] = []
        self.fitnesses: List[float] = []
        self.history_best: List[float] = []

    def initialize_population(self):
        self.population = [self.problem.get_random_solution() for _ in range(self.population_size)]

    def evaluate_population(self):
        self.fitnesses = [self.problem.fitness(ind) for ind in self.population]

    def select_parents(self) -> Tuple[List[int], List[int]]:
        pop_with_fit = list(zip(self.population, self.fitnesses))
        selected = tournament_selection(pop_with_fit, tournament_size=self.tournament_size)
        # selected is list of tuples (ind, fitness) — return first two parents
        p1 = selected[0][0]
        p2 = selected[1][0]
        return p1, p2

    def _apply_crossover(self, parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
        if self.crossover_type == "one_point":
            return one_point_crossover(parent1, parent2)
        if self.crossover_type == "two_point":
            return two_point_crossover(parent1, parent2)
        if self.crossover_type == "uniform":
            return uniform_crossover(parent1, parent2)
        return one_point_crossover(parent1, parent2)

    def mutate(self, individual: List[int]) -> List[int]:
        return bit_flip_mutation(individual, self.mutation_rate)

    def run(self) -> Tuple[List[int], float, List[float]]:
        self.initialize_population()

        for gen in range(self.generations):
            self.evaluate_population()

            # elitism: keep top N
            sorted_idx = sorted(range(len(self.fitnesses)), key=lambda i: self.fitnesses[i], reverse=True)
            new_population = [self.population[i] for i in sorted_idx[: self.elitism_count]]

            # record best fitness
            best_fit = self.fitnesses[sorted_idx[0]] if self.fitnesses else 0
            self.history_best.append(best_fit)

            # fill rest of new population
            while len(new_population) < self.population_size:
                parent1, parent2 = self.select_parents()

                if random.random() < self.crossover_rate:
                    child1, child2 = self._apply_crossover(parent1, parent2)
                else:
                    child1, child2 = parent1[:], parent2[:]

                child1 = self.mutate(child1)
                if len(new_population) < self.population_size:
                    new_population.append(child1)
                if len(new_population) < self.population_size:
                    child2 = self.mutate(child2)
                    new_population.append(child2)

            self.population = new_population

        # final evaluation
        self.evaluate_population()
        best_idx = max(range(len(self.fitnesses)), key=lambda i: self.fitnesses[i])
        best_solution = self.population[best_idx]
        best_fitness = self.fitnesses[best_idx]

        return best_solution, best_fitness, self.history_best