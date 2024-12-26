from flask import Flask, request, render_template,jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the saved model
with open('model/best_model2.pkl', 'rb') as file:
    model = pickle.load(file)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def home():
    return render_template('home.html')

@app.route('/no_heart_disease')
def no_heart_disease():
    return render_template('No-disease.html')

@app.route('/heart_disease_likely')
def heart_disease_likely():
    return render_template('Yes-disease.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Collect input data from the form
            features = [
                int(request.form['age']),
                int(request.form['sex']),
                int(request.form['cp']),
                int(request.form['trestbps']),
                int(request.form['chol']),
                int(request.form['fbs']),
                int(request.form['restecg']),
                int(request.form['thalach']),
                int(request.form['exang']),
                float(request.form['oldpeak']),
                int(request.form['slope']),
                int(request.form['ca']),
                int(request.form['thal'])
            ]
            
            # Create a NumPy array for model input
            input_features = np.array([features])
            print(input_features)

            # Use the loaded model to make a prediction
            print("Starting prediction...") 
            prediction = model.predict(input_features)
            print("Prediction:", prediction[0])

            # Redirect based on the prediction
    
            if prediction[0] == 0:
                return jsonify({'prediction': 'No'})
            else:
                return jsonify({'prediction': 'Yes'})

        except Exception as e:
            print("Error during prediction: ", e)
            return jsonify({'error': 'Error occurred during prediction'})        
        
        


if __name__ == "__main__":
    app.run(debug=True)
