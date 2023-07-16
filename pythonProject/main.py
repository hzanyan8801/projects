import requests

api_key = "d7eb34408b234a298813627b61643806"
url = "https://newsapi.org/v2/everything?q=tesla&" \
    "from=2023-06-16&sortBy=publishedAt&" \
    "apiKey=d7eb34408b234a298813627b61643806"

request = requests.get(url)
content = request.text
print(content)