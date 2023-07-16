import requests

api_key = "d7eb34408b234a298813627b61643806"

url = "https://newsapi.org/v2/everything?q=tesla&"\
    "from=2023-06-16&sortBy=publishedAt&"\
    "apiKey=d7eb34408b234a298813627b61643806"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])