import config

QUICKBOOKS_API_URL = config.config["quick_books"]["api_url"]


def build_api_headers(token):
    return {
        'Authorization': f'Bearer {token}',
        "accept": "application/json"
    }
