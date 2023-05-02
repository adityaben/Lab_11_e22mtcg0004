import flower_selection

selected_flowers = flower_selection.select_top_flowers()
flower_selection.serialize_flowers(selected_flowers)
deserialized_flowers = flower_selection.deserialize_flowers()

for flower in deserialized_flowers:
    print(flower.sepal_width, flower.petal_length, flower.petal_width)
