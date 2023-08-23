import csv
from bs4 import BeautifulSoup
import requests


for i in range(6):
    page_num = i + 1
    url = f"https://www.consumeraffairs.com/finance/new-american-funding.html?page={page_num}#scroll_to_reviews=true"
    
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")

csv_filename = "ia-data.csv"

with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=["author", "location", "date", "rating", "comment"])
    csv_writer.writeheader()

    reviews = []
    # # scrape data
    authors = soup.findAll("span", attrs={"class":"rvw__inf-nm"})
    locations = soup.findAll("span", attrs={"class":"rvw__inf-lctn"})
    dates = soup.find_all("span", attrs={"class":"rvw__rvd-dt"})
    ratings = soup.find_all("meta", attrs={"itemprop": "ratingValue"})
    comments = soup.find_all("div", attrs={"class": "rvw__top-text"})

    for author, location, date, rating, comment in zip(authors, locations, dates, ratings, comments):
        review = {
            "author": author.text,
            "location": location.text,
            "date": date.text,
            "rating": rating["content"],
            "comment": comment.text
        }
        reviews.append(review)

        for review in reviews:
            print("Author:", review["author"])
            print("Location:", review["location"])
            print("Date:", review["date"])
            print("Rating:", review["rating"])
            print("Comment:", review["comment"])
            
            
        csv_writer.writerow(review)

    print("file saved")
