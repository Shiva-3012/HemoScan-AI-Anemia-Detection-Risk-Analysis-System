import pandas as pd

df = pd.read_csv("data/anemia_dataset.csv")

# simple cleaning example
df = df.dropna()

df.to_csv("data/cleaned_anemia_dataset.csv", index=False)
print("Preprocessing done ")