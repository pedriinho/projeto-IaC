import pandas as pd
import matplotlib.pyplot as plt
mtr = pd.read_csv("consumo.csv")
anos = mtr[143:153]
x = anos["data"]
y = anos["consumo"]
done = plt.plot(x, y)
plt.show(done)