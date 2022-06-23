import requests


def research():
    search = input("Search for: ")
    r = requests.get("https://en.wikipedia.org/w/index.php?search=" + search)

    res = r.url

    print(res)


research()
