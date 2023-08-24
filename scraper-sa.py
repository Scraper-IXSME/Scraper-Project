from bs4 import BeautifulSoup
import requests
import csv 

# Rocket_Mortgage

csv_file_path = "sa-data.csv"

base_url = "https://www.consumeraffairs.com/finance/rocket-mortgage.html?page={page}#scroll_to_reviews=true"
data = {'comments': [], 'authors': [], 'dates': [], 'locations': [], 'stars': []}

for page_num in range(1, 9):
    page_to_scrape = requests.get(base_url.format(page=page_num))
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    reviews = soup.find_all("div", class_="rvw__cntr")
    
    for review in reviews:
        # Comments
        comment = review.find("div", attrs={"class": "rvw__top-text"})
        data['comments'].append(comment.get_text(strip=True) if comment else "No comment")
        
        # Authors
        author = review.find("span", attrs={"class": "rvw__inf-nm"})
        data['authors'].append(author.get_text(strip=True) if author else "No author")
        
        # Dates
        date = review.find("span", attrs={"class": "rvw__rvd-dt"})
        data['dates'].append(date.get_text(strip=True) if date else "No date")
        
        # Locations
        location = review.find("span", attrs={"class": "rvw__inf-lctn"})
        data['locations'].append(location.get_text(strip=True) if location else "No location")
        
        # Stars
        star = review.find("meta", attrs={"itemprop": "ratingValue"})
        data['stars'].append(star.get("content") if star else "N/A")

combined_data = zip(data['authors'], data['locations'], data['dates'], data['comments'], data['stars'])



# Write data to CSV file
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(
        ["Author", "Location", "Date", "Comments", "Rating"]
    )  # Write header row
    writer.writerows(combined_data)

# Print success message
print(f"CSV file '{csv_file_path}' has been created.")