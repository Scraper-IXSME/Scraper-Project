from bs4 import BeautifulSoup
import requests

#..................................................... Scrape all comments.......................................................................

current_page = 1
base_url = f"https://www.consumeraffairs.com/finance/rocket-mortgage.html?page={{page}}#scroll_to_reviews=true"


# for page_num in range(1, 9):  # Iterating through pages 1 to 8
#     base_url = f"https://www.consumeraffairs.com/finance/rocket-mortgage.html?page={page_num}#scroll_to_reviews=true"

#     page_to_scrape = requests.get(base_url)
#     soup = BeautifulSoup(page_to_scrape.text, "html.parser")

#     comments = soup.findAll("div", attrs={"class": "rvw__top-text"})

#     if comments:
#         for comment in comments:
#             print(comment.get_text(strip=True))
#     else:
#         print(f"No comments found on page {page_num}.")

#...................................Get Authors...............................................................................

# for page_num in range(1, 9):  # Iterating through pages 1 to 8
#     base_url = f"https://www.consumeraffairs.com/finance/rocket-mortgage.html?page={page_num}#scroll_to_reviews=true"

#     page_to_scrape = requests.get(base_url)
#     soup = BeautifulSoup(page_to_scrape.text, "html.parser")

#     authors = soup.findAll("span", attrs={"class": "rvw__inf-nm"})

#     if authors:
#         for author in authors:
#             print(author.get_text(strip=True))
#     else:
#         print(f"No author found on page {page_num}.")

# ..............................................Get Date...................................

# for page_num in range(1, 9):  # Iterating through pages 1 to 8
#     base_url = f"https://www.consumeraffairs.com/finance/rocket-mortgage.html?page={page_num}#scroll_to_reviews=true"

#     page_to_scrape = requests.get(base_url)
#     soup = BeautifulSoup(page_to_scrape.text, "html.parser")

#     dates = soup.findAll("span", attrs={"class": "rvw__rvd-dt"})

#     if dates:
#         for date in dates:
#             print(date.get_text(strip=True))
#     else:
#         print(f"No author found on page {page_num}.")

#................................................ Get Location.............................

# for page_num in range(1, 9):  # Iterating through pages 1 to 8
#     base_url = f"https://www.consumeraffairs.com/finance/rocket-mortgage.html?page={page_num}#scroll_to_reviews=true"

#     page_to_scrape = requests.get(base_url)
#     soup = BeautifulSoup(page_to_scrape.text, "html.parser")

#     locations = soup.findAll("span", attrs={"class": "rvw__inf-lctn"})

#     if locations:
#         for location in locations:
#             print(location.get_text(strip=True))
#     else:
#         print(f"No author found on page {page_num}.")

# .............................................. get stars.....................................


stars = []  # List to store star ratings

for page_num in range(1, 9):  # Iterating through pages 1 to 8
    base_url = f"https://www.consumeraffairs.com/finance/rocket-mortgage.html?page={page_num}#scroll_to_reviews=true"

    page_to_scrape = requests.get(base_url)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")

    reviews = soup.find_all("div", class_="rvw__cntr")  # Assuming reviews are wrapped in this class

    for review in reviews:
        star = review.find("meta", attrs={"itemprop": "ratingValue"})
        if star:
            stars.append(star.get("content"))
        else:
            stars.append("N/A")

# Print the list of star ratings after processing all pages
for star_rating in stars:
    print(star_rating)


