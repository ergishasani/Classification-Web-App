# ClassifyAI

ClassifyAI is an intelligent document classification system that supports PDF, DOCX, and TXT files. The system leverages a machine learning model to categorize files into predefined categories and display the confidence level of predictions.

## Features

- Drag-and-drop file upload functionality.
- Supports multiple file types: `.pdf`, `.docx`, `.txt`.
- Displays the uploaded file name.
- Provides the classification category and confidence level.
- Clear button to reset the form for new file uploads.

## Project Structure

```
ClassifyAI_Project/
├── backend/
│   ├── app.py             # Backend server using Flask
│   ├── models/            # Folder to store ML models (if applicable)
│   ├── uploads/           # Directory to temporarily store uploaded files
│   ├── requirements.txt   # Python dependencies
│   └── classification_log.json # Log file for classifications
│
├── frontend/
│   ├── index.html         # Main HTML file
│   ├── style.css          # Styling for the frontend
│   ├── script.js          # Client-side logic
│   ├── img/               # Folder for assets (e.g., logo)
│   └── README.md          # Project documentation
│
└── README.md              # General project documentation
```

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- Node.js (optional for frontend development)

### Backend Setup

1. Navigate to the `backend/` directory:

   ```bash
   cd backend
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask server:

   ```bash
   python app.py
   ```

   The server will be available at `http://127.0.0.1:5000`.

### Frontend Setup

1. Navigate to the `frontend/` directory:

   ```bash
   cd frontend
   ```

2. Open `index.html` in your browser to view the application.

   Alternatively, use a lightweight server to serve the frontend:

   ```bash
   python -m http.server 8000
   ```

   Visit `http://127.0.0.1:8000` in your browser.

## How to Use

1. Drag and drop a file or click the "Upload a file" area to select a file.
2. Click the "Classify" button to classify the file.
3. View the classification results, including the file name, category, and confidence.
4. To reset, click the "Clear" button and upload a new file.

## Dependencies

### Backend

- Flask
- Flask-CORS
- sklearn
- PyPDF2
- python-docx

### Frontend

- Vanilla HTML/CSS/JavaScript

## Screenshots

### Main Screen

![image](https://github.com/user-attachments/assets/c11adc42-dacf-41f0-9988-4f107c1e9100)


### File Uploaded

![image](https://github.com/user-attachments/assets/54763e35-c47e-4304-8069-24c59c31a0af)



### Classification Result

![image](https://github.com/user-attachments/assets/8f79d6e7-0105-4107-99c9-6831721b74a2)


## Contributors

- Group 7

## License

This project is licensed under the MIT License. See the LICENSE file for details.
