from flask import Blueprint, session
from quickbooks.objects.account import Account

import quick_books
from constants import SESSION_CURRENT_MINUTE, SESSION_MINUTE_API_CALLS

accounts_bp = Blueprint("accounts", __name__)

@accounts_bp.route("/accounts")
def get_accounts():
    accs = Account.all(qb=quick_books.quickbooks_client)
    return [acc.to_json() for acc in accs]

@accounts_bp.route("/test")
def test():
    return [session[SESSION_MINUTE_API_CALLS],session[SESSION_CURRENT_MINUTE]]