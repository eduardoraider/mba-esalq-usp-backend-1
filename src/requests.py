import requests

response = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
data = response.json()
# print(data["USDBRL"]["bid"])
dollar_rate = float(data["USDBRL"]["bid"])
print(f"Dollar rate: R$ {dollar_rate:.2f}")
