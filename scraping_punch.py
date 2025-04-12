import requests
from bs4 import BeautifulSoup
import time
import csv



base_url = "https://dubawa.org/category/fact-check/page/{}/"

def scrape_page(page_number):

    url = base_url.format(page_number)
    response = requests.get(url)
    # print(response.text)
    soup = BeautifulSoup(response.text, "html5lib")

    unordered_list = soup.find("ul", class_="posts-items")

    lists = unordered_list.find_all("li", class_="post-item")
    for li in lists:
        list_div = li.find("div", class_ = "post-details")

        title = list_div.find("h2", class_="post-title").text.strip()
        print(f"Title: {title}")

        link = list_div.find("a", class_="more-link button").get("href")
        print(f"\tlink: {link}")

        full_content = scrape_article_content(link)
        claim = full_content[0].text
        verdict = full_content[1].text


        print(f"\tContent: {claim}")
        print(f"\tVerdict: {verdict}")

        print("-" * 50)
        print()
        print()
        print()
        with open("created_dataset/dubawa_dataset.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([title, link, claim, verdict])




def scrape_article_content(article_url):
    response = requests.get(article_url)
    soup = BeautifulSoup(response.text, "html5lib")

    div = soup.find("div", class_="entry-content entry clearfix")
    claim= soup.find("p", class_="has-cyan-bluish-gray-background-color has-background")
    verdict = div.find_all("p")
    return verdict[:2]

    



for page in range(1, 190):
    print(f"Scraping page {page}...")
    scrape_page(page)
    time.sleep(5)