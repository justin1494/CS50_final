import requests
from bs4 import BeautifulSoup


def find_title(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find("h1").get_text()



