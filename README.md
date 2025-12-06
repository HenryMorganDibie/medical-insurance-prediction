# 📊 Medical Insurance Cost Prediction using Machine Learning

## 📌 Project Overview
This project predicts **medical insurance charges** based on key factors such as **age, BMI, number of children, smoking status, gender, and region**. Using a **Random Forest model** and a **Flask web app**, it provides **real-time predictions** and insights into the main cost drivers, helping insurance providers, policyholders, and data enthusiasts understand **how different features affect insurance costs**.

---

## 📷 Flask App Screenshots

### Medical Insurance Charge Prediction
![Medical Insurance Charge Prediction](screenshots/Medical%20Insurance%20Charge%20Prediction.JPG)

### Predicted Insurance Charge with Smoker & Non-Smoker Avg
![Predicted Insurance Charge with Smoker & Non-Smoker Avg](screenshots/Predicted%20Insurance%20Charge%20with%20Smoker%20&%20Nonsmoker%20avg.JPG)

---

## 🔍 Key Findings
- 🚬 **Smoking status is the most significant factor**, drastically increasing insurance charges.  
- 📈 **Age and BMI are strongly correlated** with higher insurance costs.  
- 🌳 **Random Forest achieved excellent performance**, capturing non-linear relationships and interactions between features.  
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
│   └── Model_Training.ipynb  # Random Forest training & evaluation
│── src/
│   ├── data_preprocessing.py  # Data cleaning & feature engineering
│   └── train_model.py  # Random Forest training script
│── models/
│   ├── model.pkl  # Serialized trained Random Forest model
│   └── scaler.pkl  # Feature scaler
│── templates/
│   ├── form.html  # Input form for Flask app
│   └── result.html  # Prediction result page with chart
│── app.py  # Flask API & web app
│── requirements.txt  # Python dependencies
│── README.md  # Project documentation
│── screenshots/  # Flask app screenshots
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

Explore the dataset and Random Forest model training:

```bash
jupyter notebook
```

---

## 🤖 Machine Learning Model Used

| Model         | Train R² | Test R² | RMSE (Test) |
| ------------- | -------- | ------- | ----------- |
| Random Forest | 0.97     | 0.82    | 4,901       |

**Key Insight:** Random Forest captures non-linear relationships and interactions between features, providing accurate predictions of insurance charges.

---

## 📊 Model Evaluation Metrics

* **R² Score** – Measures variance explained by the model
* **RMSE (Root Mean Squared Error)** – Prediction error in dollars
* **MAE (Mean Absolute Error)** – Average magnitude of errors

---

## 🔥 Using the Prediction Web App

The Flask app provides a **user-friendly interface** for predicting insurance costs.

### 1️⃣ Start the Flask Server

```bash
python app.py
```

Default server: `http://127.0.0.1:5000/`

### 2️⃣ Input Features

The form accepts:

* Age, BMI, Number of children
* Sex, Smoking status
* Region

### 3️⃣ View Results

* **Predicted insurance charge**
* **Comparison chart**: User prediction vs. dataset average, smoker average, and non-smoker average
* The chart is **interactive** using Chart.js

---

## 🔮 Future Improvements

* Incorporate **Deep Learning (ANNs)** for improved predictions
* Implement **SHAP values** for detailed feature impact explanation
* Deploy as a **Streamlit or React web app**
* Expand dataset to include **larger regions and real patient data**

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push to branch (`git push origin feature-name`)
5. Open a pull request

---

## 🏆 Acknowledgments

Inspired by **real-world health insurance analytics**. Thanks to the **open-source community** for Python libraries and tools.

📧 Contact: [henrymorgan273@yahoo.com](mailto:henrymorgan273@yahoo.com)
🌐 LinkedIn: [Henry C. Dibie](https://www.linkedin.com/in/kinghenrymorgan/)

---

## 📜 License

This project is licensed under the **MIT License** – free to use, modify, and share.
