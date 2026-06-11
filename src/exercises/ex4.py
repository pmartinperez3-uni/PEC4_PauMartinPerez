import pandas as pd
import matplotlib.pyplot as plt
import config


def FTR(data: pd.DataFrame) -> pd.DataFrame:  # noqa: N802
    """Cuenta partidos ganados por local (H), visitante (A) y empates (D)."""
    ftr = (
        data["FTR"].value_counts()
        .rename("num_matches")
        .to_frame()
    )
    ftr.index.name = "result"
    return ftr


def plot_FTR(ftr: pd.DataFrame) -> None:  # noqa: N802
    """Bar chart con la distribución de resultados FTR."""
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.bar(ftr.index, ftr["num_matches"], color=["green", "orange", "red"])
    ax.set_xlabel("Resultado (H=Local, A=Visitante, D=Empate)")
    ax.set_ylabel("Número de partidos")
    ax.set_title("Distribución de resultados FTR (1995-2025)")
    plt.tight_layout()
    plt.savefig(
        f"img/grafica_ex4_{config.nom_alumne}_{config.date_time}.png"
    )
    plt.close()
