# UPI Fraud Responder

An AI-powered UPI fraud detection and first-response assistance application built using Python, Streamlit, and Google's Gemini API.

## 🚀 Live Application

**Try the application here:**

[UPI Fraud Responder – Open Live App](https://ananyaa08-upi-fraud-responder-app-0w9ket.streamlit.app/)


## 1. Project Overview

UPI Fraud Responder is designed to assist users in identifying potential UPI-related fraud incidents and understanding appropriate first-response actions.

The application processes user-provided incident details, extracts relevant information, and provides structured guidance to help users respond to suspected digital payment fraud.

It combines rule-based processing with Large Language Model (LLM) capabilities to make incident analysis more accessible and organized.

## 2. Key Features

- **Fraud Incident Analysis:** Processes user-provided descriptions of suspected UPI fraud.
- **Information Extraction:** Identifies relevant incident details using Gemini API.
- **Rule-Based Fallback:** Supports regex-based extraction when LLM functionality is unavailable.
- **First-Response Guidance:** Provides structured guidance based on reported incidents.
- **Knowledge Base Integration:** Uses a knowledge base to support relevant responses.
- **Interactive Interface:** Provides a user-friendly interface through Streamlit.

## 3. Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| AI/LLM | Google Gemini API |
| Text Processing | Regex |
| Configuration | Python dotenv |
| Version Control | Git and GitHub |

## 4. Project Structure

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

## 5. Prerequisites

Before running the application locally, make sure you have installed:

- Python 3.10 or later
- Git
- Visual Studio Code (recommended)
- Google Gemini API key (for LLM functionality)

## 6. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/ananyaa08/UPI-Fraud-Responder.git
```

Navigate into the project directory:

```bash
cd UPI-Fraud-Responder
```

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

**PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root directory using `.env.example` as a template.

Add the following configuration:

```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
GEMINI_MODEL=gemini-2.5-flash
```

Get your Gemini API key from:

https://aistudio.google.com/apikey

Replace `YOUR_GEMINI_API_KEY` with your actual API key.

**Security:** Never upload your `.env` file or expose your API key publicly.

### Step 5: Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default web browser.

If it does not open automatically, visit:

http://localhost:8501

## 7. Running Tests

Execute the available test suite using:

```bash
python run_tests.py
```

## 8. Stopping the Application

To stop the local Streamlit server, press:

```text
Ctrl + C
```

## 9. Troubleshooting

| Problem | Possible Solution |
|---|---|
| Python not recognized | Install Python and add it to PATH |
| Streamlit not recognized | Install dependencies using `pip install -r requirements.txt` |
| Gemini API error | Verify the API key and `.env` configuration |
| Missing modules | Reinstall dependencies |
| Port already in use | Stop the other Streamlit process or use another port |
| LLM extraction OFF | Check the Gemini API key and LLM configuration |

## 10. GitHub Repository

Source code and project documentation:

[UPI Fraud Responder – GitHub Repository](https://github.com/ananyaa08/UPI-Fraud-Responder)

## 11. Disclaimer

This application is intended for informational and educational assistance. It does not replace official banking, NPCI, or law-enforcement reporting channels.

Users should contact their bank and appropriate official authorities to report suspected financial fraud. They should never share their UPI PIN, OTP, passwords, or other confidential credentials.
