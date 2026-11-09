# UPI Fraud Responder

An AI-powered UPI fraud detection and first-response assistance application built using Python, Streamlit, and Google's Gemini API.

## Overview

UPI Fraud Responder is designed to assist users in identifying potential UPI-related fraud incidents and understanding appropriate first-response actions.

The application processes user-provided incident details, extracts relevant information, and provides structured guidance to help users respond to suspected digital payment fraud.

It combines rule-based processing with Large Language Model (LLM) capabilities to make incident analysis more accessible and organized.

## Key Features

- **Fraud Incident Analysis:** Processes user-provided descriptions of suspected UPI fraud.
- **Information Extraction:** Identifies relevant incident details using Gemini API.
- **Rule-Based Fallback:** Supports regex-based extraction when LLM functionality is unavailable.
- **First-Response Guidance:** Provides structured guidance based on reported incidents.
- **Knowledge Base Integration:** Uses a knowledge base to support relevant responses.
- **Interactive Interface:** Provides a user-friendly interface through Streamlit.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| AI/LLM | Google Gemini API |
| Text Processing | Regex |
| Configuration | Python dotenv |
| Version Control | Git and GitHub |

## Project Structure

```text
upi-first-responder/
│
├── app.py                 # Streamlit application
├── core.py                # Core processing logic
├── kb.py                  # Knowledge base
├── llm.py                 # LLM integration
├── tests/                 # Test cases
├── outputs/               # Generated outputs
├── run_tests.py           # Test execution script
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── .gitignore             # Files excluded from Git
├── README.md              # Project documentation
├── RUNNING.md             # Setup and execution guide
└── SOLUTION_DOC.md        # Solution documentation
```

## Installation and Setup

### Prerequisites

- Python 3.10 or later
- Git
- Google Gemini API key (for LLM functionality)

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd upi-first-responder
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file using `.env.example` as a template.

Configure the following variables:

```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
GEMINI_MODEL=gemini-2.5-flash
```

Get your Gemini API key from:

https://aistudio.google.com/apikey

**Security:** Never upload your `.env` file or expose your API key publicly.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the application in your browser at:

http://localhost:8501

For detailed instructions, refer to [RUNNING.md](RUNNING.md).

## Running Tests

Execute the test suite using:

```bash
python run_tests.py
```

## Version Control

This project is maintained using Git and GitHub.

The repository contains the application source code, documentation, dependencies, and test files.

To get the latest version:

```bash
git pull origin main
```

## Future Improvements

- Improve fraud incident classification.
- Expand the knowledge base with additional fraud scenarios.
- Enhance incident reporting and response recommendations.
- Improve extraction accuracy and handling of incomplete user inputs.
- Add further testing and validation across different incident types.

## Disclaimer

This application is intended for informational and educational assistance. It does not replace official banking, NPCI, or law-enforcement reporting channels.

Users should contact their bank and appropriate official authorities to report suspected financial fraud. They should never share their UPI PIN, OTP, passwords, or other confidential credentials.


