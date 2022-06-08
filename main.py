import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa03f033b2c5f38f59ff6130d7dc6c3c2"
# Your Auth Token from twilio.com/console
auth_token = "f96e1b7443ca8834c55337ed0c41fb3d"
client = Client(account_sid, auth_token)

#Abrir os seis arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:

    tabela_ventas = pd.read_excel(f'{mes}.xlsx')

    if (tabela_ventas['Vendas'] > 55000).any():
        vendedor = tabela_ventas.loc[tabela_ventas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_ventas.loc[tabela_ventas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes de {mes} alguem bateu a meta. Vendedor:{vendedor}, Vendas:{vendas}')
        message = client.messages.create(
            to="+34617772838",
            from_="+16572555780",
            body=f'No mes de {mes} alguem bateu a meta. Vendedor:{vendedor}, Vendas:{vendas}')
        print(message.sid)





#Para cada arquivo:


#verificar algum valor naquele arquivo é > 55.000 na coluna vendas daquele arquivo.


#Se for >55.000 -> Envia un SMS com o Nome , o mes e as vendas do vendedor

#Caso nao seja maior que se 55.000 nao quero fazer nada


