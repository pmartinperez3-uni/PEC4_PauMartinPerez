import pandas as pd
import matplotlib.pyplot as plt
import config


def total_matches(data: pd.DataFrame) -> pd.DataFrame:
    """Devuelve el total de partidos jugados por cada equipo."""
    casa = data["HomeTeam"].value_counts()
    visitante = data["AwayTeam"].value_counts()
    matches_team_total = (casa.add(visitante, fill_value=0)
                          .sort_values(ascending=False)
                          .rename("total_matches")
                          .to_frame())
    return matches_team_total


def plot_matches_team_total(matches_team_total: pd.DataFrame) -> None:
    """Bar chart con el total de partidos por equipo."""
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.bar(matches_team_total.index, matches_team_total["total_matches"])
    ax.set_xlabel("Equipo")
    ax.set_ylabel("Número de partidos")
    ax.set_title("Total de partidos jugados por equipo (1995-2025)")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(
        f"img/grafica_ex2_{config.nom_alumne}_{config.date_time}.png"
    )
    plt.close()
