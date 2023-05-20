import config

SESSION_ACCESS_TOKEN = "token"
SESSION_REFRESH_TOKEN = "refreshToken"
SESSION_REALM_ID = "realmId"
SESSION_TOKEN_EXPIRATION = "token_expiration"
SESSION_REFRESH_EXPIRATION = "refresh_expiration"
SESSION_LAST_REFRESH = "last_refresh"

SESSION_MINUTE_API_CALLS = "minute_api_calls"
SESSION_CURRENT_MINUTE = "api_minute"

MAX_CALLS_PM = int(config.config["api"]["max_calls_pm"])
