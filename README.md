# 📊 Medical Insurance Cost Prediction using Machine Learning

## 📌 Project Overview
This project predicts **medical insurance charges** based on key factors such as **age, BMI, number of children, smoking status, gender, and region**. Using machine learning models and a Flask web app, the project provides **real-time predictions** and insights into the primary cost drivers, helping insurance providers, policyholders, and data enthusiasts understand **how different features affect insurance costs**.

---

## 🔍 Key Findings
- 🚬 **Smoking status is the most significant factor**, drastically increasing insurance charges.  
- 📈 **Age and BMI are strongly correlated** with higher insurance costs.  
- 📊 **Linear Regression achieved an R² score of ~0.75**, explaining a large portion of variance.  
- 🌳 **Random Forest and XGBoost outperform simpler models**, with test R² scores of **0.82 and 0.86**, respectively.  
- ⚖ **Feature importance analysis confirms smoking, age, and BMI as top predictors**.  

---

## 📁 Dataset Information
The dataset contains **1,338 records** with the following columns:

| Column      | Description |
|------------|-------------|
| `age`      | Age of the insured person |
| `sex`      | Gender (`male` or `female`) |
| `bmi`      | Body Mass Index |
| `children` | Number of children covered by insurance |
| `smoker`   | Whether the insured is a smoker (`yes` or `no`) |
| `region`   | Geographical region (`northeast`, `northwest`, `southeast`, `southwest`) |
| `charges`  | Insurance charges (target variable) |

---

## 🛠 Technologies Used
- **Python** – Programming language  
- **Pandas & NumPy** – Data manipulation & numeric operations  
- **Matplotlib & Seaborn** – Exploratory data visualization  
- **Scikit-Learn** – Machine learning models and evaluation  
- **XGBoost** – Gradient boosting algorithm for improved accuracy  
- **Flask** – Web framework for deploying the model as an API  
- **Chart.js** – Interactive charts in the Flask app  

---

## 📂 Project Structure

<pre lang="markdown">

Medical-Insurance-Prediction/
│── data/
│   └── insurance.csv  # Dataset
│── notebooks/
│   ├── EDA.ipynb  # Exploratory Data Analysis
│   └── Model_Training.ipynb  # Model training and evaluation
│── src/
│   ├── data_preprocessing.py  # Data cleaning & feature engineering
│   └── train_model.py  # Model training script
│── models/
│   ├── model.pkl  # Serialized trained model
│   └── scaler.pkl  # Feature scaler
│── templates/
│   ├── form.html  # Input form for Flask app
│   └── result.html  # Prediction result page with chart
│── app.py  # Flask API & web app
│── requirements.txt  # Python dependencies
│── README.md  # Project documentation

</pre>

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/HenryMorganDibie/medical-insurance-prediction
cd Medical-Insurance-Prediction
````

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
# MacOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Notebooks (Optional)

Explore the dataset, perform EDA, and train models:

```bash
jupyter notebook
```

---

## 🤖 Machine Learning Models Used

| Model             | Train R² | Test R² | RMSE (Test) |
| ----------------- | -------- | ------- | ----------- |
| Linear Regression | 0.75     | 0.74    | 6,194       |
| Decision Tree     | 1.00     | 0.76    | 5,800       |
| Random Forest     | 0.97     | 0.82    | 4,901       |
| XGBoost           | 0.90     | 0.86    | 4,201       |

**Key Insights:** Ensemble methods like Random Forest and XGBoost better capture non-linear relationships and feature interactions, improving prediction accuracy.

---

## 📊 Model Evaluation Metrics

* **R² Score** – Variance explained by the model
* **RMSE (Root Mean Squared Error)** – Prediction error in dollars
* **MAE (Mean Absolute Error)** – Average magnitude of errors

---

## 🔥 Using the Prediction Web App

The Flask app provides a **user-friendly interface** for predicting insurance costs.

### 1️⃣ Start the Flask Server

```bash
python app.py
```

This starts a local web server (default: `http://127.0.0.1:5000/`).

### 2️⃣ Input Features

The form accepts:

* Age, BMI, Number of children
* Sex, Smoking status
* Region

### 3️⃣ View Results

The result page displays:

* **Predicted insurance charge**
* **Comparison chart**: User prediction vs. dataset average, smoker average, and non-smoker average

📌 The chart is **interactive** using Chart.js for visualization.

---

## 🔮 Future Improvements

* Incorporate **Deep Learning (ANNs)** for enhanced predictions
* Implement **SHAP values** for detailed feature impact explanation
* Deploy as a **Streamlit or React web app** for a modern UI
* Expand dataset to include **larger regions and real patient data**

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to your branch (`git push origin feature-name`)
5. Open a pull request

---

## 🏆 Acknowledgments

Inspired by **real-world health insurance analytics**. Thanks to the **open-source community** for Python libraries and tools.

📧 Contact: [henrymorgan273@yahoo.com](mailto:henrymorgan273@yahoo.com)
🌐 LinkedIn: [Henry C. Dibie](https://www.linkedin.com/in/kinghenrymorgan/)

---

## 📜 License

This project is licensed under the **MIT License** – free to use, modify, and share.

```

---