import unittest
from src.ga.core import GeneticAlgorithm
from src.problems.knapsack import KnapsackProblem

class TestGeneticAlgorithm(unittest.TestCase):

    def setUp(self):
        self.knapsack_problem = KnapsackProblem(num_items=20, max_weight=50)
        self.ga = GeneticAlgorithm(problem=self.knapsack_problem, population_size=50, generations=500, tournament_size=3, crossover_rate=0.8, mutation_rate=0.02, elitism_count=2)

    def test_initial_population(self):
        population = self.ga.initialize_population()
        self.assertEqual(len(population), 50)
        for individual in population:
            self.assertEqual(len(individual), 20)

    def test_selection(self):
        selected = self.ga.tournament_selection()
        self.assertEqual(len(selected), 3)
        for individual in selected:
            self.assertIn(individual, self.ga.population)

    def test_crossover_one_point(self):
        parent1 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        parent2 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        offspring = self.ga.crossover_one_point(parent1, parent2)
        self.assertNotEqual(offspring, parent1)
        self.assertNotEqual(offspring, parent2)

    def test_mutation(self):
        individual = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        mutated_individual = self.ga.bit_flip_mutation(individual)
        self.assertNotEqual(mutated_individual, individual)

    def test_elitism(self):
        self.ga.population = [[0, 1] * 10, [1, 0] * 10]  # Two individuals
        self.ga.evolve()
        self.assertIn(self.ga.best_individual, self.ga.population)

if __name__ == '__main__':
    unittest.main()