import requests

url = "https://www.consumeraffairs.com/finance/quicken_loans_mortgage.html"
html = requests.get(url)

print(html.text)