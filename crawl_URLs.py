import os
import time
from urllib.parse import urlparse
import pdfkit

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

def save_urls_to_pdf(urls, output_folder="Docs"):
    """Save a list of URLs as PDFs."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    start_time = time.time()
    for i, url in enumerate(urls, start=1):
        urls_left = len(urls) - i
        save_as_pdf(url, output_folder, start_time, urls_left)

if __name__ == "__main__":
    urls_to_save = {
        "https://support.relai.app/en/articles/194248-is-relai-available-in-my-country",
        "https://support.relai.app/en/articles/194263-on-which-devices-can-i-use-relai",
        "https://support.relai.app/en/articles/194279-what-are-the-special-features-of-relai",
        "https://support.relai.app/en/articles/194289-why-does-relai-only-support-bitcoin",
        "https://support.relai.app/en/articles/213972-how-do-i-contact-support-in-the-relai-app",
        "https://support.relai.app/en/articles/213973-how-to-change-the-language-in-the-relai-app",
        "https://support.relai.app/en/articles/213973-how-to-change-the-language-in-the-relai-app",
        "https://support.relai.app/en/articles/213974-how-to-change-the-currency-in-the-relai-app",
        "https://support.relai.app/en/articles/213975-how-to-change-the-unit-btc-sats-in-the-relai-app",
        "https://support.relai.app/en/articles/194297-how-much-do-i-pay-in-fees-for-buying-selling-bitcoin",
        "https://support.relai.app/en/articles/194322-what-are-the-limits-for-buying-and-selling-bitcoin",
        "https://support.relai.app/en/articles/194324-at-what-time-will-i-get-the-exchange-rate",
        "https://support.relai.app/en/articles/194327-what-are-the-payment-options",
        "https://support.relai.app/en/articles/194328-how-can-i-delete-an-order",
        "https://support.relai.app/en/articles/213971-updating-payment-methods-in-the-relai-app",
        "https://support.relai.app/en/articles/194330-how-do-i-buy-bitcoin-with-relai",
        "https://support.relai.app/en/articles/194332-at-what-time-does-the-buy-limit-start-and-end",
        "https://support.relai.app/en/articles/194334-with-which-currencies-can-i-buy-bitcoin",
        "https://support.relai.app/en/articles/194337-when-will-i-get-my-bitcoin",
        "https://support.relai.app/en/articles/194339-relai-electrum-with-hardware-wallet-bitbox-trezor-ledger-etc",
        "https://support.relai.app/en/articles/194338-how-do-i-buy-bitcoin-with-relai-on-an-external-wallet",
        "https://support.relai.app/en/articles/194341-why-was-my-money-sent-back-to-me",
        "https://support.relai.app/en/articles/194343-how-to-create-an-auto-invest-plan",
        "https://support.relai.app/en/articles/194345-how-do-i-sell-bitcoin-with-relai",
        "https://support.relai.app/en/articles/194346-how-long-does-it-take-to-get-the-money-in-my-account-after-the-sale",
        "https://support.relai.app/en/articles/194411-what-data-does-relai-store",
        "https://support.relai.app/en/articles/194411-what-data-does-relai-store",
        "https://support.relai.app/en/articles/194444-does-relai-or-anyone-else-have-access-to-my-funds",
        "https://support.relai.app/en/articles/194457-where-are-my-bitcoin-stored",
        "https://support.relai.app/en/articles/194473-how-can-you-operate-without-conducting-any-verification-of-your-customers",
        "https://support.relai.app/en/articles/194489-why-is-my-bank-contacting-me" 
    }
    save_urls_to_pdf(urls_to_save)

