import pandas as pd


def convert(path: str, path_to: str):
    df = pd.read_excel(path)

    df = df.dropna()

    df.to_json(path_to)


convert('Medicines_output_herbal_medicines.xlsx', 'medicine_ayur.json')
