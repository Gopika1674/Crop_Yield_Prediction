🌾 Crop Yield Prediction using Machine Learning

📌 Project Overview

Crop yield prediction is a critical challenge in agriculture as it directly impacts food security and farmers’ income. This project leverages machine learning models to predict crop yield based on factors like:
Crop type
Area (land size)
Annual rainfall
Fertilizer usage
Pesticide usage
By analyzing these inputs, the model predicts the expected yield (in hectograms per hectare), helping farmers and policymakers make better decisions.


🎯 Objectives
1.Predict crop yield more accurately than traditional methods.
2.Provide a simple web-based interface (using Streamlit) for easy usage.
3.Enable data-driven decision-making in agriculture.


🛠️ Tech Stack
1.Python 3.11
2.Machine Learning Libraries:
    pandas, numpy → Data preprocessing
    scikit-learn → Model training & evaluation
3.Visualization: matplotlib, seaborn
4.Deployment: Streamlit (interactive web app)
5.Version Control: Git & GitHub


📂 Project Structure
Crop_Yield_Prediction/
│── app/
│   └── app.py              # Streamlit app for deployment
│── data/
│   └── crop_yield.csv      # Dataset
│── models/
│   └── model.pkl           # Trained ML model (saved using joblib/pickle)
│── notebooks/
│   └── EDA.ipynb           # Jupyter Notebook for exploration & preprocessing
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation


⚙️ How It Works

1.Data Collection & Preprocessing
    Cleaned missing values
    Encoded categorical features (Crop type, etc.)
    Scaled numerical features

2.Model Training
    Tested multiple ML algorithms (Linear Regression, Random Forest, Decision Tree, XGBoost).
    Selected the best-performing model based on R² score & RMSE.

3.Deployment
    Built a Streamlit web app where users can input rainfall, fertilizer usage, etc.
    Model predicts expected yield instantly.


🚀 How to Run Locally

1.Clone this repository:
git clone https://github.com/Gopika1674/Crop_Yield_Prediction.git
cd Crop_Yield_Prediction

2.Install dependencies:
pip install -r requirements.txt

3.Run the Streamlit app:
streamlit run app/app.py

4.Open in browser: http://localhost:8501


📊 Results & Insights
Random Forest model achieved the highest accuracy with minimal error.
Key features influencing yield:
    Rainfall
    Fertilizer usage
    Crop type


🌍 Future Improvements
1.Integrate real-time weather data APIs.
2.Add SHAP Explainability to interpret predictions.
3.Extend dataset with soil quality & satellite data.
4.Deploy on cloud platforms (Heroku/Streamlit Cloud) for public use.


👩‍💻 Author
Gopika Saravanan
📧 Email: gopikasaravanan2004@gmail.com
🔗 GitHub: Gopika1674
