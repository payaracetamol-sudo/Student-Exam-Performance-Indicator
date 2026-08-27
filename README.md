# Student Exam Performance Indicator

A machine learning web app that predicts a student's math score based on their background and their reading & writing scores. Built end-to-end: data ingestion, preprocessing, model training with hyperparameter tuning, and a Flask web interface.

## Overview

This project trains and compares several regression models (Random Forest, Decision Tree, Gradient Boosting, Linear Regression, K-Neighbors, XGBoost, CatBoost, AdaBoost) on a student performance dataset, selects the best-performing one, and serves predictions through a simple web form.

## Features

- End-to-end ML pipeline: ingestion → preprocessing → training → evaluation
- Automatic hyperparameter tuning with `GridSearchCV`
- Best-model selection based on R² score
- Flask web app with a clean, custom UI for entering student data and viewing predictions
- Modular, reusable pipeline components (`src/components`, `src/pipeline`)

## Tech stack

- **Language:** Python
- **ML/Data:** scikit-learn, XGBoost, CatBoost, pandas, numpy
- **Web:** Flask
- **Serialization:** dill

## Project structure

```
├── artifacts/                 # Generated data, trained model & preprocessor (not committed)
├── notebook/
│   └── data/                  # Raw dataset (stud.csv)
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
├── templates/
│   ├── index.html             # Landing page
│   └── home.html              # Prediction form + result
├── app.py                     # Flask entry point
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository
```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
```

2. Create a virtual environment (recommended)
```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

## Usage

### Train the model

```bash
python src/components/data_ingestion.py
```

This runs the full pipeline — ingesting `notebook/data/stud.csv`, splitting it into train/test sets, transforming the data, training and evaluating all models, and saving the best model and preprocessor to `artifacts/`.

### Run the web app

```bash
python app.py
```

Then open `http://127.0.0.1:5000/` in your browser, click **Start a prediction**, fill in the form, and submit to see the predicted math score.

## Purpose & limitations

This project was built primarily as a learning exercise in shipping a complete ML pipeline — from raw data to a deployed web interface — rather than as a production-ready tool. A few things worth keeping in mind:

- The dataset is small and the relationships it captures (e.g. reading/writing scores predicting math scores) are dataset-specific, not universal.
- Some inputs (gender, race/ethnicity, parental education) are demographic in nature. Using them as predictors is common in ML tutorials, but should be treated carefully in any real-world use — correlations in a dataset can reflect systemic inequities rather than anything predictive about an individual.
- This app is best understood as a demonstration of ML engineering and deployment, or as a starting point for aggregate, research-level analysis — not as a tool for making decisions about individual students.
