from requests import get

print(get('http://127.0.0.1:8083/api/user').json())