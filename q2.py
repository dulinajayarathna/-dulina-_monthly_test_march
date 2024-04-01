``
def create_account(customer_name,opening_balance):

    account_id=str(uuid.uuid4())


    account_details={
        "customer_name": customer_name,
        "opening_balance":opening_balance,
        "account_id": account_id

    }

    return account_id
    print()


def deposite_money(id,amount):