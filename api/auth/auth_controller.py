from flask import redirect, request, session, Blueprint

from api.auth.auth_utils import refresh_auth_token
from auth import auth_client, scopes
from constants import SESSION_REALM_ID

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

    return ''
