from flask import Blueprint, session

from constants import SESSION_REALM_ID, SESSION_ACCESS_TOKEN
from quick_books.models.accounts.accounts_api import get_accounts_query

accounts_bp = Blueprint("accounts", __name__)


@accounts_bp.route("/accounts")
def get_accounts():
    accs = get_accounts_query(session[SESSION_ACCESS_TOKEN], session[SESSION_REALM_ID], "select * from Account")
    return [acc.__json__() for acc in accs]
