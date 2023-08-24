# Patriot Gold Scraper

# importing modules
import requests
from bs4 import BeautifulSoup
import csv


csv_path = 'data-xg.csv'

# URL for scrapping the data
# url = 'https://www.consumeraffairs.com/finance/patriot-gold.html'

authors = []
stars = []
dates = []
comments = []
locations = []


for i in range(1, 7):
    # get URL html
    page = requests.get(
        f'https://www.consumeraffairs.com/finance/patriot-gold.html?page={i}#scroll_to_reviews=true')
    soup = BeautifulSoup(page.text, 'html.parser')
    reviews = soup.findAll('div', attrs={'class': 'rvw__cntr'})
    # next_button = soup.select_one('button.next')

    for review in reviews:
        # author, stars, date, comments, location
        authors.append(review.find(
            'span', attrs={'class': 'rvw__inf-nm'}).text)

        star = review.find('meta', attrs={'itemprop': 'ratingValue'})
        if star:
            stars.append(star.get('content'))
        else:
            stars.append('N/A')
        dates.append(review.find('span', attrs={'class': 'rvw__rvd-dt'}).text)
        comments.append(review.find('p').text)
        locations.append(review.find(
            'span', attrs={'class': 'rvw__inf-lctn'}).text)


all_data = zip(authors, locations, dates, comments, stars)

with open(csv_path, mode="w", encoding='utf-8', newline="") as file:
    writer = csv.writer(file)
    writer.writerow(
        ['Author', 'Location', 'Date', 'Comment', 'Stars',]
    )  # Write header row
    writer.writerows(all_data)
