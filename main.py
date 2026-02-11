import requests
import os
from dotenv import load_dotenv


def main():
    load_dotenv()

    URL = "https://calendarific.com/api/v2"
    api_key = os.getenv("API_KEY")
    country = "RU"
    year = "2025"

    response = requests.get(
        f"{URL}/holidays",
        params={
            "api_key": api_key,
            "country": country,
            "year": year
        }
    )

    holidays = response.json()["response"]["holidays"]
    months = {
        1: "Января", 2: "Февраля", 3: "Марта", 4: "Апреля",
        5: "Мая", 6: "Июня", 7: "Июля", 8: "Августа",
        9: "Сентября", 10: "Октября", 11: "Ноября", 12: "Декабря"
    }

    for holiday in holidays:
        date = holiday["date"]["datetime"]
        month_name = months[date['month']]
        print(f"Дата: {date['day']} {month_name} ")
        print(f"Название праздника: {holiday['name']}")
        print(f"Описание: {holiday['description']}\n")


if __name__ == "__main__":
    main()
