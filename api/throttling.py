import datetime

from flask import Blueprint, session, abort

from constants import SESSION_MINUTE_API_CALLS, MAX_CALLS_PM, SESSION_CURRENT_MINUTE

throttling_bp = Blueprint("throttling", __name__)


@throttling_bp.before_app_request
def throttling():
    if SESSION_CURRENT_MINUTE not in session or SESSION_MINUTE_API_CALLS not in session:
        session[SESSION_MINUTE_API_CALLS] = 1
        session[SESSION_CURRENT_MINUTE] = datetime.datetime.now().minute

    if session[SESSION_MINUTE_API_CALLS] + 1 > MAX_CALLS_PM:
        abort(429)

    curr_min = datetime.datetime.now().minute
    if session[SESSION_CURRENT_MINUTE] != curr_min:
        session[SESSION_CURRENT_MINUTE] = curr_min
        session[SESSION_MINUTE_API_CALLS] = 1
    else:
        session[SESSION_MINUTE_API_CALLS] = session[SESSION_MINUTE_API_CALLS] + 1
