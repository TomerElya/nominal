from quickbooks import QuickBooks

from auth import auth_client

quickbooks_client = QuickBooks()


def initialize_quickbooks_client(realm_id):
    global quickbooks_client
    quickbooks_client = QuickBooks(
        auth_client=auth_client,
        refresh_token=auth_client.refresh_token,
        company_id=realm_id
    )
