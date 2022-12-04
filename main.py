# List of User Fullname, User ID Type and User ID Number
users_info = []

# List of all transactions being made by the user
transactions = []

# We obtain the currency and conversion rate.
money_rate = [
    ['BRL', 'Brazilian Real', 10.79],
    ['CNY', 'Chinese Yuan', 8.05],
    ['EUR', 'Euro', 59.28],
    ['INR', 'Indian Rupee', 0.71],
    ['USD', 'Dollar', 57.21]
]

# Available currency acronym
available_currency = ['BRL', 'CNY', 'EUR', 'INR', 'USD']
retry = True


# This table shows the various currency conversions.
def currency_available():
    print("\n\t\t\t\t\tAvailable Currency Exchange", end="")
    print("""
{}
    {:<15}        {:<15}        {:<10}
{}""".format("≅" * 60, 'Currency Acronym', 'Currency Name', 'Rate to Peso', "≅" * 60))
    for i, k, v in money_rate:
        option, currency, rate = i, k, v
        print("         {:<15}    {:<15}            ₱{:<10}".format(option, currency, rate))
    print()


# Security purposes
def account_security(again):
    account = []
    account_name, account_id = "", ""
    # Ascertain whether the user tried the transaction once more.
    if again:
        print("=" * 90)
        print("For security reasons, kindly enter the right information.\n")
        account_name = input("Enter Fullname: ")
        id_type = input("Enter valid ID type: ")
        account_id = input("Enter ID Number: ")

        if account_id:

            account.append(account_name)
            account.append(id_type)
            account.append(account_id)

            users_info.append(account)
            currency_checker(account_name, account_id)

        else:
            print("{}\n\t\t\tPlease enter the required information!\n{}".format('-' * 60, '-' * 60))
            account_security(again)
    else:
        if not again:
            currency_checker(account_name, account_id)


# Performs a currency check on the user
def currency_checker(account_name, account_id):
    currency_available()
    currency, sum_t = True, True
    while currency:
        currency_name = input("Enter currency acronym: ")
        if currency_name.upper() in available_currency:
            currency = False
            loop_stop = False
            while sum_t:
                try:
                    amount = int(input("Enter the amount: "))
                    if amount:
                        sum_t = False
                        for rate in money_rate:
                            if currency_name.capitalize() == rate[1] or currency_name.upper() == rate[0]:
                                loop_stop = True
                                currency_exchange(amount, rate[2], rate[1], account_name, rate[0], account_id)
                        else:
                            if not loop_stop:
                                print("{}\n\t\t\tThere is no currency name available.\n{}".format('-' * 60, '-' * 60))
                                currency_checker(account_name, account_id)
                    else:
                        print("{}\n\t\t\tPlease enter the required information!\n{}".format('-' * 60, '-' * 60))
                except:
                    print("Enter amount correctly!")
                    pass
        else:
            print("Currency does not exist.")


# Determines the user's currency conversion
def currency_exchange(amount, rate, cr, cur, acry, account_id):
    calc_rate = (amount * rate) - 40
    print("{}\n\t\t\t\tTransaction Confirmation\n{}".format('-' * 60, '-' * 60))
    check_amount = input("The amount is {} in {} Currency. Please confirm! (y/n): ".format(amount, cr))
    if check_amount.capitalize() == "Yes" or check_amount.upper() == "Y" or check_amount.lower() == "y":
        currency, sum_t = True, True
        while currency:
            print("{}\n\t\t\t\tTransaction Confirmation\n{}".format('-' * 60, '-' * 60))
            system_payment = input(
                "The cost for our currency converter is ₱40. Do you still wish to proceed? (y/n): ")
            if system_payment.capitalize() == "Yes" or system_payment.upper() == "Y" or system_payment.lower() == "y":
                currency = False
                receipt(amount, rate, calc_rate, cr)
                transaction_history(cur, account_id, calc_rate, acry)
            elif system_payment.capitalize() == "No" or system_payment.lower() == "n" or system_payment.upper() == "N":
                print('Enjoy your day!😁')
                currency = False
            else:
                print()
    elif check_amount.capitalize() == "No" or check_amount.lower() == "n" or check_amount.upper() == "N":
        currency_checker(acry, account_id)
    else:
        currency_exchange(amount, rate, cr, cur, acry, account_id)


# Display the transaction receipt
def receipt(amount, rate, calc, currency):
    print("\n" * 500)
    print("""
{}
            Money Exchange      ≅        {}
            Currency Name       ≅        {}
                Rate            ≅        ₱{}
            System Payment      ≅        ₱{}
{}
            Total Amount        ≅        ₱{}
{}
""".format("≅" * 60, amount, currency, rate, 40, "≅" * 60, calc, "≅" * 60))


# Function that determines if customer want's another transaction or see the transaction history
def transaction_options():
    print("{}\n\t\t\t\t\tOptional Transactions\n{}".format('-' * 60, '-' * 60))
    transaction_option = input("(H) for transaction history and (R) carrying out another transaction: ")

    if transaction_option.upper() == "H":
        transaction_table()
    elif transaction_option.lower() == "r":
        transaction_retry()
    else:
        print("{}\n\t\t\t\tPlease select (H) and (R)!\n{}".format('-' * 60, '-' * 60))
        transaction_options()


# Function that determines whether you want to try another transaction or not.
def transaction_retry():
    print("{}\n\t\t\t\t\tTransaction Confirmation\n{}".format('-' * 60, '-' * 60))
    retry_input = input("An additional transaction's confirmation. (y/n): ")

    if retry_input.lower() == "y":
        print('\n' * 80)
        again = False
        account_security(again)
    elif retry_input.lower() == "n":
        print('Enjoy your day!')
    else:
        print("{}\n\t\t\tNo such option was found!\n{}".format('-' * 60, '-' * 60))
        transaction_retry()


def transaction_history(name, id_number, calc, acry):
    transac = [calc, acry]

    transactions.append(transac)

    transaction_options()


def transaction_table():
    print("\n" * 500)
    print("\n\t\t\t\t\t\t\tTransaction History", end="")
    print("""
{}
    {:<15}        {:<15}        {:<10}
{}""".format("≅" * 60, 'Transaction', 'Currency Acronym', 'Amount Exchange', "≅" * 60))
    i = 1
    for k, v in transactions:
        i, acry, total = i, v, k
        print("         {:<15}          {:<15}      ₱{:<10}".format(i, acry, total))
        i += 1
    print()
    transaction_retry()


account_security(retry)