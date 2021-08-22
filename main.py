import requests, json, datetime

# Look for games and their potential time to complete: combine game store apis like cheapshark, itchio, and gog 
# with an api for howlongtobeat

result = requests.get("https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15")
listDeals = json.loads(result.content)
# print(listDeals)

def get_date(posix_time):
    return datetime.datetime.utcfromtimestamp(posix_time).strftime('%Y-%m-%dT%H:%M:%SZ')

for i in listDeals:
    print(f"Title: {i['title']}\nSale Price: {i['salePrice']}\nNormal Price: {i['normalPrice']}\nSavings: {i['savings']}%")
    print(f"Metacritic Score: {i['metacriticScore']}\nSteam Rating: {i['steamRatingPercent']}% {i['steamRatingText']}")
    print(f"Release Date: {get_date(i['releaseDate'])}\nLast Change: {get_date(i['lastChange'])}")
    print(f"Thumbnail: {i['thumb']}")
