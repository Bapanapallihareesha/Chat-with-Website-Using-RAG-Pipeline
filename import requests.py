import requests

# URL of the website you want to save
url = "https://www.geeksforgeeks.org/world-wide-web-www/"

# Send an HTTP request to fetch the content of the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the content to a local HTML file
    with open("website_content.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("Website content saved successfully!")
else:
    print(f"Failed to retrieve the website. Status code: {response.status_code}")