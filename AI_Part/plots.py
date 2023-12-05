import matplotlib.pyplot as plt
import numpy as np

X = ['Miscellaneous', 'Financials', 'IT', 'Energy', 'Utilities', 'Healthcare', 'Industrials']
X_range = np.arange(len(X))

y1 = np.array([0.16, 12.49, 3.11, 4.35, 6.13, 1.77, 2.77])
y2 = np.array([0.42, 7.48, 6.19, 0.62, 0.24, 8.94, 4.63])
y3 = np.array([0.72, 1.06, 2.56, 5.44, 0.08, 6.04, 0])
y4 = np.array([0, 0, 4.24, 0.12, 4.9, 8.84, 0])
y5 = np.array([0, 0, 0.32, 5.78, 0.11, 0, 0])
y6 = np.array([0, 0, 0.5, 0, 0, 0, 0])

plt.bar(X_range, y1)
plt.bar(X_range, y2, bottom=y1)
plt.bar(X_range, y3, bottom=y1+y2)
plt.bar(X_range, y4, bottom=y1+y2+y3)
plt.bar(X_range, y5, bottom=y1+y2+y3+y4)
plt.bar(X_range, y6, bottom=y1+y2+y3+y4+y5)

plt.xticks(X_range, X, fontdict={'rotation': 90})
plt.ylim(0, 30)
plt.grid()

plt.show()


def factorial(x):
