import requests


def avia_parse(origin,dest,dep_date,return_date):

    token = '4123dcb03fb9d7c13dc3c8ec23dad161'
    class_trip = '0'

    response = requests.get(f"https://api.travelpayouts.com/v2/prices/week-matrix?origin=MOW&destination=IST&depart_date=2023-03-13&return_date=2023-03-14&trip_class={class_trip}&sorting=price&currency=rub&market=ru&limit=5&page=1&token={token}")
    print(response.text)