import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    df_encoded = pd.get_dummies(df, columns=['sex', 'smoker', 'region'], drop_first=True)
    numeric_features = ['age', 'bmi', 'children']
    scaler = StandardScaler()
    df_encoded[numeric_features] = scaler.fit_transform(df_encoded[numeric_features])
    return df_encoded, scaler

if __name__ == "__main__":
    df = load_data('../data/insurance.csv')
    processed_df, scaler = preprocess_data(df)
    print(processed_df.head())
