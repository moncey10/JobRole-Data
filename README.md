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
