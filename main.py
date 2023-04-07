import pandas as pd
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACd3cbc7a1984bbbd9a0a233ba3e124537'
auth_token = '1e3708372e314d9bca6f9e0b7839f14c'
client = Client(account_sid, auth_token)

month_list = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
numberFrom = '+15074686651'
numberTo = '+5521994642132'

for month in month_list:
    sales_table = pd.read_excel(f'{month}.xlsx')
    if(sales_table['Vendas'] > 55000).any():
        vendedor = sales_table.loc[sales_table['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = sales_table.loc[sales_table['Vendas'] > 55000, 'Vendas'].values[0]

        msg = f"No mês de {month}, alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}"

        message = client.messages \
            .create(
            body=msg,
            from_=numberFrom,
            to=numberTo
        )
        print(f"Mensagem enviada com sucesso para {numberTo}, e esse é o Id da mensagem: {message.sid}")






