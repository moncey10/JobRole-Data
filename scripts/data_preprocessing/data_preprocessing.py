import pandas as pd
import re
from sklearn.preprocessing import LabelEncoder
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import os

# Set NLTK data path to virtual environment
nltk_data_path = os.path.join(os.path.dirname(__file__), '../../myenv/nltk_data')
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)
nltk.data.path.insert(0, nltk_data_path)

# Download NLTK resources if not present
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

def clean_text(text):
    """
    Clean text by removing special characters, extra spaces, etc.

    Args:
        text (str): Input text.

    Returns:
        str: Cleaned text.
    """
    if pd.isna(text):
        return ""
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    return text.strip().lower()

def preprocess_text(text):
    """
    Preprocess text for ML: tokenize, remove stopwords, lemmatize.

    Args:
        text (str): Input text.

    Returns:
        str: Preprocessed text.
    """
    if not text:
        return ""
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

def encode_categorical(df, categorical_columns):
    """
    Encode categorical columns using LabelEncoder.

    Args:
        df (pd.DataFrame): Input DataFrame.
        categorical_columns (list): List of categorical column names.

    Returns:
        pd.DataFrame: DataFrame with encoded columns.
    """
    encoders = {}
    for col in categorical_columns:
        if col in df.columns:
            le = LabelEncoder()
            df[col + '_encoded'] = le.fit_transform(df[col].astype(str))
            encoders[col] = le
    return df, encoders

def preprocess_data(df):
    """
    Main preprocessing function.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Preprocessed DataFrame.
    """
    # Identify text columns (assuming string columns with potential unstructured data)
    text_columns = ['description', 'responsibilities', 'benefits', 'keyword_tags']

    # Clean and preprocess text columns
    for col in text_columns:
        if col in df.columns:
            df[col + '_cleaned'] = df[col].apply(clean_text)
            df[col + '_processed'] = df[col + '_cleaned'].apply(preprocess_text)

    # Categorical columns to encode
    categorical_columns = ['industries', 'department', 'sub_department', 'jobrole', 'jobrole_category', 'status']

    # Encode categorical variables
    df, encoders = encode_categorical(df, categorical_columns)

    return df

if __name__ == "__main__":
    from data_ingestion import load_clean_dataset
    import os

    # Load data
    data_path = os.path.join(os.path.dirname(__file__), '../../data/processed/cleaned_s_user_jobrole.csv')
    df = load_clean_dataset(data_path)

    # Preprocess
    df_processed = preprocess_data(df)
    print("Preprocessing complete. Sample processed data:")
    print(df_processed[['description_cleaned', 'description_processed']].head())