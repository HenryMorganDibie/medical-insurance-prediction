import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from data_preprocessing import load_data, preprocess_data

# Load and preprocess data
df = load_data('../data/insurance.csv')
df_encoded, scaler = preprocess_data(df)

# Split features and target
X = df_encoded.drop('charges', axis=1)
y = df_encoded['charges']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)
print(f"RMSE: {rmse:.2f}, R²: {r2:.4f}")

# Save model and scaler
joblib.dump(model, '../models/model.pkl')
joblib.dump(scaler, '../models/scaler.pkl')
print("Model and scaler saved.")