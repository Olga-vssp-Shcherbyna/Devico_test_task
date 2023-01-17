import json

LEGS_NUM = {"chickens": 2, "cows": 4, "pigs": 4}


def legs_counter(file_path):
    with open(file_path, 'r') as f:
        animals = json.load(f)
    return sum([n_animals * LEGS_NUM[animal] for animal, n_animals in animals.items()])
