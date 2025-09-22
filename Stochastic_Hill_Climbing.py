import copy
import random
from typing import Callable, List, Tuple


class StochasticHillClimbing:
    def __init__(self, funcao_fitness: Callable[[List[int]], float], gerar_vizinhos: Callable[[List[int]], List[List[int]]], maximizar: bool = True):
        """
        Stochastic Hill Climbing: escolhe aleatoriamente um vizinho entre os que melhoram a solução atual.

        Args:
            funcao_fitness: função que avalia soluções (retorna escalar)
            gerar_vizinhos: função que gera vizinhos a partir de uma solução
            maximizar: True para maximização, False para minimização
        """
        self.funcao_fitness = funcao_fitness
        self.gerar_vizinhos = gerar_vizinhos
        self.maximizar = maximizar
        self.historico: List[float] = []

    def executar(self, solucao_inicial: List[int], max_iteracoes: int = 1000, verbose: bool = False) -> Tuple[List[int], float, List[float]]:
        """
        Executa o algoritmo Stochastic Hill Climbing.

        Retorna a melhor solução encontrada, seu fitness e o histórico de fitness.
        """
        solucao_atual = copy.deepcopy(solucao_inicial)
        fitness_atual = self.funcao_fitness(solucao_atual)

        self.historico = [fitness_atual]
        iteracao = 0
        melhorias = 0

        if verbose:
            print(f"Iteração {iteracao}: Fitness = {fitness_atual:.4f}")

        while iteracao < max_iteracoes:
            iteracao += 1

            # Gerar vizinhos
            vizinhos = self.gerar_vizinhos(solucao_atual)

            # Avaliar vizinhos
            avaliacoes = []
            for v in vizinhos:
                avaliacoes.append((v, self.funcao_fitness(v)))

            # Filtrar os que melhoram
            if self.maximizar:
                candidatos = [par for par in avaliacoes if par[1] > fitness_atual]
            else:
                candidatos = [par for par in avaliacoes if par[1] < fitness_atual]

            if not candidatos:
                if verbose:
                    print(f"Convergiu na iteração {iteracao}")
                break

            # Escolher aleatoriamente um vizinho melhor
            viz_escolhido, fit_escolhido = random.choice(candidatos)

            # Mover
            solucao_atual = copy.deepcopy(viz_escolhido)
            fitness_atual = fit_escolhido
            melhorias += 1
            self.historico.append(fitness_atual)

            if verbose:
                print(f"Iteração {iteracao}: Fitness = {fitness_atual:.4f}")

        if verbose:
            print(f"Melhorias realizadas: {melhorias}")
            print(f"Fitness final: {fitness_atual:.4f}")

        return solucao_atual, fitness_atual, self.historico

