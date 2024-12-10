from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import PyPDF2
import docx

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

# Function to extract text from PDF
def extract_text_from_pdf(filepath):
    try:
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ''
            for page in reader.pages:
                text += page.extract_text() + '\n'
        return text
    except Exception as e:
        raise ValueError(f"Error extracting text from PDF: {e}")

# Function to extract text from DOCX
def extract_text_from_docx(filepath):
    try:
        doc = docx.Document(filepath)
        text = ''
        for paragraph in doc.paragraphs:
            text += paragraph.text + '\n'
        return text
    except Exception as e:
        raise ValueError(f"Error extracting text from DOCX: {e}")

# Function to handle text-based files
def extract_text(filepath):
    ext = os.path.splitext(filepath)[-1].lower()
    if ext == '.pdf':
        return extract_text_from_pdf(filepath)
    elif ext == '.docx':
        return extract_text_from_docx(filepath)
    elif ext == '.txt':
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            raise ValueError(f"Error reading TXT file: {e}")
    else:
        raise ValueError(f"Unsupported file type: {ext}")

@app.route('/classify', methods=['POST'])
def classify():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    try:
        # Extract text content from the file
        content = extract_text(filepath)

        # Predict category
        X_test_vec = vectorizer.transform([content])
        prediction = model.predict(X_test_vec)[0]
        confidence = max(model.predict_proba(X_test_vec)[0]) * 100

        # Log classification result
        log_entry = {"filename": file.filename, "category": prediction, "confidence": confidence}
        with open("classification_log.json", "a") as log:
            log.write(json.dumps(log_entry) + "\n")

        return jsonify({"filename": file.filename, "category": prediction, "confidence": confidence})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Clean up the uploaded file
        if os.path.exists(filepath):
            os.remove(filepath)

if __name__ == "__main__":
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])
    app.run(debug=True)
