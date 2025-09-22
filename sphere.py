def sphere(solution):
    """
    Avalia uma solução para o problema da esfera.
    https://www.sfu.ca/~ssurjano/spheref.html

    Args:
        solution: lista de floats representando as coordenadas da solução

    Returns:
        float: valor da função objetivo esfera
    """

    fitness = sum(x**2 for x in solution)

    return fitness


if __name__ == "__main__":
    # Testando a função de avaliação da esfera
    solution = [1.0, 2.5, 3.0]
    fit = sphere(solution)
    print(f"Fitness da solução {solution}: {fit}")

    # optimal solution
    solution = [0.0, 0.0, 0.0]
    fit = sphere(solution)
    print(f"Fitness da solução {solution}: {fit}")
