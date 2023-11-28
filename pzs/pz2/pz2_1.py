import requests
from bs4 import BeautifulSoup
import json

def get_airports_data():
    """
    Функция получения данных о кодах аэропортов из Википедии.

    Возвращает словарь, где ключом является код аэропорта, а значением - словарь с информацией об аэропорте.
    """

    url = "https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_S"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    airports_data = {}
    for table in soup.find_all("table", class_="wikitable sortable"):
        rows1 = table.find_all("tr")
        cells1 = rows1[2].find_all("td")
        code1 = cells1[0].text
        for row in range(0,len(table.find_all("tr"))):
            strokes = table.find_all("tr")
            cells = strokes[row].find_all("td")
            if (len(cells)) == 4:
                code = cells[1].text
                name = cells[2].text
                city_country = cells[3].text.split(",")
                city = city_country[0]
                country = city_country[len(city_country)-1]

                airports_data[code] = {
                    "name": name,
                    "city": city,
                    "country": country,
                }

    return airports_data


def get_airport_code(airport_name, language):
    """
    Функция получения кода аэропорта по его названию.

    Возвращает код аэропорта или None, если аэропорт не существует.
    """

    airports_data = get_airports_data()

    if language == "ru":
        airport_name = airport_name.lower()

    for code, airport in airports_data.items():
        if language == "ru":
            if airport["name"].lower() == airport_name:
                return code
        else:
            if airport["name"] == airport_name:
                return code

    return None


if __name__ == "__main__":
    # Пример использования
    airport_code = get_airport_code("Grant County Airport", "ru")
    print(airport_code)

    open("airports.json", "w").write(json.dumps(get_airports_data()))
    # Результат:
    # SVO

