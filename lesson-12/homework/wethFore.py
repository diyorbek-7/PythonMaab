from bs4 import BeautifulSoup
with open('weather.html', mode = 'r') as f:
    soup = BeautifulSoup(f,'html.parser')
    soup.prettify()
    rows = soup.find('table').find_all('tr')[1:]
weather_data= []
temperatures = []
for row in rows:
    day = row.find_all('td')[0].text.strip()
    temperature=row.find_all('td')[1].text.strip().replace('°C','')
    condition =row.find_all('td')[2].text.strip()

    weather_data.append((day,temperature,condition))
    temperatures.append((day,temperature))

print('Weather:')
for day,temp,cond in weather_data:
    print(f'{day}:{temp}°C {cond}')

highest_temp_day= max(temperatures,key = lambda x:x[1])
sunny_days = [day for day,temp,cond in weather_data if cond =='Sunny']
print(f"Day with highest temperature: {highest_temp_day[0]} ({highest_temp_day[1]}°C)")

if sunny_days:
    print(f"sunny days:",",".join(sunny_days))
else:
    print('no sunny day')
avg_temp = sum(temp for _, temp in temperatures) / len(temperatures)
print(f"\nAverage Temperature for the week: {avg_temp:.2f}°C")


