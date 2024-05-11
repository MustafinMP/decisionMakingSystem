import json
from eigenvector import *


def format_estimation(est: int) -> float:
    if est == 0:
        return 1
    if est >= 0:
        return est + 1
    else:
        return 1 / (1 - est)


def build_table(pairs, size):
    table = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        table[i][i] = 1
    for pair in pairs:
        table[pair[0]][pair[1]] = format_estimation(pair[2])
        table[pair[1]][pair[0]] = format_estimation(-pair[2])
    return table


def solve(data: dict):
    criterion_table = build_table(data['global_priority'], data['objects_count'])
    criterion_vector = normalize(estimation_of_the_eigenvector(criterion_table))
    others = {criterion: build_table(data['crit_prior'][criterion], data['criterion_count'])
              for criterion in data['crit_prior'].keys()}
    others_vectors = np.array([normalize(estimation_of_the_eigenvector(others[key])) for key in others.keys()])
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
if __name__ == '__main__':
    with open('example_data.json') as file:
        data = json.load(file)
        for obj in solve(data):
            print(*obj)
