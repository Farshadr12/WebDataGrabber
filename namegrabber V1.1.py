import requests
from bs4 import BeautifulSoup
names = []
# please enter your website link bellow
base_url = "https://tetaacg.com/product-category/industrial-and-office-equipment/air-curtain/page/"

# if there are pages in your website enter the number bellow
num_pages = 4

# enter the first page separately if it has a deffrent structure url than the base url
first_page_url = "https://tetaacg.com/product-category/industrial-and-office-equipment/air-curtain/"
first_page_response = requests.get(first_page_url)
first_page_soup = BeautifulSoup(first_page_response.text, "html.parser")
first_page_product_titles = first_page_soup.find_all("span", class_="product-title")
names.extend([title.get_text(strip=True) for title in first_page_product_titles])

# Iterate over the remaining pages
for page in range(2, num_pages + 1):
    # Construct the URL for the current page
    url = base_url + str(page) + "/"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <span> tags with class="product-title" Make sure you specify the class
    product_titles = soup.find_all("span", class_="product-title")
    
    names.extend([title.get_text(strip=True) for title in product_titles])

output_file = "product_names.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write("\n".join(names))

print(f"Product names saved to '{output_file}'")
