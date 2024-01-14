import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


account_data = pd.read_csv('dataset/account.asc')  
client_data = pd.read_csv('dataset/client.asc')    
card_data = pd.read_csv('dataset/card.asc')
loan_data = pd.read_csv('dataset/loan.asc')
order_data = pd.read_csv('dataset/order.asc')
district_data = pd.read_csv('dataset/district.asc')
disp_data = pd.read_csv('dataset/disp.asc')

combined_data = pd.merge(account_data, loan_data, on='account_id', how='left')

combined_data['is_default'] = combined_data['status'].apply(lambda x: 1 if x == 'B' else 0)

features = ['age', 'income', 'loan_amount']

data_for_model = combined_data[features + ['is_default']].dropna()  # Remover valores ausentes, se houver

# Dividir os dados em conjunto de treinamento e teste
X = data_for_model[features]
y = data_for_model['is_default']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar e treinar um modelo de classificação (Random Forest neste exemplo)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Fazer previsões
predictions = model.predict(X_test)

# Avaliar o desempenho do modelo
accuracy = accuracy_score(y_test, predictions)
print(f"Acurácia do modelo: {accuracy:.2f}")

# Exibir o relatório de classificação
print("Relatório de Classificação:")
print(classification_report(y_test, predictions))
