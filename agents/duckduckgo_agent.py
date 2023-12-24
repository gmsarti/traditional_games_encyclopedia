import requests

def duckduckgo_search(game_name):
    url = f"https://api.duckduckgo.com/?q=board+game+rules+{game_name}&format=json"
    response = requests.get(url)
    data = response.json()
    if data["AbstractText"]:
        return data["AbstractText"]
    else:
        return "No relevant information found on DuckDuckGo."
