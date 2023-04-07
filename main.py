import pandas as pd
import os
from dotenv import load_dotenv

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

load_dotenv()


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

numberFrom = os.getenv('TWILIO_PHONE_NUMBER')
numberTo = os.getenv('MY_PHONE_NUMBER')

client = Client(account_sid, auth_token)

month_list = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

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






