import datetime

from intuitlib.client import AuthClient
from intuitlib.enums import Scopes

import config

last_token_refresh = datetime.datetime.now().timestamp()

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
