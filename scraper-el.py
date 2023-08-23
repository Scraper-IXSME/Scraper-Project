from bs4 import BeautifulSoup
import requests

# AmeriSave Mortgage
page = 1
next_page = True

authors = []
stars = []
date = []
comments = []
location = []

while next_page:
    page_to_scrape = requests.get(
        f"https://www.consumeraffairs.com/finance/amerisave_mortgage.html?page={page}#scroll_to_reviews=true"
    )
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    reviews = soup.findAll("div", attrs={"class": "rvw__cntr"})

    for review in reviews:
        authors.append(review.find("span", attrs={"class": "rvw__inf-nm"}).text)

    if soup.findAll("div", attrs={"class": "rvw_cntr"}) is None:
        next_page = False
    page += 1

print(authors)
