# main.py

from ga.core import GeneticAlgorithm
from problems.knapsack import KnapsackProblem

def main():
    # Configurações do problema da mochila
    num_items = 20
    population_size = 50
    num_generations = 500
    tournament_size = 3
    crossover_rate = 0.8
    mutation_rate = 0.02
    elitism_count = 2

    # Inicializa o problema da mochila
    knapsack_problem = KnapsackProblem(num_items)

    # Inicializa o algoritmo genético
    ga = GeneticAlgorithm(
        problem=knapsack_problem,
        population_size=population_size,
        num_generations=num_generations,
        tournament_size=tournament_size,
        crossover_rate=crossover_rate,
        mutation_rate=mutation_rate,
        elitism_count=elitism_count
    )

    # Executa o algoritmo genético
    best_solution = ga.run()

    # Exibe a melhor solução encontrada
    print("Melhor solução encontrada:", best_solution)

if __name__ == "__main__":
    main()