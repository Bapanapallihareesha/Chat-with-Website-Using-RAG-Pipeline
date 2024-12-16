import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to save
url = "https://www.geeksforgeeks.org/world-wide-web-www/"

# Send a GET request to fetch the content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Optional: You can filter the content you want (e.g., the main content)
    # Here we're extracting all text from paragraphs as an example
    paragraphs = soup.find_all('p')
    text_content = "\n".join([p.get_text() for p in paragraphs])

    # Save the content to a file (either as HTML or plain text)
    with open("geeksforgeeks_www_content.html", "w", encoding="utf-8") as file:
        file.write(response.text)  # Save the full HTML content

    # Optionally, save the text content separately if you want only the text
    with open("geeksforgeeks_www_text.txt", "w", encoding="utf-8") as file:
        file.write(text_content)  # Save just the text from paragraphs

    print("Webpage saved successfully!")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")