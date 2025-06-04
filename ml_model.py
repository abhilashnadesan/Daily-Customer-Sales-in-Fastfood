import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the data (update the path)
df = pd.read_csv("data/processed/sales_cleaned.csv")

# Remove missing gender if any (for safety)
df = df[df['gender'].notnull()]
df['gender'] = df['gender'].astype(int)

X = df[['gender', 'hour']]  # Features
y = df['order_type']        # Target

# Encode target labels (Online=0, In-Person=1)
y_encoded = y.astype('category').cat.codes

# Split data into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on test set
predictions = model.predict(X_test)

# Calculate accuracy
acc = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {acc:.2f}")

# Show predictions vs actual
print("Predictions:", predictions)
print("Actual:     ", y_test.values)
