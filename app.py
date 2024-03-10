# app.py
from flask import Flask, render_template, request
from load_model import load_your_model, load_your_vectorizer

app = Flask(__name__)

# Mock functions for loading model and vectorizer
def load_your_model(model_path):
    # Replace with your actual loading logic
    return "Mock Model"

def load_your_vectorizer(vectorizer_path):
    # Replace with your actual loading logic
    return "Mock Vectorizer"

# Load your trained model and TF-IDF vectorizer
model_path = "email_classification_app/path/to/your/model.pkl"
vectorizer_path = "email_classification_app/path/to/your/vectorizer.pkl"

model = load_your_model(model_path)
tfidf_vectorizer = load_your_vectorizer(vectorizer_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if request.method == 'POST':
        content = request.form['content']

        # Check for different categories using a rule-based approach
        categories = {
            "finance": ["transaction", "payment", "invoice"],
            "tickets": ["issue", "ticket", "support"],
            "promotion": ["offer", "discount", "promo"],
            "orders": ["order", "purchase", "buy"],
            "reminders": ["reminder", "upcoming", "event"]
            # Add more categories as needed
        }

        # Initialize default category
        prediction = "Other"

        # Check for category keywords
        for category, keywords in categories.items():
            if any(keyword in content.lower() for keyword in keywords):
                prediction = category
                break

        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
