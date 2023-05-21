import json
from quick_books.models.accounts.accounts_interface import Classification, AccountType, CurrencyRef, \
    ModificationMetaData


class Account:
    classification: Classification
    currency_ref: CurrencyRef
    account_type: AccountType
    active: bool
    balance: int
    metadata: ModificationMetaData



    def __init__(self, fully_qualified_name, domain, name, classification, account_sub_type, currency_ref,
                 current_balance_with_sub_accounts, sparse, metadata, account_type, current_balance, active,
                 sync_token, id, sub_account):
        self.fully_qualified_name = fully_qualified_name
        self.domain = domain
        self.name = name
        self.classification = classification
        self.account_sub_type = account_sub_type
        self.currency_ref = currency_ref
        self.current_balance_with_sub_accounts = current_balance_with_sub_accounts
        self.sparse = sparse
        self.metadata = metadata
        self.account_type = account_type
        self.current_balance = current_balance
        self.active = active
        self.sync_token = sync_token
        self.id = id
        self.sub_account = sub_account

    @staticmethod
    def from_json(obj):
        return Account(
            obj.get('FullyQualifiedName'),
            obj.get('domain'),
            obj.get('Name'),
            obj.get('Classification'),
            obj.get('AccountSubType'),
            CurrencyRef.from_json(obj.get("CurrencyRef")),
            obj.get('CurrentBalanceWithSubAccounts'),
            obj.get('sparse'),
            ModificationMetaData.from_json(obj.get('MetaData')),
            obj.get('AccountType'),
            obj.get('CurrentBalance'),
            obj.get('Active'),
            obj.get('SyncToken'),
            obj.get('Id'),
            obj.get('SubAccount')
        )

    @staticmethod
    def from_array(obj):
        return [Account.from_json(acc) for acc in obj]

    def __json__(self):
        return json.dumps(self, default=lambda o: o.__dict__)