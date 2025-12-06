from flask import Flask, request, render_template
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load trained model and scaler
model_path = os.path.join('models', 'model.pkl')
scaler_path = os.path.join('models', 'scaler.pkl')
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

numeric_features = ['age', 'bmi', 'children']
region_categories = ['region_northwest', 'region_southeast', 'region_southwest']

@app.route('/', methods=['GET'])
def home():
    return render_template('form.html')

@app.route('/predict_form', methods=['POST'])
def predict_form():
    data = {
        'age': int(request.form['age']),
        'bmi': float(request.form['bmi']),
        'children': int(request.form['children']),
        'sex': request.form['sex'],
        'smoker': request.form['smoker'],
        'region': request.form['region']
    }
    
    df = pd.DataFrame([data])
    
    # One-hot encoding
    df['sex_male'] = 1 if df['sex'][0].lower() == 'male' else 0
    df['smoker_yes'] = 1 if df['smoker'][0].lower() == 'yes' else 0
    for region in region_categories:
        region_name = region.split('_')[1]
        df[region] = 1 if df['region'][0].lower() == region_name else 0
    
    df = df[model.feature_names_in_]
    df[numeric_features] = scaler.transform(df[numeric_features])
    
    prediction = model.predict(df)[0]
    
    # Dataset stats
    insurance_df = pd.read_csv(os.path.join('data', 'insurance.csv'))
    average_charge = insurance_df['charges'].mean()
    smoker_avg = insurance_df[insurance_df['smoker']=='yes']['charges'].mean()
    nonsmoker_avg = insurance_df[insurance_df['smoker']=='no']['charges'].mean()
    
    return render_template('result.html',
                           prediction=prediction,
                           average_charge=average_charge,
                           smoker_avg=smoker_avg,
                           nonsmoker_avg=nonsmoker_avg)

if __name__ == '__main__':
    app.run(debug=True)
