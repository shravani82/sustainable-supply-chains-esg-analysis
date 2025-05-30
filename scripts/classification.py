from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Assume you have a 'Risk_Level' column with categories Low, Medium, High
# Features could be ESG scores + supply chain metrics
features = ['Environmental_Score', 'Social_Score', 'Governance_Score', 'Supplier_Reliability', 'Delivery_Time']
X = df[features]
y = df['Risk_Level']  # categorical target

# Encode target if needed
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Model training
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Prediction
y_pred = clf.predict(X_test)

# Evaluation
print(classification_report(y_test, y_pred, target_names=le.classes_))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
