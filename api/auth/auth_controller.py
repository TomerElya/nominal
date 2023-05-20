import datetime

from flask import redirect, request, session, Blueprint, abort
from quickbooks import QuickBooks

import api.auth.auth_utils
import quick_books
from constants import SESSION_ACCESS_TOKEN, SESSION_REALM_ID, SESSION_REFRESH_TOKEN, SESSION_TOKEN_EXPIRATION, \
    SESSION_REFRESH_EXPIRATION, SESSION_LAST_REFRESH
from api.auth.auth_utils import refresh_auth_token
from auth import auth_client, scopes, initialize_auth_client, last_token_refresh
from quick_books import initialize_quickbooks_client

auth_bp = Blueprint("auth", __name__)


@auth_bp.route('/auth')
def quick_books_auth():
    url = auth_client.get_authorization_url(scopes)
    return redirect(url)


@auth_bp.route("/auth-callback")
def auth_callback():
    auth_client.get_bearer_token(request.args.get("code"), request.args.get("realmId"))
    session[SESSION_REALM_ID] = request.args.get("realmId")
    refresh_auth_token(auth_client.refresh_token, session)

    return str(auth_client.x_refresh_token_expires_in)
