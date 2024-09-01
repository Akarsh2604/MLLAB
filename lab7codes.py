import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neural_network import MLPClassifier

#A1
def summ_unit(x, w):
    return np.dot(x, w)
def step_func(x):
    return 1 if x >= 0 else 0
def bipolar_step_func(x):
    return 1 if x >= 0 else -1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def tanh(x):
    return np.tanh(x)
def relu(x):
    return max(0, x)
def leaky_relu(x, alpha=0.01):
    return x if x > 0 else alpha * x
def calc_error(t, o):
    return t - o

#A2
def perc_learn(x, t, w, lr, act_func, max_epochs=1000, thresh=0.002):
    epoch = 0
    errs = []
    
    while epoch < max_epochs:
        epoch_err = 0
        for i in range(len(x)):
            w_sum = summ_unit(x[i], w)
            out = act_func(w_sum)
            err = calc_error(t[i], out)
            w += lr * err * x[i]
            epoch_err += err**2

        errs.append(epoch_err)
        epoch += 1
        if epoch_err <= thresh:
            break

    return w, errs, epoch

x = np.array([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])  
t = np.array([0, 0, 0, 1])
w = np.array([10, 0.2, -0.75])
final_w, errs, epoch = perc_learn(x, t, w, 0.05, step_func)

plt.plot(range(epoch), errs)
plt.xlabel('Epochs')
plt.ylabel('Sum-Squared Error')
plt.title('Error vs Epochs')
plt.show()

#A3
act_funcs = [step_func, bipolar_step_func, sigmoid, relu]
func_names = ['Step', 'Bipolar Step', 'Sigmoid', 'ReLU']

for func, name in zip(act_funcs, func_names):
    final_w, errs, epoch = perc_learn(x, t, w, 0.05, func)
    plt.plot(range(epoch), errs, label=name)

plt.xlabel('Epochs')
plt.ylabel('Sum-Squared Error')
plt.title('Error vs Epochs for Different Activation Functions')
plt.legend()
plt.show()

#A4
lrs = [0.1 * i for i in range(1, 11)]
iters = []

for lr in lrs:
    _, _, epoch = perc_learn(x, t, w, lr, step_func)
    iters.append(epoch)

plt.plot(lrs, iters)
plt.xlabel('Learning Rate')
plt.ylabel('Iterations to Converge')
plt.title('Learning Rate vs Iterations')
plt.show()

#A5
xor_x = np.array([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
xor_t = np.array([0, 1, 1, 0])
final_w, errs, epoch = perc_learn(xor_x, xor_t, w, 0.05, step_func)

plt.plot(range(epoch), errs)
plt.xlabel('Epochs')
plt.ylabel('Sum-Squared Error')
plt.title('Error vs Epochs for XOR Gate')
plt.show()

#A6
df = pd.read_csv(r"C:\Users\vvmad\Downloads\5th\ML\HM7 - Java\java_cc_embed_data.csv")
print(df.columns)
df.columns = df.columns.str.strip()
df['Final_Marks'] = df['Final_Marks'].apply(lambda x: 1 if x == 'Yes' else 0)
w = np.random.rand(x.shape[1])
lr = 0.05
final_w, errs, epoch = perc_learn(x, t, w, lr, sigmoid)

plt.plot(range(epoch), errs)
plt.xlabel('Epochs')
plt.ylabel('Sum-Squared Error')
plt.title('Error vs Epochs for Customer Data Perceptron')
plt.show()

#A7
pseudo_inv_w = np.dot(np.linalg.pinv(x), t)
print("Weights from Pseudo-Inverse Method:", pseudo_inv_w)
print("Final Weights from Perceptron Learning:", final_w)

#A8
class NN:
    def _init_(self, in_size, hid_size, out_size, lr=0.05):
        self.w_in_hid = np.random.rand(in_size, hid_size)
        self.w_hid_out = np.random.rand(hid_size, out_size)
        self.lr = lr

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, x):
        self.h_in = np.dot(x, self.w_in_hid)
        self.h_out = self.sigmoid(self.h_in)
        self.f_in = np.dot(self.h_out, self.w_hid_out)
        self.f_out = self.sigmoid(self.f_in)
        return self.f_out

    def backward(self, x, t, out):
        err = t - out
        d_out = err * self.sigmoid_derivative(out)
        err_hid = d_out.dot(self.w_hid_out.T)
        d_hid = err_hid * self.sigmoid_derivative(self.h_out)
        self.w_hid_out += self.h_out.T.dot(d_out) * self.lr
        self.w_in_hid += x.T.dot(d_hid) * self.lr

    def train(self, x, t, epochs=1000, thresh=0.002):
        errs = []
        for epoch in range(epochs):
            out = self.forward(x)
            self.backward(x, t, out)
            epoch_err = np.mean((t - out) ** 2)
            errs.append(epoch_err)
            if epoch_err <= thresh:
                break
        return errs

x = np.array([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])  
t = np.array([[0], [0], [0], [1]])
nn = NN(in_size=3, hid_size=2, out_size=1)
errs = nn.train(x, t)

plt.plot(errs)
plt.xlabel('Epochs')
plt.ylabel('Mean Squared Error')
plt.title('Error vs Epochs for Neural Network AND Gate')
plt.show()

#A9
xor_x = np.array([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
xor_t = np.array([[0], [1], [1], [0]])
nn = NN(in_size=3, hid_size=2, out_size=1)
errs = nn.train(xor_x, xor_t)

plt.plot(errs)
plt.xlabel('Epochs')
plt.ylabel('Mean Squared Error')
plt.title('Error vs Epochs for Neural Network XOR Gate')
plt.show()

#A10
def perc_two_out(x, t, w, lr, act_func, max_epochs=1000, thresh=0.002):
    epoch = 0
    errs = []

    while epoch < max_epochs:
        epoch_err = 0
        for i in range(len(x)):
            w_sum = summ_unit(x[i], w)
            out = np.array([act_func(w_sum[0]), act_func(w_sum[1])])
            err = t[i] - out
            w += lr * np.outer(x[i], err)
            epoch_err += np.sum(err**2)

        errs.append(epoch_err)
        epoch += 1
        if epoch_err <= thresh:
            break

    return w, errs, epoch

t = np.array([[1, 0], [1, 0], [1, 0], [0, 1]])
w = np.random.rand(x.shape[1], 2)
final_w, errs, epoch = perc_two_out(x, t, w, 0.05, step_func)
plt.plot(range(epoch), errs)
plt.xlabel('Epochs')
plt.ylabel('Sum-Squared Error')
plt.title('Error vs Epochs for 2 Output Nodes')
plt.show()

#A11
x = np.array([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])  
t = np.array([0, 0, 0, 1]) 
clf = MLPClassifier(hidden_layer_sizes=(2,), activation='logistic', learning_rate_init=0.05, max_iter=1000)
clf.fit(x[:, 1:], t)  
print("AND Gate Prediction:", clf.predict(x[:, 1:]))
xor_x = np.array([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
xor_t = np.array([0, 1, 1, 0])  
clf = MLPClassifier(hidden_layer_sizes=(2,), activation='logistic', learning_rate_init=0.05, max_iter=1000)
clf.fit(xor_x[:, 1:], xor_t)  
print("XOR Gate Prediction:", clf.predict(xor_x[:, 1:]))

#A12
clf = MLPClassifier(hidden_layer_sizes=(2,), activation='logistic', learning_rate_init=0.05, max_iter=1000)
clf.fit(x[:, 1:], t)  
preds = clf.predict(x[:, 1:])
print("Project Data Predictions:", preds)
