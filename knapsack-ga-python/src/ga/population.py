class Population:
    def __init__(self, size, num_genes):
        self.size = size
        self.num_genes = num_genes
        self.individuals = self.initialize_population()

    def initialize_population(self):
        return [[self.random_gene() for _ in range(self.num_genes)] for _ in range(self.size)]

    def random_gene(self):
        return 1 if random.random() < 0.5 else 0

    def evaluate(self, fitness_function):
        return [fitness_function(individual) for individual in self.individuals]

    def select_best(self, fitness_scores, num_best):
        sorted_indices = sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i], reverse=True)
        return [self.individuals[i] for i in sorted_indices[:num_best]]

    def get_population(self):
        return self.individuals

    def replace_population(self, new_individuals):
        self.individuals = new_individuals

    def __len__(self):
        return self.size