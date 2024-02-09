import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the dataset
file_path = "matches.csv"  
dataset = pd.read_csv(file_path)

# Preprocessing the data
# Selecting relevant features for prediction
features = ["city", "team1", "team2", "toss_winner", "toss_decision", "venue"]
target = "winner"

# Handling missing values
# For simplicity, we replace missing categorical values with a placeholder
dataset[features] = dataset[features].fillna("Unknown")

# Encoding categorical variables
le = LabelEncoder()
for feature in features:
    dataset[feature] = le.fit_transform(dataset[feature])

# Encoding the target variable
dataset[target] = le.fit_transform(dataset[target])

# Splitting the data into features (X) and target (y)
X = dataset[features]
y = dataset[target]

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Model Building
# Using Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Displaying the results
print("Accuracy of the model:", accuracy)
print("Classification Report:\n", report)

# Saving the trained model to a file
model_filename = "cricket_match_winner_predictor_model.pkl"
joblib.dump(model, model_filename)

print(f"Model saved as {model_filename}")
