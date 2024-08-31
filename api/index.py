from flask import Flask, request, jsonify
import cloudscraper
from bs4 import BeautifulSoup
from urllib.parse import quote

app = Flask(__name__)

# Initialize cloudscraper
scraper = cloudscraper.create_scraper()

def scrape_pdf_drive(query, results_per_page=10):
    # URL encode the query to handle special characters
    encoded_query = quote(query)
    url = f"https://www.pdfdrive.com/search?q={encoded_query}"
    
    try:
        response = scraper.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except (cloudscraper.exceptions.CloudScraperException, ValueError) as e:
        print(f"Request failed: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', class_='file-left')

    # Fetch the first results_per_page items
    data = []
    for result in results[:results_per_page]:
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

@app.route("/search")
def search():
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "No search query provided"}), 400

    results = scrape_pdf_drive(query)
    return jsonify({"data": results})

if __name__ == '__main__':
    app.run(debug=True)
