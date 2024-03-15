import requests
from bs4 import BeautifulSoup
zip_code_info = {
    "90210": {"state": "CA", "city": "Los Angeles"},
    # Add more zip codes with their state and city
}

def get_trulia_listings(zip_code):
    # Check if the zip code exists in the dictionary
    if zip_code in zip_code_info:
        # Extract state and city information from the dictionary
        state = zip_code_info[zip_code]["state"]
        city = zip_code_info[zip_code]["city"]
        
        # Base URL for Trulia's search results
        base_url = f"https://www.trulia.com/{state}/{city}/{zip_code}/"

        # Send a GET request to the URL
        response = requests.get(base_url)
        
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            # print(soup)
            
            # Find all the listings on the page
            listings = soup.find_all('div', class_='Box__BoxElement-sc-1f5rw0h-0 sMbDO Grid__CellBox-sc-144isrp-0 sMrhd')
            print(listings)

            # Extract relevant information from each listing
            for listing in listings:
                address = listing.find('div', class_='Text__TextBase-sc-1cait9d-0-j2PpvL h4').text.strip()
                price = listing.find('div', class_='Text__TextBase-sc-1cait9d-0 gTFTwO').text.strip()
                details = listing.find('div', class_='Text__TextBase-sc-1cait9d-0 bwaKqb').text.strip()
                print(f"Address: {address}\nPrice: {price}\nDetails: {details}\n")

        else:
            print("Failed to retrieve Trulia listings.")
    else:
        print("Zip code not found in the dictionary.")

# Example usage
zipcode = "90210"  # Enter your desired zip code here
get_trulia_listings(zipcode)