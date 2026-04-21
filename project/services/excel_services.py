import pandas as pd
from config import EXCEL_FILE

def carregar_excel():
    return pd.read_excel(EXCEL_FILE)

def projetos_pendentes():
    df = carregar_excel()
    return df[df["Status"] == "Pendente"]