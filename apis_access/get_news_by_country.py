import requests


def get_news(country):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey=890603a55bfa47048e4490069ebee18c'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(
            f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}"
        )
    return results


print(get_news(country='us'))
