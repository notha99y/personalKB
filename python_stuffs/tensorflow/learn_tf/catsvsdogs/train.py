import os
from pathlib import Path

from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator

os.environ["TF_FORCE_GPU_ALLOW_GROWTH"] = "true"


height = 150
width = 150
channel = 3

batch_size = 32

model = Sequential(
    [
        Conv2D(
            16, (3, 3), activation="relu", input_shape=(height, width, channel)
        ),
        MaxPooling2D(2, 2),
        Conv2D(32, (3, 3), activation="relu"),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation="relu"),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(512, activation="relu"),
        Dense(1, activation="sigmoid"),
    ]
)

model.compile(
    optimizer=RMSprop(lr=1e-3),
    loss="binary_crossentropy",
    metrics=["accuracy"],
)


print(model.summary())


train_datagen = ImageDataGenerator(rescale=1 / 255.0)
train_dir = Path(".") / "dogvscat" / "train"
val_dir = Path(".") / "dogvscat" / "validation"
train_generator = train_datagen.flow_from_directory(
    train_dir,
    batch_size=batch_size,
    class_mode="binary",
    target_size=(height, width),
)

val_datagen = ImageDataGenerator(rescale=1 / 255.0)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    batch_size=batch_size,
    class_mode="binary",
    target_size=(height, width),
)

history = model.fit(
    train_generator,
    validation_data=val_generator,
    steps_per_epoch=100,
    epochs=15,
    validation_steps=50,
    verbose=1,
)

model.save('dog_cat_simple')
if __name__ == "__main__":
    pass
