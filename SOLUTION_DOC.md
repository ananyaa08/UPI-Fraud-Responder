# UPI Fraud First Responder - Solution Doc (Problem 2)
**Name / Roll no. / Branch:** ______   **Prototype:** <Streamlit link> / <GitHub link>   **Video:** <link>

## 1. Why this problem, and scope
Brief example: people who lose money to a scam "panic and give up". In UPI fraud, time matters and the steps
are procedural (call 1930, file on cybercrime.gov.in, inform the bank, preserve evidence), so a narrow tool
can add real value without needing to "know Indian law".
**Covers:** UPI/online payment fraud only (courier/parcel, fake QR/collect, screen-sharing, phishing/OTP,
police-impersonation, fake job/investment). **Does not cover:** tenancy, employment, consumer refunds,
criminal matters other than payment fraud, recovery strategy, drafting court filings.
**Assumptions:** user is in India; user will verify the draft report before filing; voice and Indian-language
UI are out of scope for the 3-hour build (text input accepts Hindi/Hinglish when the LLM is on).

## 2. How it works
`User text -> extraction -> validation -> category match -> triage + follow-up questions -> report`
- **Extraction (code first, LLM second):** regex pulls amount, UTR, UPI ID, phone, bank, app, date/time.
  The LLM (Gemini free tier by default; swappable in `llm.py`) only fills gaps and writes an English
  summary/timeline. Any identifier the LLM returns must appear verbatim in the user's message and pass regex.
- **Validation (code):** UTR must be exactly 12 digits; UPI ID must look like `name@bank`; email-style
  handles are rejected. A wrong-length UTR is never "fixed" - the user is asked again.
- **Classification (code):** TF-IDF + cosine similarity against 6 hand-written category descriptions.
  Below a threshold it falls back to "type not clear". It only suggests a label; the user picks on the portal.
- **Advice (hard-coded):** triage steps, category tips, legal references and canned refusals live in `kb.py`.
  Code appends them. The model never writes advice, so it cannot invent a section or case.
- **Report (template):** fixed layout; missing fields printed as NOT PROVIDED; the user's own words quoted verbatim.
- **Human in the loop:** user reviews the draft; knowledge-base entries are marked UNVERIFIED until a person
  checks the source and sets `last_checked`.

## 3. How it avoids invented law
1. No model-generated legal text. 2. Case-law questions get a fixed refusal. 3. Recovery questions get a fixed
"no guarantee" answer. 4. Every legal note shows its source and a verified/unverified tag.
5. Prompt-injection test: instructions inside the message are ignored because the model only extracts fields.

## 4. Quality checks (12 synthetic cases, raw outputs in `/outputs`)
Run in regex-only mode: ____/12 behaved as intended. Re-run with LLM on: ____/12.
Cases: perfect input, panicked Hinglish, out-of-scope x2, bad UTR, multi-turn QR scam, screen-sharing,
digital arrest, case-law trap, guarantee trap, prompt-injection, user skips questions.
**Where it fails (be honest, add your own findings):**
- Scope check is keyword-based: "Flipkart cheated me, no refund" could still be accepted as in scope.
- Without the LLM, Hindi in Devanagari script is not understood and dates like "kal shaam" are not parsed.
- TF-IDF with 6 short category texts is crude; only a few dozen real messages would show true accuracy.
- A real UTR starting with 91 plus digits 6-9 can be mistaken for a phone number unless labelled "UTR".
- The legal notes are my own summaries of public sources and may be outdated until verified.

## 5. Tools used, and one place they got it wrong
Tools: Claude (planning, code), Gemini API (extraction). **One failure (use your own if different):** the
first version accepted a Flipkart refund complaint as UPI fraud because a TF-IDF score alone was allowed to
decide scope. Test 12 caught it; I changed scope to require explicit payment + scam vocabulary.

## 6. Scale and cost
Per message: one small LLM call (a few hundred tokens), or zero in fallback mode. A new fraud type or a new
legal area = one new entry in `kb.py` plus 2-3 test cases. Next: Hindi/voice (speech-to-text in front of the
same pipeline), analytics on which fields users cannot provide, and a lawyer reviewing `kb.py` quarterly.
Cost on free tier: Rs 0; at paid rates, small-model extraction costs a fraction of a paisa per chat.

## 7. How we'd know it works with real users
Share of users who reach a complete report; time to first triage step; % who actually called 1930 within an
hour; reviewer spot-checks that no report field is invented; zero unverified legal statements in production.
