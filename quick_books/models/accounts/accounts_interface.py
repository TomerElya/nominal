import datetime
from enum import Enum


class Classification(Enum):
    Asset = 'Asset',
    Equity = "Equity",
    Expense = "Expense",
    Liability = "Liability",
    Revenue = "Revenue"


class AccountType(Enum):
    Bank = "Bank"
    AccountsReceivable = "AccountsReceivable"
    OtherCurrentAsset = "OtherCurrentAsset"
    FixedAsset = "FixedAsset"
    OtherAsset = "OtherAsset"
    Equity = "Equity"
    AccountsPayable = "AccountsPayable"
    CreditCard = "CreditCard"
    OtherCurrentLiability = "OtherCurrentLiability"
    LongTermLiability = "LongTermLiability"
    CostofGoodsSold = "CostofGoodsSold"
    Income = "Income"
    OtherIncome = "OtherIncome"
    Expense = "Expense"
    OtherExpense = "OtherExpense"
    NonPosting = "NonPosting"
    DeferredRevenue = "DeferredRevenue"
    EquityDraw = "EquityDraw"
    OpeningBalanceEquity = "OpeningBalanceEquity"
    RetainedEarnings = "RetainedEarnings"


class CurrencyRef:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    @staticmethod
    def from_json(obj):
        return CurrencyRef(
            obj.get("name"),
            obj.get("value")
        )

    def __json__(self):
        return self.__dict__


class ModificationMetaData:
    last_updated_time: datetime.datetime
    create_time: datetime.datetime

    def __init__(self, create_time, last_updated_time):
        self.last_updated_time = last_updated_time
        self.create_time = create_time

    @staticmethod
    def from_json(obj):
        return ModificationMetaData(
            obj.get("CreateTime"),
            obj.get("LastUpdatedTime")
        )

    def __json__(self):
        return self.__dict__
