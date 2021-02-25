"""
Visualizing Intermediate Representations
"""
import os
import random
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from tensorflow.keras.models import Model, load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img

os.environ["TF_FORCE_GPU_ALLOW_GROWTH"] = "true"

model = load_model("dog_cat_simple")

successive_outputs = [layer.output for layer in model.layers[1:]]
vis_model = Model(inputs=model.input, outputs=successive_outputs)

print(vis_model)

cat_fnames = list((Path(".") / "dogvscat" / "train" / "cats").glob("*.jpg"))
dog_fnames = list((Path(".") / "dogvscat" / "train" / "dogs").glob("*.jpg"))

random_fname = random.choice(cat_fnames + dog_fnames)
img = load_img(random_fname, target_size=(150, 150))
plt.imshow(img)
plt.show()
x = img_to_array(img)
x = np.expand_dims(x, axis=0)
x /= 255

successive_feature_maps = vis_model.predict(x)

layer_names = [layer.name for layer in model.layers]

print(len(successive_feature_maps), len(layer_names))


for layer_name, feature_map in zip(layer_names, successive_feature_maps):

    if len(feature_map.shape) == 4:

        # -------------------------------------------
        # Just do this for the conv / maxpool layers, not the fully-connected layers
        # -------------------------------------------
        n_features = feature_map.shape[
            -1
        ]  # number of features in the feature map
        size = feature_map.shape[
            1
        ]  # feature map shape (1, size, size, n_features)

        # We will tile our images in this matrix
        display_grid = np.zeros((size, size * n_features))

        # -------------------------------------------------
        # Postprocess the feature to be visually palatable
        # -------------------------------------------------
        for i in range(n_features):
            x = feature_map[0, :, :, i]
            x -= x.mean()
            x /= x.std()
            x *= 64
            x += 128
            x = np.clip(x, 0, 255).astype("uint8")
            display_grid[
                :, i * size : (i + 1) * size
            ] = x  # Tile each filter into a horizontal grid

        # -----------------
        # Display the grid
        # -----------------

        scale = 20.0 / n_features
        plt.figure(figsize=(scale * n_features, scale))
        plt.title(layer_name)
        plt.grid(False)
        plt.imshow(display_grid, aspect="auto", cmap="viridis")

plt.show()
