# UPI Fraud First Responder

##  Live Demo
Try the application here: [UPI Fraud Responder](https://ananyaa08-upi-fraud-responder-app-0w9ket.streamlit.app/)

Focused first-responder chatbot for UPI / online payment fraud in India. Hybrid pipeline:
regex + optional LLM extraction -> regex validation -> TF-IDF category match -> triage + report built from a
hand-written knowledge base (`kb.py`). The LLM never writes legal advice.

## Run locally (VS Code)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate     Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then paste your free Gemini key (https://aistudio.google.com/apikey)
streamlit run app.py
```
No key? Set `LLM_PROVIDER=none` in `.env`; it runs in regex-only mode.

## Re-run tests (writes raw outputs to `outputs/`)
```bash
python run_tests.py
```

## Swap the model
Edit `.env`: `LLM_PROVIDER=gemini|anthropic|none` and the matching `*_MODEL`. Only `llm.py` talks to a model.

## Deploy free on Streamlit Community Cloud
1. Push this folder to a public GitHub repo (do NOT commit `.env`).
2. share.streamlit.io -> New app -> pick repo, main file `app.py`.
3. Advanced settings -> Secrets: `LLM_PROVIDER="gemini"` and `GEMINI_API_KEY="..."`.
   (Streamlit secrets are exposed as env vars. If your key does not load, add
   `os.environ.update(st.secrets)` after the imports in `app.py`.)

## Files
- `kb.py` - ALL legal/procedural content. Verify each entry at its source and fill `last_checked`.
- `core.py` - extraction, validation, classification, triage, report.
- `llm.py` - swappable model adapter.
- `app.py` - Streamlit UI. `run_tests.py` + `tests/cases.py` - 12 synthetic test cases.
