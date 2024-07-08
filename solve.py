import numpy as np
import json
from eigenvector import *


class Result:
    def __init__(self):
        self.criterion_rating: list = list()
        self.all_criterion_rating: list[list] = list()
        self.objects_rating: list = list()

    def get(self):
        ...


def format_estimation(est: int) -> float:
    """Перевод оценочных отношений из формата (-inf, +inf) в формат (0, +inf) для последующих вычислений"""
    if est == 0:
        return 1
    if est >= 0:
        return est + 1
    else:
        return 1 / (1 - est)


def build_table(pairs: list[list[float, float, float]], size: int) -> list[list[float]]:
    """Построение таблицы по парам связей"""
    table = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        table[i][i] = 1
    for pair in pairs:
        table[pair[0]][pair[1]] = format_estimation(pair[2])
        table[pair[1]][pair[0]] = format_estimation(-pair[2])
    return table


def solve(data: dict) -> list[list[str, float]]:
    criterion_table: list[list[float]] = build_table(data['global_priority'], data['objects_count'])
    criterion_vector: list[float] = estimation_of_the_eigenvector(criterion_table, normalize_=True)

    others = {one_criterion: build_table(data['crit_prior'][one_criterion], data['criterion_count'])
              for one_criterion in data['crit_prior'].keys()}
    others_vectors = np.array([estimation_of_the_eigenvector(others[key], normalize_=True) for key in others.keys()])
    others_vectors = np.transpose(others_vectors)
    ratings = []
    for i in range(data['objects_count']):
        rating = 0
        for j in range(data['criterion_count']):
            rating += others_vectors[i][j] * criterion_vector[j]
        ratings.append([data['objects'][i], rating])
    ratings.sort(key=lambda x: -x[1])
    return ratings


# Press the green button in the gutter to run the script.
def run():
    with open('example_data.json') as file:
        data = json.load(file)
        for obj in solve(data):
            print(*obj)
