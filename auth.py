from intuitlib.client import AuthClient
from intuitlib.enums import Scopes

import config

auth_client = AuthClient(
    config.config["quick_books"]["client_id"],
    config.config["quick_books"]["secret"],
    config.config["quick_books"]["redirect_url"],
    "sandbox",

)

scopes = [
    Scopes.ACCOUNTING,
    Scopes.EMAIL,
    Scopes.OPENID,
    Scopes.PROFILE
]