import unittest
from src.problems.knapsack import KnapsackProblem

class TestKnapsackProblem(unittest.TestCase):

    def setUp(self):
        self.items = [
            (10, 60),  # (peso, valor)
            (20, 100),
            (30, 120)
        ]
        self.capacity = 50
        self.knapsack = KnapsackProblem(self.items, self.capacity)

    def test_value_calculation(self):
        self.knapsack.selected_items = [1, 2]  # Selecionando os itens 1 e 2
        total_value = self.knapsack.calculate_total_value()
        self.assertEqual(total_value, 160)  # Valor esperado: 100 + 60

    def test_weight_calculation(self):
        self.knapsack.selected_items = [1, 2]  # Selecionando os itens 1 e 2
        total_weight = self.knapsack.calculate_total_weight()
        self.assertEqual(total_weight, 30)  # Peso esperado: 20 + 10

    def test_knapsack_exceeds_capacity(self):
        self.knapsack.selected_items = [0, 1, 2]  # Selecionando todos os itens
        total_weight = self.knapsack.calculate_total_weight()
        self.assertGreater(total_weight, self.capacity)  # Deve exceder a capacidade

    def test_knapsack_fits_capacity(self):
        self.knapsack.selected_items = [0, 1]  # Selecionando os itens 0 e 1
        total_weight = self.knapsack.calculate_total_weight()
        self.assertLessEqual(total_weight, self.capacity)  # Deve caber na capacidade

if __name__ == '__main__':
    unittest.main()