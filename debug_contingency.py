import pandas as pd
import numpy as np

# Load the processed data
data_path = 'data/processed/cleaned_s_user_jobrole.csv'
df = pd.read_csv(data_path)

print(f"Data loaded successfully. Shape: {df.shape}")
print("Columns in DataFrame:", df.columns.tolist())
print(df.head())

# Data Preprocessing
# Handle missing values if any
df.dropna(inplace=True)

# Encode categorical variables for correlation analysis
from sklearn.preprocessing import LabelEncoder

le_industries = LabelEncoder()
le_jobrole = LabelEncoder()

df['industries_encoded'] = le_industries.fit_transform(df['industries'])
df['jobrole_encoded'] = le_jobrole.fit_transform(df['jobrole'])

print("Data preprocessing completed.")
print(f"Unique industries: {len(le_industries.classes_)}")
print(f"Unique job roles: {len(le_jobrole.classes_)}")

# Now the cleaning part
required_cols = ["industries", "jobrole"]

df_clean = df.copy()

for col in required_cols:
    df_clean[col] = (
        df_clean[col]
        .astype(str)
        .str.strip()
        .replace({"": np.nan, "nan": np.nan})
    )

print("After cleaning:")
print(df_clean[required_cols].head(10))

# Drop rows where either column is missing
df_clean = df_clean.dropna(subset=required_cols)

print(f"Shape after dropna: {df_clean.shape}")

# Create contingency table
contingency_table = pd.crosstab(
    df_clean["industries"],
    df_clean["jobrole"]
)

print("Contingency table shape:", contingency_table.shape)
print(contingency_table.head())

if contingency_table.empty:
    print("Contingency table is empty!")
else:
    print("Not empty")