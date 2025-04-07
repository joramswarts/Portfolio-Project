import logging
import azure.functions as func
import requests
import zipfile
import io
from bs4 import BeautifulSoup
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# Azure configuratie
STORAGE_ACCOUNT_NAME = "bdtscraper"
CONTAINER_NAME = "csv-files"

# Gebruik Azure AD Authentication
def get_blob_service_client():
    try:
        credential = DefaultAzureCredential()
        return BlobServiceClient(
            account_url=f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net", 
            credential=credential
        )
    except Exception as e:
        logging.error(f"Fout bij het verkrijgen van BlobServiceClient: {e}")
        return None

def upload_to_blob_storage(file_name, file_content):
    try:
        blob_service_client = get_blob_service_client()
        if not blob_service_client:
            raise Exception("BlobServiceClient kon niet worden verkregen.")

        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file_name)
        logging.info(f"Uploaden naar Blob Storage: {file_name}")

        blob_client.upload_blob(file_content, overwrite=True)
        logging.info(f"✅ Bestand geüpload: {file_name} naar container {CONTAINER_NAME}")

        return file_name
    except Exception as e:
        logging.error(f"❌ Fout bij uploaden naar Blob Storage: {e}")
        return None


def extract_and_upload_zip(zip_content, depth=0, max_depth=3):
    """
    Extract en upload bestanden uit een ZIP-bestand. Als er een ZIP-bestand in zit, pak dat dan ook uit (tot max_depth).
    """
    uploaded_files = []
    try:
        with zipfile.ZipFile(io.BytesIO(zip_content), 'r') as zip_ref:
            file_list = zip_ref.namelist()
            logging.info(f"Bestanden in ZIP (diepte {depth}): {file_list}")

            for file_name in file_list:
                with zip_ref.open(file_name) as file:
                    file_content = file.read()

                    if file_name.endswith(".zip"):
                        if depth < max_depth:
                            logging.info(f"📦 Extra ZIP-bestand gevonden: {file_name}. Uitpakken...")
                            uploaded_files += extract_and_upload_zip(file_content, depth + 1, max_depth)
                        else:
                            logging.warning(f"⚠️ Max diepte ({max_depth}) bereikt. ZIP {file_name} wordt niet verder uitgepakt.")
                    elif file_name.endswith(".csv"):
                        logging.info(f"📄 CSV-bestand gevonden: {file_name}. Uploaden...")
                        uploaded = upload_to_blob_storage(file_name, file_content)
                        if uploaded:
                            uploaded_files.append(uploaded)
                        else:
                            logging.error(f"❌ Fout bij uploaden van {file_name}")

    except zipfile.BadZipFile as e:
        logging.error(f"❌ Ongeldig ZIP-bestand: {e}")
    except Exception as e:
        logging.error(f"❌ Fout bij het uitpakken van ZIP-bestand: {e}")
    
    return uploaded_files



def scrape_and_process():
    try:
        url = "https://archive.ics.uci.edu/ml/datasets/Student+Performance"
        logging.info(f"Scraping URL: {url}")
        
        response = requests.get(url)
        response.raise_for_status()
        logging.info("Pagina succesvol opgehaald.")

        soup = BeautifulSoup(response.text, "html.parser")
        download_link = None
        for link in soup.find_all("a", href=True):
            if link["href"].endswith(".zip"):
                download_link = link["href"]
                logging.info(f"Gevonden ZIP-downloadlink: {download_link}")
                break

        if not download_link:
            logging.error("Geen downloadlink gevonden.")
            return []

        full_file_url = download_link if download_link.startswith("http") else f"https://archive.ics.uci.edu{download_link}"
        logging.info(f"Downloaden van ZIP-bestand: {full_file_url}")

        zip_response = requests.get(full_file_url)
        zip_response.raise_for_status()
        logging.info(f"ZIP-bestand succesvol gedownload ({len(zip_response.content)} bytes).")

        return extract_and_upload_zip(zip_response.content)
    
    except requests.RequestException as e:
        logging.error(f"Netwerkfout bij het downloaden van ZIP-bestand: {e}")
        return []
    except Exception as e:
        logging.error(f"Onverwachte fout tijdens scraping: {e}")
        return []
