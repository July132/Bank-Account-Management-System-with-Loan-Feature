account_holders = []
balances = []
transaction_histories = []
loans = []

MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03


def create_account():
    """Create a new bank account."""
    name = input("Enter your name: ")
    account_holders.append(name)
    balances.append(0)
    transaction_histories.append([])
    loans.append(0)
    print("You have successfully created an account!")
    print()


def deposit():
    """Deposit money into an account."""
    name = input("Enter your name: ")
    name_index = 0
    for i in account_holders:
        if name not in account_holders:
            print("Account not found.")
            return
        if i == name:
            print("Account found!")
            break
        name_index += 1
    deposit_amount = float(input("Enter an amount to deposit: "))
    balances[name_index] = float(balances[name_index]) + deposit_amount
    transaction = f"{name}|deposited->{deposit_amount}"
    transaction_histories[name_index].append(transaction)
    print(f"The new balance is: {balances[name_index]}")


def withdraw():
    """Withdraw money from an account."""
    name = input("Enter your name: ")
    name_index = 0
    for i in account_holders:
        if name not in account_holders:
            print("Account not found.")
            print()
            return
        if i == name:
            print("Account found!")
            break
        name_index += 1
    withdraw_amount = float(input("Enter an amount to withdraw: "))
    if balances[name_index] < withdraw_amount:
        print("Insufficient funds.")
        print()
        return
    balances[name_index] = balances[name_index] - withdraw_amount
    print(f"The new balance is: {balances[name_index]}")
    transaction = f"{name}|withdrew->{withdraw_amount}"
    transaction_histories[name_index].append(transaction)
    print()


def check_balance():
    """Check the balance of an account."""
    name = input("Enter your name: ")
    name_index = 0
    for i in account_holders:
        if name not in account_holders:
            print("Account not found.")
            print()
            return
        if i == name:
            print("Account found!")
            break
        name_index += 1
    print(f"The balance of your account is: {balances[name_index]}")
    print()


def list_accounts():
    """List all accounts and their balances."""
    if len(account_holders) != 0:
        pass
    else:
        print("No accounts registered")
        print()
        return
    name_index = 0
    print()
    for i in account_holders:
        print(f"Account#{name_index}\n"
              f"Holder: {account_holders[name_index]}\n"
              f"Balance: {balances[name_index]}\n"
              f"Loan: {loans[name_index]}")
        print()
        name_index += 1


def transfer_funds():
    """Transfer funds between two accounts."""
    sender = input("Sender's account name: ")
    recipient = input("Recipient's account name: ")
    if sender in account_holders and recipient in account_holders:
        print("Both accounts found!")
    else:
        print("One or both accounts not found.")
        print()
        return
    transfer_amount = float(input("Enter the amount you want to transfer: "))
    if balances[account_holders.index(f"{sender}")] >= transfer_amount:
        pass
    else:
        print("Insufficient funds!")
        print()
        return
    balances[account_holders.index(f"{sender}")] -= transfer_amount
    balances[account_holders.index(f"{recipient}")] += transfer_amount
    transaction = f"{sender}|{recipient}->{transfer_amount}"
    transaction_histories[account_holders.index(f"{sender}")].append(transaction)
    transaction_histories[account_holders.index(f"{recipient}")].append(transaction)
    print("Transfer of funds successful!")
    print()


def view_transaction_history():
    """View transaction history for a specific account."""
    name = input("Enter your name: ")
    name_index = 0
    for i in account_holders:
        if name not in account_holders:
            print("Account not found.")
            return
        if i == name:
            print("Account found!")
            break
        name_index += 1
    if len(transaction_histories[name_index]) != 0:
        print("Here is the transaction history of your account:")
        print(transaction_histories[name_index])
        print()
    else:
        print("No transactions found.")
        return


def apply_for_loan():
    """Apply for a loan."""
    name = input("Enter the account holder's name: ")

    if name in account_holders:
        index = account_holders.index(name)

        loan_amount = float(input(f"Enter the loan amount (max {MAX_LOAN_AMOUNT} leva): "))

        if loan_amount <= MAX_LOAN_AMOUNT:
            balances[index] += loan_amount
            loans[index] += loan_amount * (1 + INTEREST_RATE)

            print(f"Loan of {loan_amount:.2f} leva approved for {name}. New balance: {balances[index]:.2f} leva.")
        else:
            print(f"Loan amount exceeds maximum limit of {MAX_LOAN_AMOUNT} leva.")
    else:
        print("Account not found.")


def repay_loan():
    """Repay a loan."""
    name = input("Enter the account holder's name: ")

    if name in account_holders:
        index = account_holders.index(name)

        repayment_amount = float(input(f"Enter repayment amount (Outstanding loan: {loans[index]:.2f} leva): "))

        if repayment_amount <= loans[index]:
            balances[index] -= repayment_amount
            loans[index] -= repayment_amount

            print(
                f"Repayment of {repayment_amount:.2f} leva accepted for {name}. Remaining loan: {loans[index]:.2f} leva.")
        else:
            print("Repayment amount exceeds outstanding loan.")
    else:
        print("Account not found.")


def display_menu():
    """Display the main menu."""
    print("\n--- Bank Account Management System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Transfer Funds")
    print("7. View Transaction History")
    print("8. Apply for Loan")
    print("9. Repay Loan")
    print("10. Exit")

    choice = int(input("Enter your choice: "))
    return choice


def main():
    """Main function to run the banking system."""
    while True:
        choice = display_menu()
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
