from config import RAW_FILE, PROCESSED_FILE, OUTPUTS_DIR
from load_data import load_data
from clean_data import clean_data, save_processed_data
from analyze_data import (
    count_faixa_etaria,
    count_multiresposta,
    count_sim_nao,
)
from visualize_data import (
    setup_theme,
    save_bar_chart,
    save_barh_chart,
    teal,
    red,
)


def main():
    df_raw = load_data(RAW_FILE)

    df_clean = clean_data(df_raw)
    save_processed_data(df_clean, PROCESSED_FILE)

    setup_theme()

    faixa = count_faixa_etaria(df_clean)
    save_bar_chart(
        faixa,
        "Distribuição por faixa etária",
        "Faixa etária",
        "Quantidade de participantes",
        OUTPUTS_DIR / "faixa_etaria.png",
        colors=None
    )

    dispositivos = count_multiresposta(df_clean, "dispositivos_uso")
    save_barh_chart(
        dispositivos,
        "Dispositivos mais utilizados",
        "Quantidade de participantes",
        "Dispositivo",
        OUTPUTS_DIR / "dispositivos_uso.png",
    )

    inteligentes = count_multiresposta(df_clean, "disp_inteligentes_casa")
    save_barh_chart(
        inteligentes,
        "Dispositivos inteligentes em casa",
        "Quantidade de participantes",
        "Dispositivo inteligente",
        OUTPUTS_DIR / "disp_inteligentes_casa.png",
    )

    conhece_iot = count_sim_nao(df_clean, "conhece_iot")
    save_bar_chart(
        conhece_iot,
        "Conhecimento sobre IoT",
        "Resposta",
        "Quantidade de participantes",
        OUTPUTS_DIR / "conhece_iot.png",
        colors=[teal, red]
    )

    risco = count_sim_nao(df_clean, "risco_seguranca_disp")
    save_bar_chart(
        risco,
        "Percepção de risco em dispositivos inteligentes",
        "Resposta",
        "Quantidade de participantes",
        OUTPUTS_DIR / "risco_seguranca_disp.png",
        colors=[teal, red]
    )

    curso = count_sim_nao(df_clean, "curso_tecnologia")
    save_bar_chart(
        curso,
        "Participantes com curso de tecnologia",
        "Resposta",
        "Quantidade de participantes",
        OUTPUTS_DIR / "curso_tecnologia.png",
        colors=[teal, red]
    )


if __name__ == "__main__":
    main()
