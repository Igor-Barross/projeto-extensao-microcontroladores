import pandas as pd


def count_faixa_etaria(df: pd.DataFrame) -> pd.Series:
    ordem = [
        "Menos de 18 anos",
        "18 a 24 anos",
        "25 a 34 anos",
        "35 a 44 anos",
        "45 anos ou mais",
    ]
    contagem = df["faixa_etaria"].value_counts()
    return contagem.reindex(ordem, fill_value=0)


def count_acesso_internet(df: pd.DataFrame) -> pd.Series:
    return df["acesso_internet"].value_counts()


def count_multiresposta(df: pd.DataFrame, coluna: str) -> pd.Series:
    dummies = df[coluna].fillna("").str.get_dummies(sep=", ")
    dummies.columns = dummies.columns.str.strip()
    return dummies.sum().sort_values(ascending=True)


def count_sim_nao(df: pd.DataFrame, coluna: str) -> pd.Series:
    ordem = ["Sim", "Não"]
    contagem = df[coluna].value_counts()
    return contagem.reindex(ordem, fill_value=0)
