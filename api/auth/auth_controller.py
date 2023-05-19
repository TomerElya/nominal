from flask import redirect, request, session

from api.api import app
from auth import auth_client, scopes


@app.route('/auth')
def quick_books_auth():
    url = auth_client.get_authorization_url(scopes)
    return redirect(url)


@app.route("/auth-callback")
def callback():
    auth_client.get_bearer_token(request.args.get("code"), request.args.get("realmId"))
    auth_client.refresh(auth_client.refresh_token)
    session["token"] = auth_client.access_token
    session["realmId"] = request.args.get("realmId")
    session["refershToken"] = auth_client.refresh_token
    return auth_client.access_token

