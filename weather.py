import requests

def print_weather(places: list) -> None:
    for place in places:
        params = {"nTqu": "",
                    "lang": "en"}
        if ord(place[0]) > 122:
            params = {"nTqmM": "",
                    "lang": "ru"}

        try:
            response = requests.get(f"https://wttr.in/{place}", params=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(e)

        print(response.text)


if __name__ == "__main__":
    place_1 = "san%20francisco"
    place_2 = "london"
    place_3 = "svo"
    place_4 = "череповец"
    places = [place_1,
            place_2,
            place_3,
            place_4,
            ]

    print_weather(places)
