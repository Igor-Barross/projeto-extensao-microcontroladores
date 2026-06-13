import pandas as pd
from pathlib import Path
from config import RAW_FILE, PROCESSED_FILE


def clean_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    df = dataframe.copy()

    colunas_rename = {
        "Carimbo de data/hora": "data_hora",
        "Nome completo:": "nome",
        "Qual sua Faixa etária": "faixa_etaria",
        "Você tem acesso frequente à internet?": "acesso_internet",
        "Quais dispositivos você usa no dia a dia?": "dispositivos_uso",
        "Você possui algum dispositivo inteligente em casa? Marque todos que você possui.": "disp_inteligentes_casa",  # noqa:  E501
        "Você acha que esses dispositivos podem trazer riscos de segurança?": "risco_seguranca_disp",  # noqa:  E501
        "Você já ouviu falar em Internet das Coisas (IoT)?": "conhece_iot",
        "Você já fez algum curso de tecnologia, informática ou programação?": "curso_tecnologia",  # noqa:  E501
        "Na sua opinião, como a tecnologia pode te ajudar mais no dia a dia?": "opiniao_tec_dia_a_dia",  # noqa:  E501
    }

    df = df.rename(columns=colunas_rename)
    return df


def save_processed_data(dataframe: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(path, index=False, encoding="utf-8")


if __name__ == "__main__":
    df_raw = pd.read_csv(RAW_FILE)
    df_clean = clean_data(df_raw)
    save_processed_data(df_clean, PROCESSED_FILE)
