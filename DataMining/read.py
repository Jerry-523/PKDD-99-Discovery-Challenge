import pandas as pd

# Carregar os dados em DataFrames do Pandas
account_data = pd.read_csv('dataset/account.asc')  
client_data = pd.read_csv('dataset/client.asc')    
card_data = pd.read_csv('dataset/card.asc')
loan_data = pd.read_csv('dataset/loan.asc')
order_data = pd.read_csv('dataset/order.asc')
district_data = pd.read_csv('dataset/district.asc')
disp_data = pd.read_csv('dataset/disp.asc')

# Exibindo as primeiras linhas de cada DataFrame para verificar se os dados foram carregados corretamente
print("Dados da Conta:")
print(account_data.head())

print("\nDados do Cliente:")
print(client_data.head())

print("\nDados do Loan:")
print(loan_data.head())

print("\nDados do Card:")
print(card_data.head())

print("\nDados do Order:")
print(order_data.head())

print("\nDados do Disp:")
print(disp_data.head())

print("\nDados do District:")
print(district_data.head())
