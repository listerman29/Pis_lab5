import requests
import json
from datetime import datetime


def get_weather(api_key, city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',
        'lang': 'uk'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Викличе виняток для 4XX/5XX статусів

        data = response.json()

        # Обробка та вивід даних
        print("\n=== Погода в місті ===")
        print(f"Місто: {data.get('name', 'Невідомо')}")
        print(f"Час запиту: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Температура: {round(data['main']['temp'])}°C")
        print(f"Відчувається як: {round(data['main']['feels_like'])}°C")
        print(f"Атмосферний тиск: {data['main']['pressure']} hPa")
        print(f"Вологість: {data['main']['humidity']}%")
        print(f"Вітер: {data['wind']['speed']} м/с")
        print(f"Опис: {data['weather'][0]['description'].capitalize()}")
        print(f"Іконка погоди: https://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png")

    except requests.exceptions.HTTPError as http_err:
        error_data = json.loads(http_err.response.text)
        print(f"\nПомилка {http_err.response.status_code}: {error_data.get('message', 'Невідома помилка API')}")
        print("Поради:")
        print("1. Перевірте правильність написання міста (спробуйте 'Kyiv,UA')")
        print("2. Перевірте ваш API ключ")
    except requests.exceptions.RequestException as req_err:
        print(f"\nПомилка мережі: {req_err}")
    except (KeyError, IndexError) as data_err:
        print(f"\nПомилка обробки даних: {data_err}")
        print("Отримана відповідь:", json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    API_KEY = "40bf489c5e82ca25417b626d380719b2"
    print("Введіть назву міста (наприклад: 'Kiyv,UA'):")
    city = input().strip()

    if not city:
        city = "Kiyv,UA"  # Значення за замовчуванням

    get_weather(API_KEY, city)