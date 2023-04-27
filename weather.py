import requests
import sys

def print_weather(places: list) -> None:
    for place in places:
        params = {"nTqmM": "",
                    "lang": "ru"}
        # If error appears from server, then show message to console.
        try:
            response = requests.get(f"https://wttr.in/{place}", params=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Connection Error.")
        finally:
            print(response.text)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        places = [i for i in args]
    else:
        places = [
                "Лондон",
                "Шереметьево",
                "череповец",
                ]
    print_weather(places)

