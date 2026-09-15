import csv
import requests
from bs4 import BeautifulSoup

def scrape_book():
    url="https://toscrape.com"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    books_data=[]
    book_containers=soup.find_all("article", class_="product_pod")
    for book in book_containers:
        title=book.h3.a["title"]
        price_text= book.find("p", class_="price_color").text
        clean_price=float(price_text.replace)
        books_data.append({"title": title,"price": clean_price})
    return books_data
def save_to_cvs(data: list[dict], filename = "book_report_cvs"):
    if not data:
        print("No data to save")
        return
    fieldnames= data[0].keys()
    with open (filename, mode="w", newline="", encoding="utf-8") as file:
       writer = csv.Dictwriter(file, fieldnames=fieldnames)
       writer.writeheader()
       writer.writerows(data)
    print(f"Success! File saved as: {filename}")

if __name__=="__main__":
    print("starting scraping text")
    results= scrape_book()
    print(f"Successfully scraped {len(results)} books!")
    print("First 3 results:", results[:3])