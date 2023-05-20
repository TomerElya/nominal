from flask import Flask, session
import requests
from flask_session import Session

from api.accounts.accounts_controller import accounts_bp
from api.auth.auth_controller import auth_bp

app = Flask("nominal")

app.register_blueprint(auth_bp)
app.register_blueprint(accounts_bp)

# Could leverage sessions redis storage in order to allow centralized session storage with access across the entire
# system, using filesystem here in order to have it work.
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)


@app.route("/company")
def get_company():
    realm_id = session["realmId"]
    headers = {
        'Authorization': f'Bearer {session["token"]}',
        'Accept': 'application/json'
    }
    res = requests.get(
        f'https://sandbox-quickbooks.api.intuit.com/v3/company/{realm_id}/companyinfo/{realm_id}',
        headers=headers
    )
    return res.json()

