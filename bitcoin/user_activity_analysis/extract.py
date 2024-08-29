import requests


def extract_unique_address_used():
    url = "https://api.blockchain.info/charts/market-price?timespan=30days&sampled=true&metadata=false&daysAverageString=1d&cors=true&format=json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        values = data.get("values", [])
        if values:
            first_y = int(values[0].get("y"))
            last_y = int(values[-1].get("y"))

            print(f"Last month active unique address {first_y}")
            print(f"This month  active unique address {last_y}")
        else:
            print("No values found in the response.")
    else:
        print(f"Request failed with status code {response.status_code}")


def extract_average_transaction_per_block():
    url = "https://api.blockchain.info/charts/n-transactions-per-block?timespan=30days&sampled=true&metadata=false&daysAverageString=1d&cors=true&format=json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        values = data.get("values", [])
        if values:
            first_y = int(values[0].get("y"))
            last_y = int(values[-1].get("y"))

            print(f"Average transaction size per block last month {first_y}")
            print(f"Average transaction size per block this month {last_y}")
        else:
            print("No values found in the response.")
    else:
        print(f"Request failed with status code {response.status_code}")


# extract_unique_address_used()
extract_average_transaction_per_block()
