import requests
from bs4 import BeautifulSoup
import os

# Base URL of the website
base_url = "https://tetaacg.com/product-category/industrial-and-office-equipment/air-curtain/page/"

# Number of pages to scrape
num_pages = 4

# List to store all product names
names = []

# Scrape all pages
for page in range(1, num_pages + 1):
    # Construct the URL for the current page
    url = base_url + str(page) + "/"

    # Send a GET request to the website
    response = requests.get(url)

    # Create BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <div> tags with class="product-inner"
    product_divs = soup.find_all("div", class_="product-inner")

    # Extract product names and download images
    for product_div in product_divs:
        # Extract product name
        product_title = product_div.find("span", class_="product-title")
        name = product_title.get_text(strip=True)
        names.append(name)

        # Download image
        image = product_div.find("img", class_="attachment-woocommerce_thumbnail")
        image_url = image["src"]

        # Determine image file name
        image_name = f"{name}.jpg"

        # Send a GET request to download the image
        image_response = requests.get(image_url)

        # Save the image file
        image_path = os.path.join("product_images", image_name)
        with open(image_path, "wb") as image_file:
            image_file.write(image_response.content)

# Save the names to a text file
output_file = "product_names.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write("\n".join(names))

print(f"Product names saved to '{output_file}'")
