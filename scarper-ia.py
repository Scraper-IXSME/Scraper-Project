import csv
from bs4 import BeautifulSoup
import requests
import pandas as pd

def save_to_csv(csv_filename):
    for i in range(6):
        page_num = i + 1
        url = f"https://www.consumeraffairs.com/finance/new-american-funding.html?page={page_num}#scroll_to_reviews=true"
    
        page_to_scrape = requests.get(url)
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")

        # Scrape data
        authors = soup.findAll("span", attrs={"class":"rvw__inf-nm"})
        locations = soup.findAll("span", attrs={"class":"rvw__inf-lctn"})
        dates = soup.find_all("span", attrs={"class":"rvw__rvd-dt"})
        ratings = soup.find_all("meta", attrs={"itemprop": "ratingValue"})
        comments = soup.find_all("div", attrs={"class": "rvw__top-text"})

        reviews = []
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

        # Create a DataFrame
        df = pd.DataFrame(reviews)
        # Save the DataFrame as an Excel file (XLSX format)
        excel_filename = "ia-data.xlsx"
        df.to_excel(excel_filename, index=False)
            
if __name__ == "__main__":
    csv_filename = "ia-data.csv"
    save_to_csv(csv_filename)
    print("CSV data saved as Excel file")
