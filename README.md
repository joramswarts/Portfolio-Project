# Portfolio-Project

# Studenten prestaties voorspellen en inzichterlijk maken in een handig dashboard 

## Overzicht
Dit project ontwikkelt een end-to-end pipeline die gebruikmaakt van dataverwerking om inzichten te genereren uit de Student Performance Dataset. De pipeline verwerkt de data van scraping tot rapportage via Azure-services en Power BI.

## Doel
Het doel is om een schaalbare en efficiënte pipeline te bouwen die:  
- Data verzamelt via scraping.  
- Opslaat in een beveiligde cloudomgeving (Azure).  
- Machine Learning (ML) modellen traint voor classificatie en regressie.
- Data opslaat in een veilige en bruikbare database.  
- Inzichten visualiseert in interactief dashboard.

## Projectscope
De pipeline bestaat uit de volgende componenten:
- **Website Scraping:** Ophalen van de dataset via Azure Serverless function.
- **Blob Storage:** Opslag van ruwe data in Azure Blob Storage.
- **Azure Data Factory:** Pipelines voor dataverwerking.
- **Microsoft SQL Server Database:** Structureren en opslaan van gegevens.
- **Machine Learning Modellen:** Classificatie- en regressiemodellen voor voorspellingen.
- **Power BI Dashboard:** Visualisatie van inzichten en trends.

## Projectfasen

### Fase 1: Scrapen van data
1. Ontwikkel een Python-script om de dataset automatisch te downloaden van desbetreffende databron.
2. Integreer het script in een Azure Function voor een beveiligde omgeving.
3. Gebruik libraries zoals `requests`, `BeautifulSoup`.

### Fase 2: Opslag in Azure Blob Storage
1. Configureer een Azure Blob Storage-account.
2. Schrijf een Python-script om de dataset te verwerken en te uploaden naar de Blob Storage.
3. Voer een integriteitscontrole uit.

### Fase 3: Data-uitwisseling en modellering
1. Haal brondata uit de azure blob storage.
2. Splits de data in trainings- en testdatasets.
3. Train twee ML-modellen:
   - **Classificatiemodel:** Voorspelt of een student een voldoende haalt.
   - **Regressiemodel:** Voorspelt het exacte eindcijfer.
4. Sla de voorspellingen en inzichten op in de blob storage.

### Fase 4: Opslag in SQL Server
1. Zet een Microsoft SQL Server Database op in Azure.
2. Bouw Data Factory Pipelines voor veilige data overdracht naar database:

### Fase 5: Rapportage met Power BI
1. Importeer de data uit de SQL Server naar Power BI.
2. Ontwerp interactieve dashboards die:
   - Voorspellingen en trends in studentenprestaties tonen.
   - Belangrijke variabelen visualiseren (bijv. studie-uren en prestaties).
   - Vergelijkingen mogelijk maken tussen groepen studenten.

## Benodigdheden
### Software
- **Python** (aanbevolen versie: 3.8+)
- **Power BI Desktop**
- **Azure CLI**

### Python Libraries
- Zie requirements.txt

### Azure Services
- Azure Blob Storage
- Azure Functions
- Azure SQL Database
- Azure Data Factory

## Installatie en Gebruik
1. **Clone deze repository:**
   ```bash
   git clone https://github.com/joramswarts/Portfolio-Project.git
   cd Portfolio-Project
   ```

2. **Installeer vereiste Python-libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configureer Azure:**
   - Maak een Azure account en vraag toegang aan tot benodigde resources bij project owners
  
4. **Start data ophaal process**
   - Open de Functionapp "BDTscraperCode" en open functie "scraper_funtion"
   - Start deze functie door op 'Test & Run' te klikken

5. **Data testen**
   - Voer tests uit zoals in het testplan beschreven om te checken of data klopt.

6. **ML-modellen starten**
   - Run Classificatie-model.ipynb, Regressie-model.ipynb en daarna merged_data.py om data door de modellen te halen en op te slaan in SQL
  
7. **Data testen**
   - Voer tests uit zoals in het testplan beschreven om te checken of data klopt.

8. **Data naar SQL**
   - De data wordt elke 3rde van de maand automatisch naar de SQL server overgezet.
   - Wanneer je dit process eerder wilt testen. Open het Data Factory, open de Author tab. Ga naar "Pipelines" en trigger de 2 pipelines die je ziet staan.

9. **Dashboard refresh**
   - Refresh het dashboard om de nieuwste inzichten te zien.
   - 
## Projectstructuur
```
Portfolio-Project/

├── Classificatie_Model/    # Classificatie model code
├── Dashboard/              # PowerBi Dasboard file
├── Regressie_Model/        # Regressie model code
├── Merged_Data/            # Script wat model data merged en upload naar blob
├── azure-function-scraper  # Azure Serverless scrape function         
├── requirements.txt        # Vereiste libraries
└── README.md               # Projectdocumentatie
```
