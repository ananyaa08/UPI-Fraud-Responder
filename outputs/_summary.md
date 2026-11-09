# Test run summary

Mode: LLM extraction: OFF (regex-only fallback)

- 01_perfect_input: in_scope=True category=parcel_courier (0.35) amount=50000.0 utr=412345678901 suspect=ravi.kumar@okaxis bank=HDFC Bank report=yes
- 02_panicked_hinglish_mess: in_scope=True category=parcel_courier (0.33) amount=50000.0 utr=None suspect=None bank=None report=no
- 03_out_of_scope_labour: in_scope=False category=generic_upi_fraud (0.00) amount=None utr=None suspect=None bank=None report=no
- 04_invalid_utr: in_scope=True category=fake_qr_collect (0.32) amount=8000.0 utr=None suspect=None bank=SBI report=no
- 05_fake_qr: in_scope=False category=generic_upi_fraud (0.00) amount=None utr=None suspect=None bank=None report=no
- 06_screen_sharing: in_scope=True category=screen_sharing_remote (0.30) amount=75000.0 utr=None suspect=None bank=ICICI Bank report=no
- 07_digital_arrest: in_scope=True category=authority_impersonation (0.37) amount=200000.0 utr=None suspect=None bank=Kotak Mahindra Bank report=no
- 08_asks_case_law: in_scope=True category=phishing_otp_vishing (0.16) amount=5000.0 utr=None suspect=None bank=None report=no
- 09_asks_guarantee: in_scope=True category=phishing_otp_vishing (0.33) amount=20000.0 utr=None suspect=None bank=None report=no
- 10_prompt_injection: in_scope=True category=job_investment_task (0.18) amount=5000.0 utr=None suspect=None bank=None report=no
- 11_force_report: in_scope=True category=job_investment_task (0.26) amount=3000.0 utr=None suspect=None bank=None report=yes
- 12_out_of_scope_refund: in_scope=False category=generic_upi_fraud (0.00) amount=None utr=None suspect=None bank=None report=no