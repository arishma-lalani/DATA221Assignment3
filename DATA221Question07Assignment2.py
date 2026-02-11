# Question 7

import requests
from bs4 import BeautifulSoup

# Provide the url that we want to scrape
url = "https://en.wikipedia.org/wiki/Data_science"

# This chunk of code is an extra measure to ensure that we aren't blocked from accessing the Wikipedia page
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)

# Parse the content from the web page using the BeautifulSoup package
data_science_wikipedia_website = BeautifulSoup(response.text, "html.parser")

# Find the Wikipedia page title and print it
if data_science_wikipedia_website.title:
    website_page_title = data_science_wikipedia_website.title.get_text().strip()
    print("Page Title:", website_page_title)

# Find the first paragraph of the main article content using the ID provided
first_paragraph_from_main_content = data_science_wikipedia_website.find("div", id="mw-content-text")

# Find the first paragraph that has at least 50 characters
if first_paragraph_from_main_content:
    paragraphs = first_paragraph_from_main_content.find_all("p")  # Tell BeautifulSoup to find all paragraph tags
    for paragraph in paragraphs:
        text = paragraph.get_text().strip()
        if len(text) >= 50:
            print("\nFirst paragraph:\n")
            print(text)
            break