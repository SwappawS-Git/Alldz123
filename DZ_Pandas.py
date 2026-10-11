
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sales_clean.csv")


sellers = df.groupby("seller")['total'].sum().sort_values(ascending=False)

sellers.to_csv("sellers.csv")

sellers.plot(kind="bar", title="увесь дохід", rot=0)

plt.tight_layout()
plt.savefig("sellers.png")