Follow these steps to replicate the environment and run the project locally.

1. Environment Setup 
First, clone the repository and create a virtual environment to isolate the dependencies.

DOS
git clone <your-repository-link>
cd diabetes-prediction-api
python -m venv venv
venv\Scripts\activate
2. Install Dependencies
Install the required libraries listed in the requirements.txt file.

DOS
pip install -r requirements.txt
3. Data Preprocessing
Run the cleaning script to handle missing values and prepare the dataset.

DOS
python data_prep.py
Output: SUCCESS: Cleaned data saved to data/cleaned_diabetes.csv

4. Model Training
Train the Random Forest model and save the serialized objects (.pkl).

DOS
python train_model.py
Output: Model Accuracy: 73.38%

Output: SUCCESS: Model and Scaler saved in /models folder!

5. Launch the API
Start the Uvicorn server to host the FastAPI application.

DOS
uvicorn app.main:app --reload
🧪 Testing the Endpoint
Once the server is running at http://127.0.0.1:8000, you can test it using cURL in a new terminal window:

DOS
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
  "Pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 80,
  "BMI": 25.5,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 30
}'
💡 Troubleshooting Tip
Missing Data: If data_prep.py fails, ensure diabetes.csv is placed inside the /data folder.

Port Conflict: If port 8000 is busy, run the API on a different port using:

uvicorn app.main:app --port 8080
