import requests
apr = 'ad513c94c2474c017ee4298342b5702c'
url = 'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
res = requests.get(url)
if res.status_code==200:
    data = res.json()


