import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = sns.load_dataset("iris")
# print(data)

#mean(avg), mode, median

avg_petal_length = data['petal_length'].mean()

print("Average petal length:", avg_petal_length)

avg_petal_length = np.mean(data['petal_length'])

print("Average petal length:", avg_petal_length)

mode_petal_length = data['petal_length'].mode()

print("Petal mode:", mode_petal_length)

median_petal_length = data['petal_length'].median()

print("Petal median:", median_petal_length)