import pickle
from serialization import Flower

def deserialize_flowers(filename):
    with open(filename, 'rb') as f:
        flowers = pickle.load(f)
    return flowers

if __name__ == '__main__':
    flowers = deserialize_flowers('selected_flowers.pkl')
    for flower in flowers:
        print(flower.name)
