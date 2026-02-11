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

    for holiday in holidays:
        date = holiday["date"]["datetime"]
        print(f"Дата: {date['day']} {date['month']}, ")
        print(f"Название праздника: {holiday['name']}")
        print(f"Описание: {holiday['description']}\n")

if __name__ == "__main__":
    main()