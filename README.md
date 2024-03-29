# Docs Site Crawler

This repository contains a Python script for crawling a documentation website, visiting all sublinks within a specified base URL sitemap, and saving each page as a PDF in the `Docs` folder.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3.6 or newer
- [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)

## Setup

1. **Clone the Repository**
   Start by cloning this repository to your local machine:

   ```git clone https://github.com/avaid96/Scrape2PDF```
   ```cd docssitecrawler```

2. **Create and Activate a Virtual Environment**

    It's recommended to use a virtual environment for Python projects. This keeps dependencies required by different projects separate. Create a virtual environment in the project directory:

    ```python3 -m venv myenv```
    ```source myenv/bin/activate```

3. **Install Dependencies**

    Install the Python dependencies specified in requirements.txt:
    
    ```pip install -r requirements.txt```

    Ensure wkhtmltopdf is installed on your system and is in your PATH. This tool is used by the script to convert HTML pages to PDF. Installation instructions can be found on the wkhtmltopdf website - https://wkhtmltopdf.org/downloads.html.

3. **Running the Script**
    With the virtual environment activated and dependencies installed, you can run the script as follows:

    ```python crawl-docs.py <your-url>/sitemap.xml```

    This will start the crawling process, saving PDFs of the crawled pages into the Docs folder.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or create an issue if you have any improvements or find any bugs.