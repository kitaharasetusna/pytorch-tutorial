import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# Toy dataset
x_train = np.array([[3.3], [4.4], [5.5], [6.71], [6.93], [4.168], 
                    [9.779], [6.182], [7.59], [2.167], [7.042], 
                    [10.791], [5.313], [7.997], [3.1]], dtype=np.float32)

y_train = np.array([[1.7], [2.76], [2.09], [3.19], [1.694], [1.573], 
                    [3.366], [2.596], [2.53], [1.221], [2.827], 
                    [3.465], [1.65], [2.904], [1.3]], dtype=np.float32)

# epoch_num = 100
# learning_rate = 0.01
#
# input_size, output_size = 1, 1
# model = nn.Linear(input_size, output_size)
#
# optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
# criterion = nn.MSELoss()
#
# for epoch in range(1, epoch_num+1):
#     inputs = torch.from_numpy(x_train)
#     targets = torch.from_numpy(y_train)
#
#     outputs = model(inputs)
#     loss = criterion(outputs, targets)
#
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()
#
#     if epoch%10==0:
#         print('epoch: [{}/{}], loss: {}'.format(epoch, epoch_num,loss.item()))
#
# predicted = model(torch.from_numpy(x_train)).detach().numpy()
# plt.plot(x_train, y_train, 'ro', label='orgin_data')
# plt.plot(x_train, predicted, label='fitted_data')
# plt.legend()
# plt.show()
#
# torch.save(model, 'model.ckpt')

model = torch.load('model.ckpt')
predicted = model(torch.from_numpy(x_train)).detach().numpy()
plt.plot(x_train, y_train, 'ro', label='origin_data')
plt.plot(x_train, predicted, label='fitted_data')
plt.show()

