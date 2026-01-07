import pandas as pd
import json
import os

def load_schema(schema_path):
    """
    Load the data schema from JSON file.

    Args:
        schema_path (str): Path to the schema JSON file.

    Returns:
        dict: Schema dictionary.
    """
    with open(schema_path, 'r') as f:
        schema = json.load(f)
    return schema

def validate_schema(df, schema):
    """
    Validate the DataFrame against the schema.

    Args:
        df (pd.DataFrame): DataFrame to validate.
        schema (dict): Schema dictionary.

    Returns:
        dict: Validation results with errors if any.
    """
    errors = []

    # Check columns
    expected_columns = set(schema.get('columns', []))
    actual_columns = set(df.columns)
    if expected_columns != actual_columns:
        missing = expected_columns - actual_columns
        extra = actual_columns - expected_columns
        if missing:
            errors.append(f"Missing columns: {list(missing)}")
        if extra:
            errors.append(f"Extra columns: {list(extra)}")

    # Check data types
    data_types = schema.get('data_types', {})
    for col, expected_dtype in data_types.items():
        if col in df.columns:
            actual_dtype = str(df[col].dtype)
            # Map pandas dtypes to schema types
            dtype_mapping = {
                'int64': 'int',
                'object': 'str',
                'float64': 'float',
                'bool': 'bool'
            }
            mapped_dtype = dtype_mapping.get(actual_dtype, actual_dtype)
            if mapped_dtype != expected_dtype:
                errors.append(f"Column '{col}': expected {expected_dtype}, got {mapped_dtype}")

    # Check primary key
    primary_key = schema.get('primary_key')
    if primary_key and primary_key in df.columns:
        if df[primary_key].duplicated().any():
            errors.append(f"Primary key '{primary_key}' has duplicates")

    return {'valid': len(errors) == 0, 'errors': errors}

if __name__ == "__main__":
    # Paths
    schema_path = os.path.join(os.path.dirname(__file__), '../../config/data_schema.json')
    data_path = os.path.join(os.path.dirname(__file__), '../../data/processed/cleaned_s_user_jobrole.csv')

    # Load schema and data
    schema = load_schema(schema_path)
    df = pd.read_csv(data_path)

    # Validate
    result = validate_schema(df, schema)
    if result['valid']:
        print("Schema validation passed.")
    else:
        print("Schema validation failed with errors:")
        for error in result['errors']:
            print(f"- {error}")