import requests


print(requests.get("http://127.0.0.1:8000/items?count=20").json())
print(requests.get("http://127.0.0.1:8000/items?category=tools").json())



print(requests.get("http://127.0.0.1:8000/items?category=ingredient").json())





print(requests.get("http://127.0.0.1:8000/items/?count=Hello").json())


print(
    requests.post(
        "http://127.0.0.1:8000/",
        json={"name": "Screwdriver", "price": 3.99, "count": 'Hello', "id": 4},
    ).json()
)


