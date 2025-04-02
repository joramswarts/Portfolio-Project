import pandas as pd
from io import StringIO
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# Azure Blob Storage Configuratie (zonder connection string)
STORAGE_ACCOUNT_NAME = "bdtscraper"  # Vervang dit met jouw storage account naam
CONTAINER_NAME = "csv-files"  # Vervang dit met jouw container naam

# Verbinden met Azure Blob Storage via DefaultAzureCredential
def get_blob_service_client():
    credential = DefaultAzureCredential()
    return BlobServiceClient(
        account_url=f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net", 
        credential=credential
    )

# Functie om bestanden te uploaden naar Azure Blob Storage
def upload_to_blob(blob_name, dataframe):
    """Uploads een Pandas DataFrame als CSV naar Azure Blob Storage."""
    blob_service_client = get_blob_service_client()
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)

    csv_buffer = StringIO()
    dataframe.to_csv(csv_buffer, sep=";", index=False)
    
    blob_client.upload_blob(csv_buffer.getvalue(), overwrite=True)
    print(f"Bestand geüpload naar Azure Blob Storage: {blob_name}")

# Bestandspaden en output-bestanden definiëren (nu voor Azure)
datasets = [
    ("Regressie_Model/student-mat_regression_predictions.csv", "Classificatie_Model/student-mat_classification_predictions.csv", "Merged_Data/student-mat_merged.csv"),
    ("Regressie_Model/student-por_regression_predictions.csv", "Classificatie_Model/student-por_classification_predictions.csv", "Merged_Data/student-por_merged.csv")
]

# Loop door datasets en verwerk ze
for df1_path, df2_path, output_path in datasets:
    print(f"Verwerken: {output_path}")

    # CSV-bestanden laden
    df1 = pd.read_csv(df1_path, sep=';')
    df2 = pd.read_csv(df2_path, sep=';')

    # Gemeenschappelijke kolommen vinden (behalve de uitgesloten kolommen)
    merge_columns = [col for col in df1.columns if col in df2.columns and col not in ['G3', 'Predictions', 'G3_class']]

    # Mergen van datasets
    merged_df = pd.merge(df1, df2[['G3_class'] + merge_columns], on=merge_columns, how='inner')

    # Upload het samengevoegde bestand naar Azure Blob Storage
    azure_blob_path = f"Merged_Data/{output_path.split('/')[-1]}"  # Zorgt voor juiste blob-padstructuur
    upload_to_blob(azure_blob_path, merged_df)

print("Alle bestanden succesvol samengevoegd en geüpload naar Azure!")