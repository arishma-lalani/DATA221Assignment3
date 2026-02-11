# Question 8

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

# Find the main article content using the ID provided
main_content_from_website = data_science_wikipedia_website.find("div", id="mw-content-text")

# Use the "mw-parser-output" class to see the actual headings that are hidden inside the div
if main_content_from_website:
    main_article_content = main_content_from_website.find("div", class_="mw-parser-output")

    # Find all h2 headings from inside the main article content
    headings = main_article_content.find_all("h2")

    # List the words that should not be included in the headings
    excluded_headings = ["References", "External links", "See also", "Notes"]

    # Create an empty list to store the valid headings
    valid_headings = []

    # Check each heading
    for heading in headings:
        # Acquire the valid text and strip "[edit]"
        heading_text = heading.get_text().replace("[edit]", "").strip()

        # Skip any headings mentioned under excluded headings
        if any(word in heading_text for word in excluded_headings):
            continue

        # Add the valid heading to the list
        valid_headings.append(heading_text)

    # Save headings to a text file called "headings.txt"
    with open("headings.txt", "w") as file:
        for heading in valid_headings:
            file.write(heading + "\n")  # This newline character ensures it saves it in the .txt file one heading per line

    # Print a message that confirms that the headings have been saved to the .txt file (only for user clarity)
    print("Section headings have been successfully saved to headings.txt")
