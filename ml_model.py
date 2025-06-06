import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the data
df = pd.read_csv("data/processed/sales_cleaned.csv")

# Clean the data
df = df[df['gender'].notnull()]
df['gender'] = df['gender'].astype(int)

# Use all relevant features — update this list as needed
features = ['gender', 'hour']  # Add more features if available
X = df[features]
y = df['order_type'].astype('category').cat.codes

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Set up Random Forest and hyperparameter grid
model = RandomForestClassifier(random_state=42, class_weight='balanced')  # helps if classes imbalanced

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
}

# GridSearch with 5-fold cross-validation
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

print("Best hyperparameters:", grid_search.best_params_)

# Predict on test set with best estimator
best_model = grid_search.best_estimator_
predictions = best_model.predict(X_test)

# Evaluate
acc = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {acc:.2f}")

cm = confusion_matrix(y_test, predictions)
print("Confusion Matrix:")
print(cm)

cr = classification_report(y_test, predictions, target_names=['Online', 'In-Person'])
print("Classification Report:")
print(cr)

print("Predictions:", predictions)
print("Actual:     ", y_test.values)
