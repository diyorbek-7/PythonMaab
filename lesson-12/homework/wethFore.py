from bs4 import BeautifulSoup

with open('weather.html', mode='r', encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

rows = soup.find('table').find_all('tr')[1:]

weather_data = []
temperatures = []

for row in rows:
    columns = row.find_all('td')
    day = columns[0].text.strip()
    temperature = columns[1].text.strip().replace('°C', '')
    condition = columns[2].text.strip()

    temp_num = int(temperature)

    weather_data.append((day, temp_num, condition))
    temperatures.append((day, temp_num))

print('Weather:')
for day, temp, cond in weather_data:
    print(f'{day}: {temp}°C {cond}')

highest_temp_day = max(temperatures, key=lambda x: x[1])
sunny_days = [day for day, temp, cond in weather_data if cond == 'Sunny']

print(f"\nDay with highest temperature: {highest_temp_day[0]} ({highest_temp_day[1]}°C)")

if sunny_days:
    print(f"Sunny days: {', '.join(sunny_days)}")
else:
    print("No sunny day")

avg_temp = sum(temp for _, temp in temperatures) / len(temperatures)
print(f"\nAverage Temperature for the week: {avg_temp:.2f}°C")
