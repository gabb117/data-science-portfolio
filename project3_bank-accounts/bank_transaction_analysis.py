import pandas as pd
import os
print("Current working directory:", os.getcwd())


def loading_data():
    
    accounts = pd.read_csv('/Users/gabrielesagnelli/Desktop/data-science-portfolio/project3_bank-accounts/bank_account.csv')
    transactions = pd.read_csv('/Users/gabrielesagnelli/Desktop/data-science-portfolio/project3_bank-accounts/transactions.csv')
    return accounts, transactions

def calculate_account_balances(accounts, transactions):
    
    merged_df = pd.merge(accounts, transactions, on='Account', how='left') #it returns a dataframe with all the rows of the left dataframe and the common rows of the right dataframe.
    account_amount_balance = merged_df.groupby('Account')['Amount'].sum() #it returns a dataframe with the sum of the Amount column for each group of the Account column.
    return(account_amount_balance)
        
def calculate_account_balances_causal(transactions):
    return transactions.groupby(['Account','Causal'])['Amount'].sum()
    #it returns a dataframe with the sum of the Amount column for each group of the Account and Causal columns.

def branch_operations_recovery(accounts, transactions, branch):
 
    merged_df = pd.merge(accounts, transactions, on='Account', how='inner')
    #it returns a dataframe with the common rows of both dataframes.
    branch_df = merged_df[merged_df['Branch'] == branch]
    #it returns a dataframe with the rows of the merged_df dataframe that have the value of the Branch column equal to the branch parameter.
    total = branch_df[['Date', 'Amount', 'Causal', 'Account']]
    #it returns a dataframe with the columns Date, Amount, Causal and Account of the branch_df dataframe.
    return total

def balance_bybranch_recovery(accounts, transactions):
    accounts_transactions = pd.merge(accounts, transactions, on='Account', how='inner')
    #it returns a dataframe with the common rows of both dataframes.
    balance_bybranch = accounts_transactions.groupby(['Branch', 'Causal'])['Amount'].sum()
    #it returns a dataframe with the sum of the Amount column for each group of the Branch and Causal columns.
    return balance_bybranch

def inactive_accounts_identify(accounts, transactions):
    active_accounts = transactions['Account'].unique()
    # it returns an array of the unique values in the Account column of the transactions dataframe.
    inactive_accounts = accounts[~accounts['Account'].isin(active_accounts)]
    # it returns a dataframe with the rows of the accounts dataframe that are not in the active_accounts array.
    return inactive_accounts
    

def main ():

    accounts, transactions = loading_data()

    print("Account Balances:")
    print(calculate_account_balances(accounts, transactions))

    print()
    
    print("Account Balances by Causal:")
    print(calculate_account_balances_causal(transactions))

    print()

    print("Branch Operations Recovery for IT001:")
    print(branch_operations_recovery(accounts, transactions, 'IT001'))

    print()

    print("Balance by Branch and Causal:")
    print(balance_bybranch_recovery(accounts, transactions))

    print()

    print("Inactive Accounts:")
    print(inactive_accounts_identify(accounts, transactions))
  



main()