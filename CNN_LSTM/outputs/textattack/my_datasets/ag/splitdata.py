import pandas as pd
from sklearn.model_selection import train_test_split

# Load the original train.tsv
train_data = pd.read_csv("train.tsv", sep="\t", header=None, names=["Text", "Label"])

# Perform 80-20 split for train and validation
train_split, val_split = train_test_split(train_data, test_size=0.2, random_state=42)

# Save the splits to new files
train_split.to_csv("train.tsv", sep="\t", index=False, header=False)
val_split.to_csv("dev.tsv", sep="\t", index=False, header=False)
