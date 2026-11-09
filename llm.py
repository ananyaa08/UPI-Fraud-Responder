"""
Swappable LLM adapter. The rest of the code only calls `call_llm_json(prompt)`.
Choose provider with env LLM_PROVIDER = gemini | anthropic | none
"""
import os

PROVIDER = os.getenv("LLM_PROVIDER", "gemini").lower()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-haiku-5-5")


def llm_available() -> bool:
    if PROVIDER == "gemini":
        return bool(os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"))
    if PROVIDER == "anthropic":
        return bool(os.getenv("ANTHROPIC_API_KEY"))
    return False


def call_llm_json(prompt: str):
    """Returns the raw text of the model reply (expected to be JSON), or None if no LLM."""
    if not llm_available():
        return None
    if PROVIDER == "gemini":
        from google import genai
        key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        client = genai.Client(api_key=key)
        import time
        last_err = None
        for attempt in range(3):
            try:
                resp = client.models.generate_content(
                    model=GEMINI_MODEL,
                    contents=prompt,
                    config={"response_mime_type": "application/json", "temperature": 0},
                )
                return resp.text
            except Exception as e:
                last_err = e
                if "503" in str(e) or "429" in str(e):  # overloaded / rate limited: wait, then retry
                    time.sleep(2 * (attempt + 1))
                    continue
                raise
        raise last_err
    if PROVIDER == "anthropic":
        import anthropic
        client = anthropic.Anthropic()
        msg = client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=1024,
            temperature=0,
            messages=[{"role": "user", "content": prompt}],
        )
        return msg.content[0].text
    return None
