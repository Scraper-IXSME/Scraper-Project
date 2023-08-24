import requests
from bs4 import BeautifulSoup

# URL for scrapping the data
base_url = 'https://www.consumeraffairs.com/finance/patriot-gold.html?page={}#scroll_to_reviews=true'

def test_url_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)  # Return the error message

def main():
    for i in range(1, 7):
        url = base_url.format(i)
        print(f"Testing URL: {url}")
        response_content = test_url_response(url)

        if "Error" in response_content:
            print(f"Error response from {url}: {response_content}")
        else:
            print(f"Successful response from {url}")

if __name__ == "__main__":
    main()
