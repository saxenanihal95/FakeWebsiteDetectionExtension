from flask import Flask, request, jsonify
import joblib  # For loading model
from feature import FeatureExtractor
from flask_cors import CORS  # Import the CORS module
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

CORS(app)  # Enable CORS for your Flask app

# Load your trained model
model = joblib.load('./random_forest_classifier.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract URL from request
        data = request.json
        url = data['url']
        print('url',url)
        extractor = FeatureExtractor(url)
        # Extract features from URL
        features = extractor.extract()

        # Convert features to the format your model expects, e.g., a DataFrame or a numpy array
        features_df = pd.DataFrame([features])

        # Use the Logistic Regression model for prediction
        y_pred = model.predict(features_df)
        # Get the probability of being safe (class 1)
        y_pro_safe = model.predict_proba(features_df)[0, 1]

        if y_pred == 1:
            pred = "It is {0:.2f} % safe to go".format(y_pro_safe * 100)
        else:
            pred = "It is not safe"

        return jsonify({'pred': pred})
    except ValueError as e:
        # Log the error and return a message
        app.logger.error(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)