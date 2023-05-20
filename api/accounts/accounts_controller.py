from flask import Blueprint
from quickbooks.objects.account import Account

import quick_books

accounts_bp = Blueprint("accounts", __name__)


@accounts_bp.route("/accounts")
def get_accounts():
    accs = Account.all(qb=quick_books.quickbooks_client)
    return [acc.to_json() for acc in accs]
