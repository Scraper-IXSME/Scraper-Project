from bs4 import BeautifulSoup
import requests
import csv
import unittest
import pandas as pd

# AmeriSave Mortgage

csv_file_path = "el-data.csv"

authors = []
location = []
date = []
comments = []
stars = []


def create_csv():
    for i in range(1, 30):
        page_to_scrape = requests.get(
            f"https://www.consumeraffairs.com/finance/amerisave_mortgage.html?page={i}#scroll_to_reviews=true"
        )
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        reviews = soup.findAll("div", attrs={"class": "rvw__cntr"})

        for review in reviews:
            authors.append(review.find("span", attrs={"class": "rvw__inf-nm"}).text)
            location.append(review.find("span", attrs={"class": "rvw__inf-lctn"}).text)
            date.append(review.find("span", attrs={"class": "rvw__rvd-dt"}).text)
            comments.append(review.find("p").text)
            star = review.find("meta", attrs={"itemprop": "ratingValue"})
            if star:
                stars.append(star.get("content"))
            else:
                stars.append("N/A")

    combined_data = zip(authors, location, date, comments, stars)

    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["Author", "Location", "Date", "Comments", "Rating"]
        )  # Write header row
        writer.writerows(combined_data)


class TestScraping(unittest.TestCase):
    def test_scraping(self):
        with open("el-data.csv", mode="r") as file:
            lines = file.readlines()
            self.assertTrue(len(lines) > 0)


df = pd.read_csv(csv_file_path, encoding="ISO-8859-1")

print("pandas reading file: ", df.head())
print("unit testing: ", unittest.main())
