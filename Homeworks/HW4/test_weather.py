import requests

API_KEY = "886fafae19831bbb5e8061918c1fe6c0"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Функція для отримання погоди по місту"""
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric&lang=ua"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return None
    return data


def test_get_weather():
    # Перевірка запиту для реального міста
    data = get_weather("Kyiv")
    assert data is not None, "Не вдалося отримати дані"
    assert "main" in data, "У відповіді немає ключа 'main'"
    assert "temp" in data["main"], "У відповіді немає температури"

    # Перевірка запиту для неправильного міста
    data = get_weather("NotExistCity123")
    assert data is None, "Повинно повертати None для неправильного міста"

    print("Всі тести пройдено успішно!")


if __name__ == "__main__":
    test_get_weather()