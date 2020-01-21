import pandas as pd
import matplotlib.pyplot as plt
plt.title("CONSUMO")
mtr = pd.read_csv("consumo.csv")
mtr.boxplot()
# plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)
plt.xlabel("data")
plt.ylabel("consumo")
plt.grid(True)
plt.show()