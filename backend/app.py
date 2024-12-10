from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)
CORS(app)
app.config["UPLOAD_FOLDER"] = "./uploads"

# Mock model and vectorizer (replace with your actual pre-trained model)
categories = ["Mathematics", "Science", "Literature", "History", "Biology", "fungi"]
vectorizer = TfidfVectorizer()
model = MultinomialNB()
X_train = ["algebra equations", "physics laws", "novel poetry", "ancient empires", "fungi"]
y_train = ["Mathematics", "Science", "Literature", "History", "fungi"]
X_train_vec = vectorizer.fit_transform(X_train)
model.fit(X_train_vec, y_train)

@app.route('/classify', methods=['POST'])
def classify():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Predict category
    X_test_vec = vectorizer.transform([content])
    prediction = model.predict(X_test_vec)[0]
    confidence = max(model.predict_proba(X_test_vec)[0]) * 100

    # Log classification result
    log_entry = {"filename": file.filename, "category": prediction, "confidence": confidence}
    with open("classification_log.json", "a") as log:
        log.write(json.dumps(log_entry) + "\n")

    return jsonify({"filename": file.filename, "category": prediction, "confidence": confidence})

if __name__ == "__main__":
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])
    app.run(debug=True)

