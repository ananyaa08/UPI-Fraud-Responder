"""
Hand-written knowledge base. This is the ONLY place legal / procedural advice lives.
The LLM never writes advice; code appends entries from here.

IMPORTANT: every entry below was written from public knowledge and must be checked by YOU
against the linked official source. After checking, fill `last_checked` (e.g. "2026-11-08").
Entries with last_checked=None are displayed to the user as "unverified".
"""

DISCLAIMER = (
    "I am an AI assistant, not a lawyer or the police. I give procedural first-aid and help you "
    "organise facts. I cannot guarantee that money will be recovered."
)

# ---- Immediate triage: shown on the first in-scope message -------------------------------
TRIAGE_STEPS = [
    "**Call 1930 (National Cyber Crime Helpline) right now** and also file at "
    "**https://cybercrime.gov.in**. Speed matters: the sooner a transaction is reported, the better the "
    "chance the receiving account can be put on hold. There is no guarantee.",
    "**Call your bank's helpline** (number on the back of your card / official app) and ask them to "
    "flag the transaction and block UPI/card if needed. Ask for a complaint/ticket number and note it down.",
    "**Do not delete anything.** Keep chats, call logs, screenshots, the payment receipt and the "
    "scammer's numbers/IDs.",
    "**Do not send more money** to 'release', 'verify' or 'recover' the first payment, and never share "
    "your UPI PIN or OTP with anyone. You never need a PIN to *receive* money.",
]

# ---- Categories (used by TF-IDF matcher). reference_text includes some Hinglish words. ----
CATEGORIES = {
    "parcel_courier": {
        "label": "Courier / parcel / customs scam",
        "reference_text": "fedex dhl bluedart courier parcel package customs custom duty delivery fee held "
                          "seized illegal items drugs aadhaar linked parcel pay fee release shipment tracking "
                          "number off switched off",
        "tips": ["Courier firms do not demand fees through personal UPI IDs or phone calls. Note the "
                 "tracking number or website/link they gave you."],
    },
    "authority_impersonation": {
        "label": "Impersonation of police / agency ('digital arrest') scam",
        "reference_text": "police cbi ed customs narcotics officer video call digital arrest arrested "
                          "warrant case money laundering verify account safe account transfer rbi trai "
                          "court notice threat",
        "tips": ["Government agencies do not 'digitally arrest' anyone or ask for payment over a call. "
                 "Do not stay on the call; note the number, any badge/ID shown, and any 'case number' they quoted."],
    },
    "fake_qr_collect": {
        "label": "Fake QR / collect-request scam",
        "reference_text": "qr code scan receive money collect request pending request approve request "
                          "refund cashback olx buyer seller advance enter pin to receive payment debited "
                          "instead of credited",
        "tips": ["You never need to scan a QR code or enter your PIN to receive money. If money left your "
                 "account after you scanned/approved something, mention that clearly in the report."],
    },
    "screen_sharing_remote": {
        "label": "Screen-sharing / remote-access app scam",
        "reference_text": "anydesk teamviewer quicksupport screen share remote access app install apk "
                          "download link customer care helpline refund fake support controlled phone "
                          "hacked mobile banking sim",
        "tips": ["Uninstall the remote-access app, turn off internet on that phone, change your banking "
                 "passwords/UPI PIN from a safe device, and ask your bank to block net-banking/UPI."],
    },
    "phishing_otp_vishing": {
        "label": "Phishing / OTP / fake bank KYC scam",
        "reference_text": "otp kyc update bank account blocked suspended sms link call pretending bank "
                          "manager credit card limit reward points pan update password cvv card number "
                          "shared otp unauthorised debit",
        "tips": ["If you shared an OTP/PIN/card details, tell your bank immediately, mention the time you "
                 "shared it, and ask them to block the card/UPI."],
    },
    "job_investment_task": {
        "label": "Fake job / task / investment scam",
        "reference_text": "job offer part time work from home telegram whatsapp group task like youtube "
                          "review earn commission investment trading stock crypto returns profit "
                          "deposit more withdraw fee tax",
        "tips": ["Stop all payments. Save the group/channel link, the usernames and the website/app name "
                 "and every deposit receipt."],
    },
    "generic_upi_fraud": {
        "label": "UPI / online payment fraud (type not clear)",
        "reference_text": "",
        "tips": [],
    },
}

# ---- Legal / regulatory context. Shown to user as 'for your information'. ----
LEGAL_NOTES = [
    {
        "text": "IT Act, 2000 - Section 66D deals with cheating by personation using a computer resource "
                "or communication device. Police decide which sections to register; I cannot tell you "
                "which will be applied.",
        "source": "https://www.indiacode.nic.in (search: Information Technology Act, 2000)",
        "last_checked": None,
    },
    {
        "text": "Bharatiya Nyaya Sanhita, 2023 - provisions on cheating (Sec. 318) and cheating by "
                "personation (Sec. 319) may also be invoked by police.",
        "source": "https://www.indiacode.nic.in (search: Bharatiya Nyaya Sanhita, 2023)",
        "last_checked": None,
    },
    {
        "text": "RBI's circular on 'Customer Protection - Limiting Liability of Customers in Unauthorised "
                "Electronic Banking Transactions' (6 July 2017) limits customer liability mainly for "
                "UNAUTHORISED transactions reported promptly. If you were tricked into sending the money "
                "yourself, it may not apply directly; your bank decides first. Do not assume a refund.",
        "source": "https://www.rbi.org.in (search the circular title)",
        "last_checked": None,
    },
    {
        "text": "If your bank does not resolve your complaint, you can escalate to the RBI Integrated "
                "Ombudsman after giving the bank a chance to respond (check the current time limit on the portal).",
        "source": "https://cms.rbi.org.in",
        "last_checked": None,
    },
]

# ---- Canned responses ----
OUT_OF_SCOPE_MSG = (
    "I can only help with **UPI / online payment fraud** (money lost to a scam or unauthorised payment). "
    "What you describe is outside that, so I won't guess at the law. For other legal problems please "
    "contact a lawyer or your District Legal Services Authority (DLSA) / NALSA for free legal aid: "
    "https://nalsa.gov.in. If your problem *is* a payment scam, tell me what happened."
)

CASE_LAW_MSG = (
    "I don't cite court cases or judgments: I could get one wrong, so I don't try. "
    "I only share the few references in my knowledge base, each with its source so you can check it. "
    "For case law, please ask a lawyer "
    "or your DLSA."
)

NO_GUARANTEE_MSG = (
    "I can't promise you will get the money back. Recovery depends on how fast the transaction is "
    "reported, whether funds are still in the receiving account, and your bank's and the police's "
    "processes. What I can do is help you report quickly and with complete details."
)

QUESTIONS = {
    "amount": "How much money was sent (in ₹)?",
    "txn_time": "What date and approximate time did you make the payment?",
    "utr": "What is the **12-digit UTR / UPI reference number**? Find it in your payment app under "
           "transaction history -> details.",
    "suspect_id": "Which **UPI ID, phone number or account** did the money go to? (e.g. name@bank). "
                  "Copy it from the transaction details.",
    "bank": "Which **bank account** was the money sent from?",
}
REQUIRED_ORDER = ["amount", "txn_time", "utr", "suspect_id", "bank"]
