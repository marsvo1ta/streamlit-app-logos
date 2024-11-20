from streamlit_cookies_manager import EncryptedCookieManager

# Ініціалізація Cookie Manager
def initialize_cookies(prefix="my_app", password="my_secret_password"):
    cookies = EncryptedCookieManager(prefix=prefix, password=password)
    if not cookies.ready():
        return None
    return cookies

# Перевірка, чи користувач автентифікований
def is_authenticated(cookies):
    return cookies.get("authenticated") == "true"

# Збереження статусу автентифікації
def set_authenticated(cookies, value):
    cookies["authenticated"] = "true" if value else "false"
    cookies.save()
