import requests
from bs4 import BeautifulSoup


def find_title(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find("h1").get_text()

def find_text(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find("p").get_text()

print(find_text("https://wiadomosci.wp.pl/janusz-kowalski-bronil-ziobro-posla-poniosly-emocje-6844095797385760a"))



