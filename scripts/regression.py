from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Target variable example: 'Delivery_Time'
# Features: ESG scores or other relevant predictors
features = ['Environmental_Score', 'Social_Score', 'Governance_Score']
X = df[features]
y = df['Delivery_Time']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(f"R2 Score: {r2_score(y_test, y_pred):.3f}")
print(f"RMSE: {mean_squared_error(y_test, y_pred, squared=False):.3f}")

# Coefficients interpretation
coeff_df = pd.DataFrame({'Feature': features, 'Coefficient': model.coef_})
print(coeff_df)
