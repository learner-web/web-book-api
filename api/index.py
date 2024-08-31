from flask import Flask, request, jsonify
import cloudscraper
from bs4 import BeautifulSoup
from urllib.parse import quote

app = Flask(__name__)

# Initialize cloudscraper
scraper = cloudscraper.create_scraper()

# Function to scrape PDFDrive
def scrape_pdf_drive(query):
    # URL encode the query to handle special characters
    encoded_query = quote(query)
    url = f"https://www.pdfdrive.com/search?q={encoded_query}"
    
    try:
        response = scraper.get(url)  # Use cloudscraper for the request
        response.raise_for_status()  # Raise an exception for HTTP errors
    except (requests.RequestException, ValueError) as e:
        print(f"Request failed: {e}")
        return []

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

# Scrape Science category
def scrape_pdf_drive_science():
    url = f"https://www.pdfdrive.com/category/14"
    
    try:
        response = scraper.get(url)
        response.raise_for_status()
    except (requests.RequestException, ValueError) as e:
        print(f"Request failed: {e}")
        return []

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

# Scrape History category
def scrape_pdf_drive_history():
    url = f"https://www.pdfdrive.com/category/15"
    
    try:
        response = scraper.get(url)
        response.raise_for_status()
    except (requests.RequestException, ValueError) as e:
        print(f"Request failed: {e}")
        return []

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

# Scrape Fitness category
def scrape_pdf_drive_fit():
    url = f"https://www.pdfdrive.com/category/8"
    
    try:
        response = scraper.get(url)
        response.raise_for_status()
    except (requests.RequestException, ValueError) as e:
        print(f"Request failed: {e}")
        return []

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

# Scrape Art category
def scrape_pdf_drive_art():
    url = f"https://www.pdfdrive.com/category/1"
    
    try:
        response = scraper.get(url)
        response.raise_for_status()
    except (requests.RequestException, ValueError) as e:
        print(f"Request failed: {e}")
        return []

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

# Scrape Technology category
def scrape_pdf_drive_tech():
    url = f"https://www.pdfdrive.com/category/5"
    
    try:
        response = scraper.get(url)
        response.raise_for_status()
    except (requests.RequestException, ValueError) as e:
        print(f"Request failed: {e}")
        return []

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

# Scrape Health category
def scrape_pdf_drive_health():
    url = f"https://www.pdfdrive.com/category/112"
    
    try:
        response = scraper.get(url)
        response.raise_for_status()
    except (requests.RequestException, ValueError) as e:
        print(f"Request failed: {e}")
        return []

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

@app.route("/science")
def scie():
    results = scrape_pdf_drive_science()
    return jsonify({"data": results})

@app.route("/history")
def his():
    results = scrape_pdf_drive_history()
    return jsonify({"data": results})

@app.route("/fit")
def fit():
    results = scrape_pdf_drive_fit()
    return jsonify({"data": results})

@app.route("/art")
def art():
    results = scrape_pdf_drive_art()
    return jsonify({"data": results})

@app.route("/tech")
def tec():
    results = scrape_pdf_drive_tech()
    return jsonify({"data": results})

@app.route("/health")
def hea():
    results = scrape_pdf_drive_health()
    return jsonify({"data": results})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
