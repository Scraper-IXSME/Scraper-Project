# QuickenLoans  Scraper
import requests
from bs4 import BeautifulSoup
import csv

def scrape_reviews(url):
    page = requests.get(url)
    page.encoding = 'utf-8'  # Set the page encoding to UTF-8
    soup = BeautifulSoup(page.text, 'html.parser')
    reviews = soup.find_all('div', class_='rvw__cntr')

    authors = []
    stars = []
    dates = []
    comments = []
    locations = []

    for review in reviews:
        authors.append(review.find('span', class_='rvw__inf-nm').text)

        star = review.find('meta', itemprop='ratingValue')
        stars.append(star.get('content') if star else 'N/A')

        dates.append(review.find('span', class_='rvw__rvd-dt').text)

        # Check if the <p> tag exists before extracting its text
        comment_tag = review.find('p')
        comments.append(comment_tag.text if comment_tag else 'No comment')

        locations.append(review.find('span', class_='rvw__inf-lctn').text)

    return zip(authors, locations, dates, comments, stars)

def write_to_csv(file_path, data):
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Author', 'Location', 'Date', 'Comment', 'Stars'])
        writer.writerows(data)

csv_path = 'data-ms.csv'
base_url = 'https://www.consumeraffairs.com/finance/quicken_loans_mortgage.html?page={}'

all_data = []
for i in range(1, 34):
    url = base_url.format(i)
    reviews_data = scrape_reviews(url)
    all_data.extend(reviews_data)

write_to_csv(csv_path, all_data)
