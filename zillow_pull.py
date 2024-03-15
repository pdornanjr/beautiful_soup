from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def get_zillow_listings(zip_code):
    # Configure Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    # Base URL for Zillow's search results
    base_url = f"https://www.zillow.com/homes/{zip_code}_rb/"
    
    try:
        # Load the Zillow page
        driver.get(base_url)

        # Get the page source after JavaScript has rendered it
        page_source = driver.page_source

        # Parse the HTML content of the page
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find all the listings on the page
        listings = soup.find_all('article', class_='list-card')

        # Extract relevant information from each listing
        for listing in listings:
            address = listing.find('address').text.strip()
            price = listing.find('div', class_='list-card-price').text.strip()
            details = listing.find('ul', class_='list-card-details').text.strip()
            print(f"Address: {address}\nPrice: {price}\nDetails: {details}\n")
    
    finally:
        # Close the browser window
        driver.quit()

# Example usage
zipcode = "90210"  # Enter your desired zip code here
get_zillow_listings(zipcode)