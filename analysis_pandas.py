import pandas as pd

df = pd.read_csv(
    "expenses.csv",
    header=None,
    names=["date", "category", "name", "cost"]
)

print(df)
sum = df['cost'].sum()
print(sum)