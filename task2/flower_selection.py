import pickle
from selection_score import calculate_selection_score
from iris import Flower

def select_top_flowers():
    flowers = []
    with open('iris.data', 'r') as f:
        for line in f:
            parts = line.split(',')
            if len(parts) == 5:
                sepal_width = float(parts[1])
                petal_length = float(parts[2])
                petal_width = float(parts[3])
                flower = Flower(sepal_width, petal_length, petal_width)
                flowers.append(flower)
    scores = []
    for flower in flowers:
        score = calculate_selection_score(flower)
        scores.append(score)
    num_top_flowers = len(flowers) // 2
    top_flowers = []
    for i in range(num_top_flowers):
        max_index = scores.index(max(scores))
        top_flowers.append(flowers[max_index])
        scores.pop(max_index)
        flowers.pop(max_index)
    return top_flowers

def serialize_flowers(flowers):
    with open('selected_flowers.pkl', 'wb') as f:
        for flower in flowers:
            pickle.dump({'sepal_width': flower.sepal_width,
                         'petal_length': flower.petal_length,
                         'petal_width': flower.petal_width}, f)

def deserialize_flowers():
    flowers = []
    with open('selected_flowers.pkl', 'rb') as f:
        while True:
            try:
                flower_data = pickle.load(f)
                flower = Flower(flower_data['sepal_width'], flower_data['petal_length'], flower_data['petal_width'])
                flowers.append(flower)
            except EOFError:
                break
    return flowers
