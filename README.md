# Data Governance and ML Pipeline

This repository contains the folder structure and resources for Sprint 1 tasks, focused on job role data analysis and machine learning modeling.

## Project Structure

- **data/raw**: Raw dataset files (e.g., `s_user_jobrole.csv`).
- **data/processed**: Cleaned and preprocessed data (e.g., `cleaned_s_user_jobrole.csv`).
- **models/baseline**: Baseline machine learning models (e.g., Logistic Regression, Random Forest).
- **models/advanced**: Advanced machine learning models (e.g., BERT-based transformers).
- **scripts/data_preprocessing**: Scripts for data cleaning and transformation.
- **scripts/model_training**: Scripts for training machine learning models.
- **notebooks**: Jupyter notebooks for exploratory analysis (e.g., `eda_report.json`).
- **config**: Configuration files for data validation (`data_config.yaml`) and model hyperparameters (`model_config.yaml`).
- **docs**: Documentation, including `Technical Specifications.txt`.

## Data Representation

- **Text Data**: Use embeddings (e.g., Word2Vec, GloVe, BERT) for textual descriptions like job roles and responsibilities.
- **Categorical Data**: Apply one-hot encoding for fields like `industries`, `department`, and `status`.
- **Numerical Data**: Normalize fields like `salary_range` and `experience` using Min-Max scaling or Z-score.
- **Date Fields**: Convert dates (e.g., `job_posting_date`, `application_deadline`) to numerical formats (days since epoch).

## Data Cleaning

- Remove rows with missing or invalid `id` values.
- Standardize text formats (capitalization, whitespace).
- Output in `.csv` format for ML pipelines.

## Data Governance

- **Primary Key**: `id` must be unique and non-null.
- **Validation Rules**: See `config/data_config.yaml` for details on categorical, numerical, text, and date validations.

## Recommended ML Algorithms

- **Logistic Regression**: For binary classification (e.g., predicting job status).
- **Random Forest**: For multi-class classification (e.g., predicting department or industries).
- **K-Means Clustering**: For unsupervised clustering of job roles.
- **BERT-based Models**: For NLP tasks on job descriptions.

## Installation and Usage

1. Clone the repository.
2. Install dependencies (e.g., via `pip install -r requirements.txt` if available).
3. Run preprocessing scripts in `scripts/data_preprocessing/`.
4. Train models using scripts in `scripts/model_training/`.
5. Explore data in `notebooks/`.

For detailed specs, see `docs/Technical Specifications.txt`.


# data_ingestion.py — Dataset Loading
## Purpose
- Safely loads the cleaned dataset from disk and makes it available as a Pandas DataFrame.
## What it does
- Verifies that the dataset file exists
- Loads the CSV into a DataFrame
- Prints dataset shape for verification
- Designed to be reusable across the project

## Why it matters
- This ensures consistent and reliable data loading across preprocessing, validation, and modeling steps.

# text_and_categorical_preprocessing.py — ML Preprocessing
## Purpose
- Prepares the cleaned dataset for machine learning by transforming text and categorical features into ML-friendly formats.
  ## What it does
- Cleans text fields (lowercasing, removing punctuation)
- Applies NLP preprocessing:

tokenization

stopword removal

lemmatization

- Creates both human-readable and ML-processed text columns
- Encodes categorical columns using LabelEncoder
- Stores encoders for future decoding if needed


## Why it matters
- Machine learning models cannot work directly with raw text or string categories.
- This step converts human-readable data into structured numerical representations.

# schema_validation.py — Data Validation
## Purpose
- Validates the dataset against a predefined schema to ensure structural consistency.
## What it does
- Loads expected schema from a JSON file

## Verifies:
- required columns
- unexpected extra columns
- data type correctness
- primary key uniqueness

Reports validation errors clearly


## Why it matters
- Even cleaned data can break pipelines if its structure changes.
- Schema validation prevents silent failures in analysis and ML workflows.

# categorical_staging.py — Categorical Standardization & Staging
## Purpose
Standardizes categorical values and stores them in a SQLite staging database.
## What it does
- Normalizes categorical text (strip spaces, lowercase)
- Extracts categorical columns
- Stores them in a SQLite staging table
- Enables reuse and consistency of category values


## Why it matters
- Categorical inconsistencies (e.g., IT vs it) can create incorrect model behavior.
- Staging provides a controlled layer between raw data and modeling.
## Overall Pipeline Flow
- Load cleaned dataset
- Validate schema consistency
- Preprocess text and encode categorical features
- Standardize and stage categorical values
- Dataset becomes ready for analysis and machine learning models

  



