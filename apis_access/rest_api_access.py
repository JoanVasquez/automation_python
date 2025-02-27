import requests

r = requests.get(
    'https://newsapi.org/v2/everything?q=tesla&from=2025-01-27&sortBy=publishedAt&n&apiKey=890603a55bfa47048e4490069ebee18c'
)
content = r.json()
print(content['articles'])
