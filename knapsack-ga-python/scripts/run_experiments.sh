#!/bin/bash

# Script para executar as instâncias do Algoritmo Genético para o problema da mochila

# Definindo parâmetros
POPULATION_SIZE=50
GENERATIONS=500
TOURNAMENT_SIZE=3
CROSSOVER_RATE=0.8
MUTATION_RATE=0.02
ELITISM_COUNT=2

# Executando 3 instâncias do Algoritmo Genético
for i in {1..3}
do
    echo "Executando instância $i do Algoritmo Genético..."
    python3 src/main.py --population_size $POPULATION_SIZE --generations $GENERATIONS --tournament_size $TOURNAMENT_SIZE --crossover_rate $CROSSOVER_RATE --mutation_rate $MUTATION_RATE --elitism_count $ELITISM_COUNT
done

echo "Experimentos concluídos."