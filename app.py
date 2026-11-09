import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from core import Case, respond, llm_status  # noqa: E402  (after load_dotenv so env is set)
import kb  # noqa: E402

st.set_page_config(page_title="UPI Fraud First Responder", page_icon="🚨")
st.title("🚨 UPI Fraud First Responder")
st.caption("Lost money to a UPI / online payment scam? Tell me what happened, in English, Hindi or Hinglish.")

with st.sidebar:
    st.markdown("**Scope:** UPI / online payment fraud only.")
    st.markdown("**Emergency:** call **1930** | https://cybercrime.gov.in")
    st.info(kb.DISCLAIMER)
    st.caption(llm_status())
    st.caption("Do not paste real Aadhaar/PAN/card/PIN/OTP details here.")
    if st.button("Start a new case"):
        st.session_state.clear()
        st.rerun()

if "case" not in st.session_state:
    st.session_state.case = Case()
    st.session_state.chat = []
    st.session_state.report = None

for role, content in st.session_state.chat:
    with st.chat_message(role):
        st.markdown(content)

if st.session_state.report:
    st.subheader("Draft incident report")
    st.code(st.session_state.report, language=None)
    st.download_button("Download report (.txt)", st.session_state.report, file_name="incident_report.txt")

user_msg = st.chat_input("Describe what happened (e.g. 'I sent 50k on GPay to a fake FedEx caller')")
if user_msg:
    st.session_state.chat.append(("user", user_msg))
    result = respond(st.session_state.case, user_msg)
    st.session_state.chat.append(("assistant", result["text"]))
    if result["report"]:
        st.session_state.report = result["report"]
    st.rerun()
