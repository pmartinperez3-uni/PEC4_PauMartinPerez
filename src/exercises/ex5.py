from typing import Tuple
import numpy as py
import pandas as pd


def add_points(data: pd.DataFrame) -> pd.DataFrame:
    """Añade columnas points_home y points_away según el resultado FTR."""
    condiciones_casa = [data["FTR"] == "H",
                        data["FTR"] == "D",
                        data["FTR"] == "A"]
    condiciones_visitante = [data["FTR"] == "A",
                             data["FTR"] == "D",
                             data["FTR"] == "H"]
    values = [3, 1, 0]
    data = data.copy()
    data["points_home"] = py.select(condiciones_casa, values, default=0)
    data["points_away"] = py.select(condiciones_visitante, values, default=0)
    return data


def fun_total_points(
    data: pd.DataFrame,
) -> Tuple[pd.Series, pd.DataFrame]:
    """Calcula puntos totales acumulados por equipo (Series y DataFrame)."""
    puntos_casa = data.groupby("HomeTeam")["points_home"].sum()
    puntos_visitante = data.groupby("AwayTeam")["points_away"].sum()
    total = (puntos_casa.add(puntos_visitante, fill_value=0)
             .sort_values(ascending=False)
             .rename("total_points"))
    return total, total.to_frame()


def alltime_winner(df_total_points: pd.DataFrame) -> str:
    """Devuelve el equipo con más puntos acumulados."""
    return df_total_points["total_points"].idxmax()
