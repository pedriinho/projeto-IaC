import pandas as pd
import matplotlib.pyplot as plt
mtr = pd.read_csv("consumo.csv")
mtr.boxplot()
plt.show()