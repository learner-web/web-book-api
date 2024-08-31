from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

app = Flask(__name__)

# Function to scrape PDFDrive
def scrape_pdf_drive(query):
    # URL encode the query to handle special characters
    encoded_query = quote(query)
    url = f"https://www.pdfdrive.com/search?q={encoded_query}"
    
    try:
        response = requests.get(url)  # Set a timeout for the request
        response.raise_for_status()  # Raise an exception for HTTP errors
    except (requests.RequestException, ValueError) as e:
        print(f"Request failed: {e}")
        return []

    # Use 'html.parser' or 'lxml' to avoid dependency issues with 'html5lib'
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', class_='file-left')
    
    data = []
    for result in results:
        title = result.find('img').get("title", "No title")
        link = result.find('a').get("href", "")
        image = result.find('img').get("src", "")
        if link:
            link = f"https://www.pdfdrive.com{link}"
        data.append({
            'title': title,
            'link': link,
            'image': image
        })
    
    return data

@app.route("/")
def welcome():
    return jsonify({"response": "welcome"})

@app.route("/search")
def search():
    query = request.args.get("book")
    if not query:
        return jsonify({"error": "No search query provided"}), 400

    results = scrape_pdf_drive(query)
    return jsonify({"data": results})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
