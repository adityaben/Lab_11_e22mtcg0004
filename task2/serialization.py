import pickle
from flower_selection import select_top_50_percent

class Petal:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Sepal:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Flower:
    def __init__(self, sepal, petal, name):
        self.sepal = sepal
        self.petal = petal
        self.name = name

def serialize_flowers(filename, flower_list):
    selected_flowers = select_top_50_percent(flower_list)
    for flower in selected_flowers:
        del flower.sepal.length
    with open(filename, 'wb') as f:
        pickle.dump(selected_flowers, f)
