import requests

from quick_books.models.accounts.accounts import Account
from quick_books.quick_books import QUICKBOOKS_API_URL, build_api_headers


def get_accounts_query(access_token, realm_id, query):
    url = f'{QUICKBOOKS_API_URL}/v3/company/{realm_id}/query?query={query}'
    res = requests.get(url, headers=build_api_headers(access_token))
    return Account.from_array(res.json()["QueryResponse"]["Account"])
