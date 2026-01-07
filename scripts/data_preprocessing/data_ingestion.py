import pandas as pd
import os

def load_clean_dataset(file_path):
    """
    Load the clean dataset from the specified file path.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)
    print(f"Loaded dataset with shape: {df.shape}")
    return df

if __name__ == "__main__":
    # Path to the clean dataset
    data_path = os.path.join(os.path.dirname(__file__), '../../data/processed/cleaned_s_user_jobrole.csv')
    df = load_clean_dataset(data_path)
    print(df.head())