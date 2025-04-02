import pandas as pd

# Bestandspaden en output-bestanden in een lijst zetten
datasets = [
    ("Regressie_Model/student-mat_regression_predictions.csv", "Classificatie_Model/student-mat_classification_predictions.csv", "Merged_Data/student-mat_merged.csv"),
    ("Regressie_Model/student-por_regression_predictions.csv", "Classificatie_Model/student-por_classification_predictions.csv", "Merged_Data/student-por_merged.csv")
]

# Loop door datasets
for df1_path, df2_path, output_path in datasets:
    # CSV-bestanden laden
    df1 = pd.read_csv(df1_path, sep=';')
    df2 = pd.read_csv(df2_path, sep=';')

    # Gemeenschappelijke kolommen vinden (behalve de uitgesloten kolommen)
    merge_columns = [col for col in df1.columns if col in df2.columns and col not in ['G3', 'Predictions', 'G3_class']]

    # Mergen en opslaan
    merged_df = pd.merge(df1, df2[['G3_class'] + merge_columns], on=merge_columns, how='inner')
    merged_df.to_csv(output_path, index=False, sep=';')

print("Bestanden succesvol samengevoegd en opgeslagen!")
