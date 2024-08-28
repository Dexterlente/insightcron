import requests
from bs4 import BeautifulSoup

# URL of the page you want to scrape
url = 'https://bitnodes.io/nodes/#network-snapshot'

# Send a GET request to fetch the page content
response = requests.get(url)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the first element with the class "big col-md-3 text-center"
element = soup.find('div', class_='big col-md-3 text-center')

if element:
    # Get the text of the first element
    full_text = element.get_text(strip=True)

    # Split the text by 'Nodes' and keep the first part, which should be the number
    target_text = full_text.split('Nodes')[0] + 'Nodes'

    print(target_text)
