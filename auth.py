from threading import Lock

from intuitlib.client import AuthClient
from intuitlib.enums import Scopes

import config

"""
A mutex is necessary since AuthClient is intended to work per user. To avoid context switches and auth_client's
credentials shifting from one user to another, we use a mutex to isolate the operation of token acquisition, store on
session and release.
"""
auth_client_mutex = Lock()

auth_client = AuthClient(
    client_id=config.config["quick_books"]["client_id"],
    client_secret=config.config["quick_books"]["secret"],
    redirect_uri=config.config["quick_books"]["redirect_url"],
    environment="sandbox",
)

scopes = [
    Scopes.ACCOUNTING,
    Scopes.EMAIL,
    Scopes.OPENID,
    Scopes.PROFILE
]


def initialize_auth_client(token, refresh):
    auth_client.refresh_token = refresh
    auth_client.access_token = token
