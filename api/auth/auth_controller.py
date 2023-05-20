import datetime

from flask import redirect, request, session, Blueprint, abort
from quickbooks import QuickBooks

import api.auth.auth_utils
import quick_books
from constants import SESSION_ACCESS_TOKEN, SESSION_REALM_ID, SESSION_REFRESH_TOKEN, SESSION_TOKEN_EXPIRATION, \
    SESSION_REFRESH_EXPIRATION
from api.auth.auth_utils import refresh_auth_token
from auth import auth_client, scopes, initialize_auth_client
from quick_books import initialize_quickbooks_client

auth_bp = Blueprint("auth", __name__)


@auth_bp.before_app_request
def auth_middleware():
    if request.endpoint not in ['auth.quick_books_auth', 'auth.auth_callback']:
        now = datetime.datetime.now().timestamp()
        if SESSION_ACCESS_TOKEN not in session or SESSION_REFRESH_TOKEN not in session or SESSION_TOKEN_EXPIRATION not\
                in session or SESSION_REALM_ID not in session:
            abort(401)
        if session[SESSION_TOKEN_EXPIRATION] <= now:
            refresh_auth_token(session, session[SESSION_REFRESH_TOKEN])
        if session[SESSION_REFRESH_EXPIRATION] <= now:
            session.pop(SESSION_ACCESS_TOKEN)
        if quick_books.quickbooks_client.company_id == 0:
            initialize_auth_client(session[SESSION_ACCESS_TOKEN], session[SESSION_REFRESH_TOKEN])
            initialize_quickbooks_client(session[SESSION_REALM_ID])



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
