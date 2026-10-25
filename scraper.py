# Books Web Scraper
# Collects book titles and prices from books.toscrape.com and saves them to books.csv


# Step 1: Import dependencies
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import time


# Step 2: Set the starting URL and make an empty list for the results
url = "https://books.toscrape.com/"
rows = []


# Step 3: Repeat for every page
# This loop keeps running as long as "url" has a value.
# When we reach the last page, url becomes None and the loop stops.
while url:
    print("Scraping:", url)

    # Step 4: Download the page
    # timeout=30 means wait up to 30 seconds for the site to answer
    response = requests.get(url, timeout=30)
    response.raise_for_status()   # stops with an error if the request failed

    # Step 5: Read the HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 6: Find every book on the page and get its title and price
    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        price = book.select_one("p.price_color").text
        rows.append({"title": title, "price": price})

    # Step 7: Find the "next" button and set url to the next page
    # If there is no next button, url becomes None and the loop ends
    next_link = soup.select_one("li.next a")
    url = urljoin(url, next_link["href"]) if next_link else None

    # Step 8: Wait 1 second before the next page (be polite to the website)
    time.sleep(1)


# Step 9: Save everything to a CSV file
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price"])
    writer.writeheader()
    writer.writerows(rows)


# Step 10: Show a message when finished
print("Done! Saved", len(rows), "books to books.csv")