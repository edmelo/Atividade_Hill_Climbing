# Atividade: Hill Climbing Tradicional e Estocástico no Knapsack (20 dimensões)

## Objetivo
Implementar e avaliar o algoritmo Hill Climbing (HC) tradicional e sua variação Stochastic Hill Climbing (SHC) no problema da mochila binária (Knapsack) com 20 itens, executando 30 simulações e comparando os resultados por meio de estatísticas (média e desvio padrão) e boxplots.

## Resumo do que foi feito
- Atualizado o problema Knapsack para suportar 20 dimensões (itens) e tornar a dimensão configurável.
- Ajustado o script de Hill Climbing tradicional para trabalhar com 20 itens.
- Implementado o Stochastic Hill Climbing (SHC), que escolhe aleatoriamente entre vizinhos que melhoram a solução.
- Criados scripts de experimentos para:
  - Rodar 30 simulações do HC e gerar média, desvio padrão e boxplot.
  - Comparar HC vs SHC com 30 simulações, salvar estatísticas comparativas e boxplot lado a lado.

## Ambiente e dependências
As dependências estão em `requirements.txt` (numpy, pandas, seaborn, matplotlib, jupyter). Os scripts foram preparados para rodar em ambientes headless (matplotlib backend Agg) e salvam os artefatos no diretório do projeto.

## Implementações e alterações
### 1) knapsack.py (20 dimensões)
- Adicionadas constantes para uma instância com 20 itens (valores e pesos), mantendo compatibilidade com a instância original de 10 itens.
- `knapsack(solution, dim=20)`: agora o default é 20; a função verifica que o tamanho da solução coincide com `dim` e calcula (valor_total, peso_total, válido) considerando a capacidade máxima da instância (456 para 20 itens).
- O arquivo inclui uma função de teste parametrizada por `dim` para inspeção rápida.

### 2) hill_climbing.py (HC tradicional)
- Mantida a geração de vizinhos via flip de um único bit aleatório (até `n_vizinhos`).
- Ajustes:
  - Import do `knapsack` local.
  - `DIM = 20` para executar com 20 itens.
  - Fitness definido como o valor total do knapsack (maximização), zerado automaticamente se exceder a capacidade (penalização embutida pela função `knapsack`).

### 3) Stochastic_Hill_Climbing.py (SHC)
- Implementada a classe `StochasticHillClimbing` com a mesma interface do HC tradicional:
  - Em cada iteração, gera vizinhos, avalia todos e filtra os que melhoram o fitness corrente.
  - Escolhe aleatoriamente um vizinho dentre os que melhoram e move para ele.
  - Para quando não há vizinho melhor.

### 4) experimentos_knapsack.py (30 simulações do HC)
- Roda 30 execuções do HC (20D) e salva:
  - `boxplot_fitness.png`: boxplot dos 30 fitness finais.
  - `fitness_values.csv`: vetor de fitness (uma coluna `fitness`).
  - `estatisticas_knapsack.txt`: média e desvio padrão (amostral).
- Detalhes:
  - Usa seeds distintas por rodada (0..29) para reprodutibilidade.
  - Usa backend `Agg` para salvar figuras sem abrir janelas gráficas.
  - Log simplificado opcional em `experimentos_log.txt`.

### 5) experimentos_comparacao.py (HC vs SHC, 30 simulações)
- Executa 30 rodadas para cada algoritmo, com as MESMAS seeds e mesma solução inicial por rodada para fairness.
- Salva:
  - `boxplot_comparacao.png`: boxplot comparando HC (tradicional) vs SHC.
  - `fitness_comparacao.csv`: linhas com `algoritmo,fitness` (30 por método).
  - `estatisticas_comparacao.txt`: média e desvio padrão (amostral) de cada método.
- Log simples em `comparacao_log.txt` e captura de erros em `comparacao_error.log` (se necessário).

## Como executar (Windows - cmd)
1. Instale as dependências:
```cmd
pip install -r requirements.txt
```

2. Rode 30 simulações do HC (gera boxplot individual e estatísticas do HC):
```cmd
python experimentos_knapsack.py
```

3. Compare HC vs SHC (gera boxplot comparativo e estatísticas de ambos):
```cmd
python experimentos_comparacao.py
```

Os artefatos são salvos na raiz do projeto.

## Resultados (30 execuções, Knapsack 20D)
Resumo disponível em `estatisticas_comparacao.txt`:

- Hill Climbing (HC)
  - Média: 463.9667
  - Desvio Padrão (amostral): 47.7100

- Stochastic Hill Climbing (SHC)
  - Média: 403.1667
  - Desvio Padrão (amostral): 43.7675

Figura: `boxplot_comparacao.png` — mostra a distribuição dos fitness finais dos dois métodos.

Interpretando:
- O HC tradicional, ao sempre escolher o melhor vizinho, apresentou média mais alta nesta instância específica, com dispersão moderada.
- O SHC, ao escolher aleatoriamente entre vizinhos que melhoram, amplia a exploração e pode escapar de alguns ótimos locais; contudo, nesta configuração, a média final foi menor que a do HC.
- O comportamento pode variar conforme a definição de vizinhança, número de vizinhos gerados, seeds e capacidade da mochila; ainda assim, os boxplots ajudam a visualizar a robustez e a variabilidade de cada método.

## Artefatos gerados
- Avaliação do HC (30x):
  - `boxplot_fitness.png`
  - `fitness_values.csv`
  - `estatisticas_knapsack.txt`
  - `experimentos_log.txt` (log opcional)

- Comparação HC vs SHC (30x cada):
  - `boxplot_comparacao.png`
  - `fitness_comparacao.csv`
  - `estatisticas_comparacao.txt`
  - `comparacao_log.txt` (log opcional)

## Conclusões e próximos passos
- A comparação sugere que, para a vizinhança adotada (flip de bit) e a instância de 20 itens construída, o HC superou o SHC em média.
- Próximos passos que podem alterar o panorama:
  - Aumentar o número de vizinhos por iteração e/ou permitir flips múltiplos.
  - Introduzir reinícios aleatórios (Random Restart Hill Climbing) para mitigar ótimos locais.
  - Ajustar a instância (valores/pesos/capacidade) e comparar novamente.
  - Testar Simulated Annealing, GRASP, ou meta-heurísticas populacionais (GA/PSO) para referência.

