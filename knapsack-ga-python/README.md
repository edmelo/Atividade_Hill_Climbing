# Knapsack Genetic Algorithm

Este projeto implementa um Algoritmo Genético para resolver o problema da mochila (Knapsack Problem) em 20 dimensões. O algoritmo é projetado para ser flexível e extensível, permitindo a experimentação com diferentes parâmetros e métodos.

## Estrutura do Projeto

- **src/**: Contém o código-fonte do projeto.
  - **ga/**: Implementação do Algoritmo Genético.
    - `__init__.py`: Inicializa o pacote do módulo de Algoritmo Genético.
    - `core.py`: Contém a classe `GeneticAlgorithm` com a lógica principal do algoritmo.
    - `population.py`: Define a classe `Population` para gerenciar a população de indivíduos.
    - `selection.py`: Implementa a função `tournament_selection` para seleção por torneio.
    - `crossover.py`: Contém funções para métodos de crossover (um ponto, dois pontos e uniforme).
    - `mutation.py`: Implementa a função `bit_flip_mutation` para mutação.
    - `utils.py`: Funções utilitárias para o projeto.
  - **problems/**: Módulo que define o problema da mochila.
    - `__init__.py`: Inicializa o pacote do módulo de problemas.
    - `knapsack.py`: Define a classe `KnapsackProblem` para o problema da mochila.
  - **experiments/**: Módulo para executar instâncias do algoritmo genético.
    - `__init__.py`: Inicializa o pacote do módulo de experimentos.
    - `run_instances.py`: Lógica para executar as instâncias do algoritmo genético.
  - `main.py`: Ponto de entrada do programa.

- **tests/**: Contém testes unitários.
  - `test_ga_core.py`: Testes para a classe `GeneticAlgorithm`.
  - `test_knapsack.py`: Testes para a classe `KnapsackProblem`.

- **configs/**: Configurações do projeto.
  - `default.yaml`: Configuração padrão com parâmetros do algoritmo.

- **scripts/**: Scripts auxiliares.
  - `run_experiments.sh`: Script para automatizar a execução das instâncias do algoritmo genético.

- **requirements.txt**: Lista de dependências do projeto.

- **pyproject.toml**: Configurações do projeto, incluindo dependências e metadados.

- **.gitignore**: Arquivos e pastas a serem ignorados pelo controle de versão.

## Instalação

Para instalar as dependências do projeto, execute:

```
pip install -r requirements.txt
```

## Uso

Para executar o algoritmo genético, utilize o arquivo `main.py`. Você pode configurar os parâmetros no arquivo `configs/default.yaml` antes de executar.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.