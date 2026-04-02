# 🏥 Diabetes Prediction API

A production-ready Machine Learning service that predicts diabetes risk based on diagnostic measurements.

## 🌟 Features
- **Data Engineering:** Automated cleaning of biological "zeros" using median imputation.
- **ML Model:** Random Forest Classifier (~73% Accuracy).
- **FastAPI Backend:** High-performance API with Pydantic data validation.
- **Interactive Docs:** Built-in Swagger UI for real-time testing.

## 🛠️ Tech Stack
- **Language:** Python 3.9+
- **ML Libraries:** Scikit-Learn, Pandas, NumPy
- **API Framework:** FastAPI, Uvicorn
- **DevOps:** Git, Docker (Optional)

## 🚀 Quick Start
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/yourusername/diabetes-prediction-api.git](https://github.com/yourusername/diabetes-prediction-api.git)
   cd diabetes-prediction-api
   
**Phase 1: Environment & Dependency Management**
The project began by isolating the development environment to ensure portability and avoid version conflicts.

Virtual Environment: Created using python -m venv venv to keep the project clean.

Dependency Installation: A requirements.txt file was generated to manage the following core libraries:

pandas & numpy: For data manipulation and numerical analysis.

scikit-learn: For machine learning algorithms and preprocessing.

fastapi & uvicorn: To build and serve the REST API.

joblib: For model serialization (saving the "brain").

matplotlib & seaborn: For data visualization during the analysis phase.

**Phase 2: Data Engineering & Cleaning**
Raw medical data often contains noise. In the Pima Indians dataset, missing values were incorrectly recorded as 0 for biological markers like Glucose, Blood Pressure, and BMI.

Imputation Strategy: I replaced these invalid zeros with NaN and applied Median Imputation. This prevents the model from being biased by "zero-value" outliers.

Preprocessing Pipeline: Created data_prep.py to automate this cleaning, resulting in cleaned_diabetes.csv.

**Phase 3: Machine Learning Pipeline**
Using the cleaned data, I developed a robust training script (train_model.py):

Feature Scaling: Applied StandardScaler to ensure all inputs (like Age vs. Insulin) are on the same scale, which is critical for the Random Forest algorithm.

Model Selection: Trained a Random Forest Classifier with 100 estimators.

Validation: Split the data into 80% training and 20% testing, achieving an accuracy of 73.38%.

Persistence: Saved both the trained model.pkl and the scaler.pkl to the models/ directory.

**Phase 4: API Development (Production Layer)**
The final stage was transforming the static model into a live service using FastAPI.

Schema Validation: Implemented Pydantic classes to strictly define the input data types, ensuring the API rejects invalid requests.

Inference Endpoint: Created a POST /predict route that accepts patient data, scales it using the saved scaler, and returns the prediction and confidence probability.

Documentation: Enabled FastAPI's automatic Swagger UI, allowing for interactive browser-based testing.

**Phase 5: Version Control & DevOps** 
Git Integration: Initialized a local repository and managed changes through meaningful commits.

Project Structure: Followed industry standards by separating code (app/), data (data/), and serialized models (models/).

Reproducibility: Updated the final requirements.txt using pip freeze to ensure the exact environment can be recreated by other developers.
