from streamlit import secrets


def countries_dict(iew) -> str:
    dct = {
        "00": "US",
        "40": "PL",
        "20": "DE",
        "50": "GB",
        "80": "FR",
        "19": "KR",
        "60": "CN",
        "90": "ES",
        "18": "JP",
        "30": "IT",
        "10": "CZ",
        "14": "LT",
        "11": "HU",
        "15": "SK",
        "12": "CA",
        "17": "EE",
        "13": "LV",
        "16": "RO",
        "70": "TR"
    }
    return dct[iew[2:4]]
    

def analyze_country(iew: str) -> dict:
    code = countries_dict(iew)
    return {'Authorization': f'Basic {secrets[f"NPS_{code}_AUTH"]}'}
