import requests
from bs4 import BeautifulSoup


def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.find_all("a"))

if __name__ == "__main__":
    get_page(input("What URL do you want to scape?"))
