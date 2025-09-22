import os
import random
import numpy as np
import matplotlib
matplotlib.use("Agg")  # backend para ambientes headless
import seaborn as sns
import matplotlib.pyplot as plt
from hill_climbing import HillClimbing, gerar_vizinhos_knapsack
from knapsack import knapsack


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def log(msg: str):
    try:
        with open(os.path.join(SCRIPT_DIR, "experimentos_log.txt"), "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception:
        pass


def rodar_experimentos(n_runs=30, dim=20, max_iter=200, verbose=False):
    fitnesses = []

    for run in range(n_runs):
        # Semente diferente por execução para reprodutibilidade e variabilidade
        random.seed(run)

        # Solução inicial aleatória
        solucao_inicial = [int(random.random() > 0.8) for _ in range(dim)]

        # Setup do Hill Climbing
        hc = HillClimbing(
            funcao_fitness=lambda sol: knapsack(sol, dim=dim)[0],
            gerar_vizinhos=gerar_vizinhos_knapsack,
            maximizar=True,
        )

        # Executa
        _, melhor_fitness, _ = hc.executar(solucao_inicial, max_iteracoes=max_iter, verbose=verbose)
        fitnesses.append(melhor_fitness)

    return np.array(fitnesses, dtype=float)


def salvar_boxplot(fitnesses, saida_png=None):
    if saida_png is None:
        saida_png = os.path.join(SCRIPT_DIR, "boxplot_fitness.png")
    plt.figure(figsize=(6, 5))
    sns.set(style="whitegrid")
    ax = sns.boxplot(y=fitnesses, color="#4C78A8")
    ax.set_title("Boxplot dos Fitness (30 execuções)")
    ax.set_ylabel("Fitness final")
    plt.tight_layout()
    plt.savefig(saida_png, dpi=150)
    plt.close()
    return saida_png


def salvar_resultados(fitnesses, media, desvio_padrao, basepath=None):
    if basepath is None:
        basepath = SCRIPT_DIR
    # Salvar fitnesses
    csv_path = os.path.join(basepath, "fitness_values.csv")
    np.savetxt(csv_path, fitnesses, delimiter=",", fmt="%.6f", header="fitness", comments="")

    # Salvar estatísticas
    stats_path = os.path.join(basepath, "estatisticas_knapsack.txt")
    with open(stats_path, "w", encoding="utf-8") as f:
        f.write("=== Estatísticas das execuções ===\n")
        f.write(f"Quantidade de execuções: {len(fitnesses)}\n")
        f.write(f"Média do fitness: {media:.4f}\n")
        f.write(f"Desvio padrão (amostral): {desvio_padrao:.4f}\n")
    return csv_path, stats_path


if __name__ == "__main__":
    try:
        N_RUNS = 30
        DIM = 20
        MAX_ITER = 200

        log(f"Iniciando experimentos em {SCRIPT_DIR}")
        fitnesses = rodar_experimentos(n_runs=N_RUNS, dim=DIM, max_iter=MAX_ITER, verbose=False)

        media = float(np.mean(fitnesses))
        desvio_padrao_amostral = float(np.std(fitnesses, ddof=1))  # ddof=1 => desvio padrão amostral

        # Persistir arquivos
        png_path = salvar_boxplot(fitnesses)
        csv_path, stats_path = salvar_resultados(fitnesses, media, desvio_padrao_amostral)
        log(f"Arquivos gerados: {os.path.basename(png_path)}, {os.path.basename(csv_path)}, {os.path.basename(stats_path)}")
    except Exception as e:
        import traceback
        with open(os.path.join(SCRIPT_DIR, "experimentos_error.log"), "w", encoding="utf-8") as ef:
            ef.write("Falha ao executar experimentos.\n")
            ef.write(str(e) + "\n\n")
            ef.write(traceback.format_exc())
        log("Erro durante execução. Verifique experimentos_error.log")
        raise
