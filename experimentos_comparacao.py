import os
import random
import numpy as np
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
import matplotlib.pyplot as plt

from hill_climbing import HillClimbing, gerar_vizinhos_knapsack
from knapsack import knapsack
from Stochastic_Hill_Climbing import StochasticHillClimbing

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def log(msg: str):
    try:
        with open(os.path.join(SCRIPT_DIR, "comparacao_log.txt"), "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception:
        pass


def rodar_30_runs(dim=20, max_iter=200):
    fitness_hc = []
    fitness_shc = []

    for run in range(30):
        # mesma semente para ambos
        random.seed(run)
        solucao_inicial = [int(random.random() > 0.8) for _ in range(dim)]

        # Tradicional
        hc = HillClimbing(
            funcao_fitness=lambda s: knapsack(s, dim=dim)[0],
            gerar_vizinhos=gerar_vizinhos_knapsack,
            maximizar=True,
        )
        _, fit_hc, _ = hc.executar(solucao_inicial, max_iteracoes=max_iter, verbose=False)
        fitness_hc.append(fit_hc)

        # Stochastic
        # reusa mesma solucao_inicial; opcionalmente podemos fixar de novo a semente
        shc = StochasticHillClimbing(
            funcao_fitness=lambda s: knapsack(s, dim=dim)[0],
            gerar_vizinhos=gerar_vizinhos_knapsack,
            maximizar=True,
        )
        _, fit_shc, _ = shc.executar(solucao_inicial, max_iteracoes=max_iter, verbose=False)
        fitness_shc.append(fit_shc)

    return np.array(fitness_hc, dtype=float), np.array(fitness_shc, dtype=float)


def salvar_boxplot_comparativo(fitness_hc, fitness_shc, saida_png=None):
    if saida_png is None:
        saida_png = os.path.join(SCRIPT_DIR, "boxplot_comparacao.png")

    data = [
        ("HC", x) for x in fitness_hc
    ] + [
        ("SHC", x) for x in fitness_shc
    ]
    labels, values = zip(*data)

    plt.figure(figsize=(7, 5))
    sns.set(style="whitegrid")
    ax = sns.boxplot(x=list(labels), y=list(values), palette=["#4C78A8", "#F58518"])
    ax.set_xlabel("Algoritmo")
    ax.set_ylabel("Fitness final")
    ax.set_title("Comparação: Hill Climbing vs Stochastic Hill Climbing (30 execuções)")
    plt.tight_layout()
    plt.savefig(saida_png, dpi=150)
    plt.close()
    return saida_png


def salvar_csv_stats(fitness_hc, fitness_shc):
    csv_path = os.path.join(SCRIPT_DIR, "fitness_comparacao.csv")
    with open(csv_path, "w", encoding="utf-8") as f:
        f.write("algoritmo,fitness\n")
        for v in fitness_hc:
            f.write(f"HC,{v:.6f}\n")
        for v in fitness_shc:
            f.write(f"SHC,{v:.6f}\n")

    stats_path = os.path.join(SCRIPT_DIR, "estatisticas_comparacao.txt")
    def stats(arr):
        return float(np.mean(arr)), float(np.std(arr, ddof=1))

    m_hc, sd_hc = stats(fitness_hc)
    m_shc, sd_shc = stats(fitness_shc)

    with open(stats_path, "w", encoding="utf-8") as f:
        f.write("=== Estatísticas (30 execuções) ===\n")
        f.write(f"HC - Média: {m_hc:.4f}, Desvio Padrão: {sd_hc:.4f}\n")
        f.write(f"SHC - Média: {m_shc:.4f}, Desvio Padrão: {sd_shc:.4f}\n")

    return csv_path, stats_path


if __name__ == "__main__":
    try:
        log("Iniciando comparação HC vs SHC (30 execuções)...")
        hc_vals, shc_vals = rodar_30_runs(dim=20, max_iter=200)
        png = salvar_boxplot_comparativo(hc_vals, shc_vals)
        csv, stats = salvar_csv_stats(hc_vals, shc_vals)
        log(f"Gerados: {os.path.basename(png)}, {os.path.basename(csv)}, {os.path.basename(stats)}")
    except Exception as e:
        import traceback
        with open(os.path.join(SCRIPT_DIR, "comparacao_error.log"), "w", encoding="utf-8") as ef:
            ef.write("Falha na comparação.\n")
            ef.write(str(e) + "\n\n")
            ef.write(traceback.format_exc())
        log("Erro durante a comparação. Verifique comparacao_error.log")
        raise

