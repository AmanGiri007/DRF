import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/"
# get_response = requests.get(endpoint, params={"abc": 123},
#                             json={"query": "hello world how are you this is new"})
get_response = requests.post(endpoint, params={"abc": 123},
                             json={"title": "hello world", "content": "From top", "price": "343"})
# print(get_response.text)
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())
