import requests
from bs4 import BeautifulSoup


def repo_contributors():
    url = "https://github.com/bitcoin/bitcoin"
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    span = soup.find('span', {'class': 'Counter ml-1'})

    print(span.text)

# TODO
# def get_monthly_commit():
#     url = "https://github.com/bitcoin/bitcoin/pulse/monthly"
#     response = requests.get(url)

#     if response.status_code == 200:
#         html_content = response.text
#         soup = BeautifulSoup(html_content, 'html.parser')

#     # Find the <span> element with class="text-emphasized"
#     span_tag = soup.find('span', {'class': 'text-emphasized'})

#     if span_tag:
#         # Print the text content of the <span> tag
#         print(span_tag.text.strip())
#     else:
#         print("Span with class='text-emphasized' not found.")

#     else:
#         print("Failed to retrieve the page. Status code:", response.status_code)


repo_contributors()
# get_monthly_commit()
# TODO
