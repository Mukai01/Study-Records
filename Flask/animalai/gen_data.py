import os, glob
from PIL import Image
import numpy as np
from sklearn import model_selection

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50

# 画像の読み込み
X = []
Y = []

for index, class_label in enumerate(classes):
    photos_dir = "./"+class_label
    files = glob.glob(photos_dir + "/*.jpg")
    for i, file_name in enumerate(files):
        if i >= 200: break
        image = Image.open(file_name)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X.append(data)
        Y.append(index)

# リストをarrayに変換
X = np.array(X)
Y = np.array(Y)

# データを分割
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save("./animal.npy", xy)