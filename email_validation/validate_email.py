import re
from streamlit import secrets

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


def authenticate_user(email):
    allowed_emails = secrets["ALLOWED_EMAILS"].split(",")
    return email in allowed_emails and is_valid_email(email)
