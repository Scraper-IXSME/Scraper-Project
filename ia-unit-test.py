import requests

base_url = 'https://www.consumeraffairs.com/finance/new-american-funding.html?page={page_num}#scroll_to_reviews=true'

def test_url_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)  

def main():
    for page_num in range(6):
        url = base_url.format(page_num=page_num)
        print(f"Testing URL: {url}")
        response_content = test_url_response(url)

        if "Error" in response_content:
            print(f"Error response from {url}: {response_content}")
        else:
            print(f"Successful response from {url}")

if __name__ == "__main__":
    main()
