from datetime import datetime

from flask import Blueprint, request, session, abort

import quick_books
from api.auth.auth_utils import refresh_auth_token
from auth import initialize_auth_client, last_token_refresh
from constants import SESSION_ACCESS_TOKEN, SESSION_REFRESH_TOKEN, SESSION_TOKEN_EXPIRATION, SESSION_REALM_ID, \
    SESSION_LAST_REFRESH, SESSION_REFRESH_EXPIRATION

auth_middleware_bp = Blueprint("auth_middleware", __name__)


@auth_middleware_bp.before_app_request
def auth_middleware():
    if request.endpoint not in ['auth.quick_books_auth', 'auth.auth_callback']:
        if SESSION_ACCESS_TOKEN not in session or SESSION_REFRESH_TOKEN not in session or SESSION_TOKEN_EXPIRATION not\
                in session or SESSION_REALM_ID not in session:
            abort(401)

        now = datetime.now().timestamp()
        if session[SESSION_TOKEN_EXPIRATION] <= now:
            # If token has expired and the last refresh on the session has not updated, that means no one has
            # refreshed it. Either refresh it or initialize according to new refreshed credentials.
            if session[SESSION_LAST_REFRESH] < now:
                refresh_auth_token(session, session[SESSION_REFRESH_TOKEN])
            else:
                initialize_auth_client(session[SESSION_ACCESS_TOKEN], session[SESSION_REFRESH_TOKEN])

        # If refresh token expired, pop access token so it has to be reacquired.
        if session[SESSION_REFRESH_EXPIRATION] <= now:
            session.pop(SESSION_ACCESS_TOKEN)

        # If token has refreshed, reinitialize auth client with new credentials
        if session[SESSION_LAST_REFRESH] > last_token_refresh:
            initialize_auth_client(session[SESSION_ACCESS_TOKEN], session[SESSION_REFRESH_TOKEN])

        if quick_books.quickbooks_client.company_id == 0:
            initialize_auth_client(session[SESSION_ACCESS_TOKEN], session[SESSION_REFRESH_TOKEN])
            quick_books.initialize_quickbooks_client(session[SESSION_REALM_ID])
