#import the needed libraries
from data_handler import load_data, to_batches         # yes, you can import your code. Cool!
import matplotlib.pyplot as plt
import torch.optim as optim
import torch.nn as nn

import matplotlib.pyplot as plt
import numpy as np

from model import FullyConnected

path = './Chapter 3/03. MLP Regression/data/turkish_stocks.csv'
x_train, x_test, y_train, y_test = load_data(path)

fc = FullyConnected(8, 1)
optimizer = optim.SGD(fc.parameters(), lr=3e-3)
loss_func = nn.MSELoss()

epochs = 500
loss_list = []
for i in range(epochs):
    running_loss = 0
    
    x_train_batch, x_test_batch, y_train_batch, y_test_batch = to_batches(x_train, x_test, y_train, y_test, 100)

    for x_batch, y_batch in zip(x_train_batch, y_train_batch):
        optimizer.zero_grad()

        prediction = fc.forward(x_batch)
        loss = loss_func(prediction, y_batch)

        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    print(f'Epoch number: {i}, loss: {running_loss/x_train_batch.shape[0]}')
    loss_list.append(running_loss/x_train_batch.shape[0])

plt.plot(loss_list)
plt.show()
# Remember to validate your model: with torch.no_grad() ...... model.eval .........model.train












# features = T.rand((3,))

# # print(features)

# fully_con_net = FullyConnected(3, 1)

# print(fully_con_net.forward(features))

# # to Train a model
# # define loss function --> criterion = torch.nn.BCELoss() 
# # define optimizer      --> optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# # training loop ---> define "epochs" ---> epoch = lasts until you pass ALL your samples to the model (better by batches)
# #   for each train_batch:
# #       step1: reset the gradients  --> optimizer.zero_grad()
# #       step2: prediction           --> pred = model.forward(X)
# #       step3: compute loss         --> loss = criterion(pred, Y)
# #       step4: backprop             --> loss.backward()
# #       step5: store the weight     --> criterion.step()
# #   # model evaluation
# #   model.eval()
# #   with torch.no_grad():
# #       for each test_batch:
# #       step1: pretiction
# #       step2: compute loss
# #   model.train()