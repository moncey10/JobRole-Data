import sqlite3
import pandas as pd
import os

def create_staging_table(db_path, table_name, categorical_columns, df):
    """
    Create a staging table for categorical variables.

    Args:
        db_path (str): Path to the SQLite database.
        table_name (str): Name of the staging table.
        categorical_columns (list): List of categorical column names.
        df (pd.DataFrame): DataFrame with data.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table with columns for each categorical variable
    columns = ['id INTEGER PRIMARY KEY AUTOINCREMENT']
    for col in categorical_columns:
        columns.append(f"{col} TEXT")
    create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"

    cursor.execute(create_query)

    # Insert unique combinations or all rows? For staging, perhaps insert all rows.
    # But to standardize, maybe insert unique values per column.

    # For simplicity, insert all rows into the table.
    df_categorical = df[categorical_columns]
    df_categorical.to_sql(table_name, conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()
    print(f"Staging table '{table_name}' created and populated in {db_path}")

def standardize_categoricals(df, categorical_columns):
    """
    Standardize categorical variables (e.g., strip, lower case).

    Args:
        df (pd.DataFrame): Input DataFrame.
        categorical_columns (list): List of categorical column names.

    Returns:
        pd.DataFrame: DataFrame with standardized categoricals.
    """
    for col in categorical_columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.lower()
    return df

if __name__ == "__main__":
    from data_ingestion import load_clean_dataset

    # Load data
    data_path = os.path.join(os.path.dirname(__file__), '../../data/processed/cleaned_s_user_jobrole.csv')
    df = load_clean_dataset(data_path)

    # Categorical columns
    categorical_columns = ['industries', 'department', 'sub_department', 'jobrole', 'jobrole_category', 'status']

    # Standardize
    df = standardize_categoricals(df, categorical_columns)

    # Database path
    db_path = os.path.join(os.path.dirname(__file__), '../../data/staging.db')
    table_name = 'categorical_staging'

    # Create staging table
    create_staging_table(db_path, table_name, categorical_columns, df)

    # Verify
    conn = sqlite3.connect(db_path)
    result = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 5", conn)
    print("Sample from staging table:")
    print(result)
    conn.close()