import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('carData.csv')

x = df['Year']
y = df['Selling_Price']

np.random.seed(20)
indices = np.arange(len(df))
np.random.shuffle(indices)
train_size = int(0.7 * len(df))
train_indices = indices[:train_size]
test_indices = indices[train_size:]

x_train, y_train = x[train_indices], y[train_indices]
x_test, y_test = x[test_indices], y[test_indices]

res = stats.linregress(x_train, y_train)

print(f'r-squared: {res.rvalue**2:.6f}')
print(f'r-value: {res.rvalue:.6f}')
print(f'p-value: {res.pvalue:.6f}')
print(f'slope: {res.slope:.6f}')
print(f'intercept: {res.intercept:.6f}')
print(f'stderr: {res.stderr:.6f}')

plt.plot(x_train, y_train, 'o', label='original data')
plt.plot(x_train, res.intercept + res.slope*x_train, 'r', label='fitted line')
plt.legend()
plt.show()

plt.plot(x_test, y_test, 'o', label='original data')
plt.plot(x_train, res.intercept + res.slope*x_train, 'r', label='fitted line')
plt.legend()
plt.show()