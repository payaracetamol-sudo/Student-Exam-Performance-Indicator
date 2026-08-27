# Student Exam Performance Indicator

A machine learning web application that predicts a student's math score based on demographic attributes and their reading and writing performance. Built end-to-end featuring data ingestion, preprocessing pipelines, automated model evaluation, hyperparameter tuning, and a Flask web interface.

## Overview

This project trains and compares multiple regression models—including Random Forest, Decision Tree, Gradient Boosting, Linear Regression, K-Neighbors, XGBoost, CatBoost, and AdaBoost—on a student performance dataset, selects the top-performing model based on $R^2$ score, and serves real-time predictions via a web form.

## Features

* **Modular ML Pipeline:** Clean separation of concerns across data ingestion, transformation, and model training (`src/components`).
* **Automated Model Evaluation:** Cross-evaluates models using `GridSearchCV` hyperparameter tuning.
* **Smart Model Persistence:** Evaluates test metrics and automatically serializes the best model (`artifacts/model.pkl`) and preprocessing pipeline (`artifacts/preprocessor.pkl`).
* **Flask Web Interface:** Web application allowing users to input student features and receive instant predictions.
* **Custom Error Handling & Logging:** Centralized logging (`src/logger.py`) and exception tracing (`src/exception.py`).

## Tech Stack

* **Language:** Python 3.10+
* **Machine Learning & Data Processing:** scikit-learn, XGBoost, CatBoost, pandas, NumPy
* **Web Framework:** Flask
* **Serialization & Utilities:** dill, joblib

## Project Structure