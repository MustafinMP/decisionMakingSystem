def product(vector: list[float]) -> float:
    """Перемножение ряда чисел"""
    p = 1
    for i in vector:
        p *= i
    return p


def estimation_of_the_eigenvector(table: list[list[float]], normalize_: bool = False) -> list[float]:
    vector = []
    for row in range(len(table)):
        vector.append(product(table[row]) ** 0.25)
    if normalize_:
        return normalize(vector)
    return vector


def normalize(vector: list[float]) -> list[float]:
    """Приведение к диапазону [0, 1]"""
    s = sum(vector)
    return list(map(lambda elem: elem / s, vector))