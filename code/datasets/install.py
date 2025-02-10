#Dataset from https://www.kaggle.com/datasets/thedevastator/dataset-for-solving-math-word-problems

import kagglehub

# Download latest version
path = kagglehub.dataset_download("thedevastator/dataset-for-solving-math-word-problems")

print("Path to dataset files:", path)