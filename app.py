from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if request.method == 'POST':
        contents = request.form.getlist('content[]')  # Retrieve multiple email contents

        # Check for different categories using a rule-based approach
        categories = {
            "finance": ["transaction", "payment", "invoice"],
            "tickets": ["issue", "ticket", "support"],
            "promotion": ["offer", "discount", "promo"],
            "orders": ["order", "purchase", "buy"],
            "reminders": ["reminder", "upcoming", "event"]
            # Add more categories as needed
        }

        # Initialize list to store predictions for each email
        predictions = []

        # Iterate over each email content
        for content in contents:
            # Initialize default category for the current email
            prediction = "Other"

            # Check for category keywords
            for category, keywords in categories.items():
                if any(keyword in content.lower() for keyword in keywords):
                    prediction = category
                    break
            
            # Add prediction for the current email to the list
            predictions.append(prediction)

        # Add serial numbers to predictions
        predictions_with_serial = [(i + 1, prediction) for i, prediction in enumerate(predictions)]

        return render_template('result.html', predictions=predictions_with_serial)

if __name__ == '__main__':
    app.run(debug=True)
# mayank arpit