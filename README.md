# Live Text Analyzer

## About the Project

Live Text Analyzer is a beginner-friendly Python project that uses Regular Expressions (Regex) to identify and extract useful information from text.

The application is designed to extract information such as email addresses, phone numbers, URLs, dates, and prices automatically.

## Features

- Extract email addresses from text.
- Extract mobile phone numbers.
- Identify website URLs.
- Extract dates in supported formats.
- Extract prices in Indian Rupees (₹) and US Dollars ($).
- Count words, characters, and lines.
- Detect duplicate email addresses.
- Export extracted information into a CSV file.

## Technologies Used

- Python
- Regular Expressions (Regex)
- Streamlit
- Pandas
- CSV

## Project Structure

```text
Live-Text-Analyzer/
│
├── app.py
├── regex_extractor.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Abhinav181-reddy/Live-Text-Analyzer.git
```

### 2. Navigate to the Project Folder

```bash
cd Live-Text-Analyzer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Project

Run the Regex extraction script:

```bash
python regex_extractor.py
```

To launch the Streamlit application:

```bash
streamlit run app.py
```

## Learning Objectives

- Understand Regular Expressions in Python.
- Learn text extraction and pattern matching.
- Work with Python modules and functions.
- Build an interactive application using Streamlit.
- Export structured data using Pandas and CSV.

## Future Improvements

- Add more Regex patterns.
- Improve input validation.
- Enhance the dashboard interface.
- Support additional date and currency formats.

## Author

**Abhinav Reddy**

GitHub: https://github.com/Abhinav181-reddy

---

*This project was developed as part of my Python learning journey to gain practical experience with Regex, text processing, and application development.*
