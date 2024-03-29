import requests
from bs4 import BeautifulSoup
import pdfkit
import os
import argparse
from urllib.parse import urlparse
import time

def fetch_sitemap_urls(sitemap_url):
    """Fetch URLs from a sitemap."""
    print(f"Fetching sitemap: {sitemap_url}")
    response = requests.get(sitemap_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'xml')  # Use 'xml' parser for parsing sitemap
        urls = [loc.text for loc in soup.find_all('loc')]
        print(f"Found {len(urls)} URLs in the sitemap.")
        return urls
    else:
        print(f"Failed to fetch sitemap: HTTP {response.status_code}")
        return []

def save_as_pdf(url, folder, start_time, urls_left):
    """Save a web page as a PDF file in a specified folder, display time elapsed and URLs left."""
    # Extract a meaningful filename from the URL
    parsed_url = urlparse(url)
    filename = parsed_url.path.replace('/', '_')[1:] + ".pdf"
    if filename == ".pdf":
        filename = "index.pdf"
    filepath = os.path.join(folder, filename)

    options = {
        'quiet': ''
    }
    try:
        pdfkit.from_url(url, filepath, options=options)
        elapsed_time = time.time() - start_time
        print(f"Successfully saved {url} as {filepath}. Time elapsed: {elapsed_time:.2f}s. URLs left: {urls_left}")
    except Exception as e:
        print(f"Failed to save {url} as PDF: {e}")

def download_sitemap_to_pdf(sitemap_url, output_folder="Docs"):
    """Download all URLs in a sitemap to PDF."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    urls = fetch_sitemap_urls(sitemap_url)
    if urls:
        start_time = time.time()
        for i, url in enumerate(urls, start=1):
            urls_left = len(urls) - i
            save_as_pdf(url, output_folder, start_time, urls_left)
    else:
        print("No URLs to process.")

def main():
    parser = argparse.ArgumentParser(description='Download all pages listed in a sitemap.xml to PDF.')
    parser.add_argument('sitemap_url', help='The URL of the sitemap.xml to process.')
    args = parser.parse_args()

    download_sitemap_to_pdf(args.sitemap_url)

if __name__ == "__main__":
    main()
