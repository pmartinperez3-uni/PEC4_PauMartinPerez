from typing import Tuple
import pandas as pd
import matplotlib.pyplot as plt
import config


def goals_distribution(
    data: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Devuelve la distribución de frecuencias de goles local y visitante."""
    distr_goals_home = (
        data["FTHG"].value_counts()
        .sort_index()
        .rename("num_matches")
        .to_frame()
    )
    distr_goals_home.index.name = "FTHG"

    distr_goals_away = (
        data["FTAG"].value_counts()
        .sort_index()
        .rename("num_matches")
        .to_frame()
    )
    distr_goals_away.index.name = "FTAG"

    return distr_goals_home, distr_goals_away


def plot_goals_ditribution(
    distr_goals_home: pd.DataFrame,
    distr_goals_away: pd.DataFrame,
) -> None:
    """Plot de distribución de goles para local y visitante."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].bar(distr_goals_home.index, distr_goals_home["num_matches"],
                color="steelblue")
    axes[0].set_title("Distribución de goles del local")
    axes[0].set_xlabel("Goles")
    axes[0].set_ylabel("Número de partidos")
    axes[1].bar(distr_goals_away.index, distr_goals_away["num_matches"],
                color="salmon")
    axes[1].set_title("Distribución de goles del visitante")
    axes[1].set_xlabel("Goles")
    axes[1].set_ylabel("Número de partidos")
    plt.tight_layout()
    plt.savefig(
        f"img/grafica_ex3_{config.nom_alumne}_{config.date_time}.png"
    )
    plt.close()
