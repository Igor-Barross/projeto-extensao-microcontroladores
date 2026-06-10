import pandas as pd
from pathlib import Path
from config import RAW_FILE


def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)

    return df


if __name__ == "__main__":
    df = load_data(RAW_FILE)

    print(df.head())
