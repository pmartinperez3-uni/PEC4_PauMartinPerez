from typing import Tuple
import pandas as pd
import matplotlib.pyplot as plt
import config


def fun_total_goals(data: pd.DataFrame) -> Tuple[int, int, int]:
    """Calcula goles totales: local, visitante y total."""
    home_goals = int(data["FTHG"].sum())
    away_goals = int(data["FTAG"].sum())
    total_goals = home_goals + away_goals
    return home_goals, away_goals, total_goals


def fun_total_goals_by_team(
    data: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Calcula goles local, visitante y total por equipo."""
    home_goals_by_team = (
        data.groupby("HomeTeam")["FTHG"].sum()
        .rename("home_goals")
        .to_frame()
    )
    away_goals_by_team = (
        data.groupby("AwayTeam")["FTAG"].sum()
        .rename("away_goals")
        .to_frame()
    )
    total_goals_by_team = (
        home_goals_by_team["home_goals"]
        .add(away_goals_by_team["away_goals"], fill_value=0)
        .sort_values(ascending=False)
        .rename("total_goals")
        .to_frame()
    )
    return home_goals_by_team, away_goals_by_team, total_goals_by_team


def fun_summary_1996_2025(
    total_points_by_team: pd.Series,
    home_goals_by_team: pd.DataFrame,
    away_goals_by_team: pd.DataFrame,
    total_goals_by_team: pd.DataFrame,
) -> pd.DataFrame:
    """Combina puntos y goles por equipo en un único DataFrame resumen."""
    summary = pd.concat(
        [total_points_by_team,
         home_goals_by_team,
         away_goals_by_team,
         total_goals_by_team],
        axis=1,
    )
    summary = summary.sort_values("total_points", ascending=False)
    return summary


def podium(summary_1996_2025: pd.DataFrame) -> None:
    """Crea un gráfico de podium con los 3 primeros equipos."""
    top3 = summary_1996_2025.head(3)
    teams = top3.index.tolist()
    points = top3["total_points"].tolist()

    order = [teams[1], teams[0], teams[2]]
    heights = [points[1], points[0], points[2]]
    colors = ["silver", "gold", "#cd7f32"]

    fig, ax = plt.subplots(figsize=(7, 6))
    bars = ax.bar(order, heights, color=colors, width=0.5)
    for bar, name in zip(bars, order):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 5,
            name,
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
        )
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Podium histórico LaLiga 1995-2025")
    plt.tight_layout()
    plt.savefig(
        f"img/grafica_ex6_{config.nom_alumne}_{config.date_time}.png"
    )
    plt.close()
