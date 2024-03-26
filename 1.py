import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

year = [2020, 2021, 2022, 2023, 2024]
money = [15000, 18000, 19200, 21000, 23000]
size = np.array(money) / 100

sns.barplot(x=year, y=money, hue=money, palette='light:pink', dodge=False)
plt.show()
