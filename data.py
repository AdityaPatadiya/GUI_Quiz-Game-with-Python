import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

responce = requests.get(url="https://opentdb.com/api.php", params=parameters)
responce.raise_for_status()  # it will automatically give the exception according to the error in the link.
data = responce.json()
question_data = data["results"]
