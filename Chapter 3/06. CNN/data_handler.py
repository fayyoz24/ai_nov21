
# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'

import matplotlib.pyplot as plt

import torch
from torchvision import datasets, transforms


# train_transform = # your code here

# test_transform = # your code here
# data_dir = "./Chapter 3/06. CNN/data/train" # or the path where you have downloaded the dataset

# train_data = datasets.ImageFolder(data_dir + '/train')#, transform=train_transforms)
def olma():

    test_data = datasets.ImageFolder('./Chapter 3/06. CNN/data/test1')
    return test_data
