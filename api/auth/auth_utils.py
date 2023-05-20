import datetime

from quickbooks import QuickBooks

from constants import SESSION_ACCESS_TOKEN, SESSION_REFRESH_TOKEN, SESSION_TOKEN_EXPIRATION, SESSION_REFRESH_EXPIRATION, \
    SESSION_REALM_ID
from auth import auth_client
from quick_books import initialize_quickbooks_client


def refresh_auth_token(refresh_token, session):
    auth_client.refresh(refresh_token)
    session[SESSION_ACCESS_TOKEN] = auth_client.access_token
    session[SESSION_REFRESH_TOKEN] = auth_client.refresh_token

    now = datetime.datetime.now()
    token_expire = now + datetime.timedelta(seconds=auth_client.expires_in)
    session[SESSION_TOKEN_EXPIRATION] = token_expire.timestamp()

    refresh_token_expire = now + datetime.timedelta(seconds=auth_client.x_refresh_token_expires_in)
    session[SESSION_REFRESH_EXPIRATION] = refresh_token_expire.timestamp()

    initialize_quickbooks_client(session[SESSION_REALM_ID])
