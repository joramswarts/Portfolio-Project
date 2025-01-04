# Portfolio-Project
Project where we analyse student performance

# Automatisering van Data-analyse en Rapportage met Azure en Power BI

## Overzicht
Dit project ontwikkelt een end-to-end pipeline die gebruikmaakt van geautomatiseerde dataverwerking om inzichten te genereren uit de Student Performance Dataset. De pipeline verwerkt de data van scraping tot rapportage via Azure-services en Power BI.

## Doel
Het doel is om een schaalbare en efficiënte pipeline te bouwen die:  
- Data verzamelt via scraping.  
- Opslaat in een beveiligde cloudomgeving (Azure).  
- Machine Learning (ML) modellen traint voor classificatie en regressie.  
- Inzichten visualiseert in interactieve dashboards.

## Projectscope
De pipeline bestaat uit de volgende componenten:
- **Website Scraping:** Automatisch ophalen van de dataset.
- **Blob Storage:** Opslag van ruwe data in Azure Blob Storage.
- **Azure Functions:** Functies voor dataverwerking en opslag.
- **Microsoft SQL Server Database:** Structureren en opslaan van gegevens.
- **Machine Learning Modellen:** Classificatie- en regressiemodellen voor voorspellingen.
- **Power BI Dashboard:** Visualisatie van inzichten en trends.

## Projectfasen

### Fase 1: Scrapen van data
1. Ontwikkel een Python-script om de dataset automatisch te downloaden van desbetreffende databron.
2. Integreer het script in een Azure Function voor automatisering.
3. Gebruik libraries zoals `requests`, `BeautifulSoup` en `selenium`.

### Fase 2: Opslag in Azure Blob Storage
1. Configureer een Azure Blob Storage-account.
2. Schrijf een Python-script om de dataset te verwerken en te uploaden naar de Blob Storage.
3. Voer een integriteitscontrole uit, zoals een checksum.

### Fase 3: Data-uitwisseling en modellering
1. Gebruik een Azure Function om de dataset uit Blob Storage op te halen en te verwerken.
2. Splits de data in trainings- en testdatasets.
3. Train twee ML-modellen:
   - **Classificatiemodel:** Voorspelt of een student een voldoende haalt.
   - **Regressiemodel:** Voorspelt het exacte eindcijfer.
4. Sla de voorspellingen en inzichten op in een aparte dataset.

### Fase 4: Opslag in SQL Server
1. Zet een Microsoft SQL Server Database op in Azure.
2. Ontwerp tabellen voor:
   - Ruwe data vanuit databron.
   - Voorspellingen en inzichten uit de ML-modellen.
3. Gebruik ETL-processen (Extract, Transform, Load) voor veilige data-overdracht.

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
- `requests`
- `beautifulsoup4`
- `selenium`
- `pandas`
- `scikit-learn`
- `pyodbc`
- `mathplotlib`

### Azure Services
- Azure Blob Storage
- Azure Functions
- Azure SQL Database

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
   - Maak een Azure Blob Storage-account.
   - Zet een Azure SQL Database op.

4. **Implementeer Azure Functions:**
   - Voeg het scraping-script en dataverwerkingsscripten toe aan de Functions.

5. **Train ML-modellen:**
   - Gebruik de data van Blob Storage.
   - Sla voorspellingen op in de SQL-database.

6. **Creëer dashboards in Power BI:**
   - Importeer data uit de SQL Server.
   - Ontwerp visuele rapportages en publiceer deze.

## Projectstructuur
```
projectnaam/
├── data/                   # Dataset en ruwe bestanden
├── azure/
│   ├── functions/          # Azure Functions-code
├── notebooks/              # Jupyter Notebooks voor modellering
├── scripts/                # Python-scripts voor ETL en modellering
├── dashboards/             # Power BI-bestanden
├── requirements.txt        # Vereiste libraries
└── README.md               # Projectdocumentatie
```
