import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def extract_node():

    url = 'https://bitnodes.io/nodes/#network-snapshot'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    element = soup.find('div', class_='big col-md-3 text-center')
    if element:
        full_text = element.get_text(strip=True)
        nodes_number = full_text.split('Nodes')[0]

        print(nodes_number)
        return nodes_number


def extract_growth():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://bitnodes.io/dashboard/90d/')

    driver.implicitly_wait(3)

    span_element = driver.find_element(
        By.CSS_SELECTOR, 'h1#change-nodes span.text-success.hidden-xs')
    percentage = span_element.text.strip()

    print(percentage)
    return percentage

    driver.quit()


def extract_latency():

    url = "https://api.blockchain.info/charts/median-confirmation-time?timespan=30days&sampled=true&metadata=false&daysAverageString=1d&cors=true&format=json"
    response = requests.get(url)
    data = response.json()

    latest_median_confirmation_time = data["values"][-1]["y"]
    print(round(latest_median_confirmation_time, 2))
    return round(latest_median_confirmation_time, 2)


extract_node()
extract_growth()
extract_latency()
