import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}


def get_data():
    res = requests.get(url="https://opentdb.com/api.php", params=parameters)
    res.raise_for_status()
    data = res.json()
    return data["results"]


question_data = get_data()
