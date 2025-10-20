# run_instances.py

import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from typing import List

from ga.core import GeneticAlgorithm
from problems.knapsack import KnapsackProblem


def run_single_instance(weights, values, capacity, crossover_type: str, run_id: int, **ga_params):
    problem = KnapsackProblem(weights, values, capacity)
    ga = GeneticAlgorithm(problem=problem, crossover_type=crossover_type, **ga_params)
    best_solution, best_fitness, history = ga.run()
    return best_solution, best_fitness, history


def run_experiments_for_instance(weights, values, capacity, out_dir: str, repetitions: int = 30, **ga_params):
    os.makedirs(out_dir, exist_ok=True)

    configs = ["one_point", "two_point", "uniform"]
    results = {c: [] for c in configs}
    histories = {c: [] for c in configs}

    for config in configs:
        for r in range(repetitions):
            _, best_fitness, history = run_single_instance(weights, values, capacity, config, r, **ga_params)
            results[config].append(best_fitness)
            histories[config].append(history)

        # save results CSV
        csv_path = os.path.join(out_dir, f"results_{config}.csv")
        with open(csv_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["run", "best_fitness"]) 
            for i, val in enumerate(results[config]):
                writer.writerow([i, val])

    # plot convergence (mean history per generation)
    plt.figure(figsize=(8, 6))
    for config in configs:
        # pad histories to max length and compute mean
        max_len = max(len(h) for h in histories[config])
        arr = np.array([h + [h[-1]] * (max_len - len(h)) for h in histories[config]])
        mean_curve = arr.mean(axis=0)
        plt.plot(mean_curve, label=config)

    plt.xlabel("Geração")
    plt.ylabel("Melhor fitness")
    plt.title("Convergência média por configuração")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "convergencia_media.png"))
    plt.close()

    # boxplot comparando os melhores fitnesses
    plt.figure(figsize=(8, 6))
    data = [results[c] for c in configs]
    plt.boxplot(data, labels=configs)
    plt.ylabel("Best fitness")
    plt.title("Boxplot - Melhor fitness por configuração ({} repetições)".format(repetitions))
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "boxplot_configs.png"))
    plt.close()

    return results, histories


def main():
    # Exemplo: criar uma instância de 20 dimensões aleatória (pode ser substituída por instâncias fixas)
    import random

    random.seed(0)
    np.random.seed(0)

    dimensions = 20
    weights = [random.randint(1, 20) for _ in range(dimensions)]
    values = [random.randint(1, 100) for _ in range(dimensions)]
    capacity = int(sum(weights) * 0.5)

    out_dir = "./results_ga"
    ga_params = {
        "population_size": 50,
        "generations": 500,
        "tournament_size": 3,
        "crossover_rate": 0.8,
        "mutation_rate": 0.02,
        "elitism_count": 2,
    }

    results, histories = run_experiments_for_instance(weights, values, capacity, out_dir, repetitions=30, **ga_params)

    # salvar resumo estatístico
    summary_path = os.path.join(out_dir, "summary.txt")
    with open(summary_path, "w") as f:
        for config, vals in results.items():
            f.write(f"Config: {config}\n")
            f.write(f"Mean: {np.mean(vals):.4f}\n")
            f.write(f"Std: {np.std(vals, ddof=1):.4f}\n")
            f.write(f"Best: {np.max(vals):.4f}\n")
            f.write("\n")

    print("Experimentos completos. Resultados salvos em:", out_dir)


if __name__ == "__main__":
    main()
