import logging
import azure.functions as func
from scraper_function.scraper_function import scrape_and_process

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("HTTP Trigger ontvangen. Scraping starten...")

    try:
        scraped_data = scrape_and_process()
        return func.HttpResponse(str(scraped_data), mimetype="application/json", status_code=200)
    except Exception as e:
        logging.error(f"Fout bij het uitvoeren van de scraper: {str(e)}")
        return func.HttpResponse(f"Fout opgetreden: {str(e)}", status_code=500)
