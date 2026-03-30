import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulate sales data
np.random.seed(42)

n_orders = 500

data = pd.DataFrame({
    "order_id": range(n_orders),
    "region": np.random.choice(["North", "South", "East", "West"], n_orders),
    "product": np.random.choice(["A", "B", "C"], n_orders),
    "revenue": np.random.randint(50, 500, n_orders),
    "month": np.random.choice(["Jan", "Feb", "Mar", "Apr"], n_orders)
})

# Summary
print("Total Revenue:", data["revenue"].sum())

print("\nRevenue by Region:")
print(data.groupby("region")["revenue"].sum())

print("\nRevenue by Product:")
print(data.groupby("product")["revenue"].sum())

# Visualization
data.groupby("region")["revenue"].sum().plot(kind="bar")
plt.title("Revenue by Region")
plt.ylabel("Revenue")
plt.show()

data.groupby("product")["revenue"].sum().plot(kind="bar")
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.show()
