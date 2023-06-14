#Para importar um arquivo CSV usando a biblioteca pandas em Python, você pode usar a read_csvfunção. Aqui está um exemplo:
import pandas as pd

# Provide the path to your CSV file
file_path = "arquivo_em.csv"

# Read the CSV file into a DataFrame
data = pd.read_csv(file_path)

# Now you can work with the 'data' DataFrame
# For example, you can print the first few rows
print(data.head())
