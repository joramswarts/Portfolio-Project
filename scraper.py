import os
import zipfile
import requests
from bs4 import BeautifulSoup
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# Azure configuratie
STORAGE_ACCOUNT_NAME = "bdtscraper"
CONTAINER_NAME = "csv-files"

# Gebruik Azure AD Authentication
def get_blob_service_client():
    try:
        # Gebruik de DefaultAzureCredential voor automatische authenticatie
        credential = DefaultAzureCredential()
        blob_service_client = BlobServiceClient(
            account_url=f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net",
            credential=credential
        )
        return blob_service_client
    except Exception as e:
        print(f"Fout bij het verkrijgen van de Blob Service Client: {e}")
        return None

# Upload CSV-bestand naar Azure Blob Storage
def upload_to_blob_storage(file_path, container_name):
    blob_service_client = get_blob_service_client()
    if not blob_service_client:
        print("Kan geen verbinding maken met Azure Blob Storage")
        return
    
    try:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=os.path.basename(file_path))
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f"Bestand geüpload: {file_path} naar container {container_name}")
    except Exception as e:
        print(f"Fout bij uploaden naar Azure: {e}")

# Functie om ZIP-bestanden uit te pakken
def extract_zip(file_path, target_dir):
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(target_dir)
            extracted_files = zip_ref.namelist()
            print(f"Uitgepakt: {extracted_files}")
            for extracted_file in extracted_files:
                extracted_path = os.path.join(target_dir, extracted_file)
                if extracted_file.endswith('.zip'):
                    extract_zip(extracted_path, target_dir)
    except Exception as e:
        print(f"Fout bij het uitpakken van {file_path}: {e}")

# Functie om bestanden te downloaden
def download_file(url, save_path):
    response = requests.get(url, stream=True)
    with open(save_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Download voltooid: {save_path}")

# Instellingen
download_dir = os.path.join(os.getcwd(), "downloads")
os.makedirs(download_dir, exist_ok=True)

# Scrape de downloadlink
url = "https://archive.ics.uci.edu/ml/datasets/Student+Performance"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

download_link = None
for link in soup.find_all("a", href=True):
    if link["href"].endswith(".zip"):
        download_link = link["href"]
        break

if download_link:
    full_file_url = download_link if download_link.startswith("http") else f"https://archive.ics.uci.edu{download_link}"
    zip_path = os.path.join(download_dir, "student_data.zip")

    # Download en uitpakken
    download_file(full_file_url, zip_path)
    extract_zip(zip_path, download_dir)

    # Zoek en upload CSV-bestanden naar Azure
    csv_files = [os.path.join(download_dir, f) for f in os.listdir(download_dir) if f.endswith(".csv")]
    if csv_files:
        print(f"Gevonden CSV-bestanden: {', '.join([os.path.basename(f) for f in csv_files])}")
        for csv_file in csv_files:
            upload_to_blob_storage(csv_file, CONTAINER_NAME)
    else:
        print("Geen CSV-bestanden gevonden.")

else:
    print("Downloadlink niet gevonden.")
