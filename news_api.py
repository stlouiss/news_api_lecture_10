
import requests

base_url = 'https://newsapi.org/v2/top-headlines'
params = {
    "q": "new hampshire",
    "apiKey": NEWSAPI_KEY
}

response = requests.get(base_url, params)
result = response.json()
print(result)

print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')

for news_dictionary in result["articles"]:
    if "New Hampshire" in news_dictionary["title"]:
        print(news_dictionary["title"], "-", news_dictionary["source"]["name"])




