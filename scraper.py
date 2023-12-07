from bs4 import BeautifulSoup
import cloudscraper

class Shoe:
    """Shoe object for describing shoe data"""

    def __init__(self):
        pass




def main():
    url = "https://www.goat.com/search?query=nike&product_condition=used&size_converted=us_sneakers_men_12.5"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    scraper = cloudscraper.create_scraper()
    webpage = scraper.get(url=url, headers=headers)
    soup = BeautifulSoup(webpage.content, "html.parser")
    results = soup.find(id="value")
    results = results.prettify()
    with open("results.txt", "w") as f:
        f.write(results)











if __name__ == "__main__":
    main()