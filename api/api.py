from flask import Flask, session
import requests
from flask_session import Session

app = Flask("nominal")
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