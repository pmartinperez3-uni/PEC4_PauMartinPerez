import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import config  # noqa: E402
from exercises import ex1, ex2, ex3, ex4, ex5, ex6, ex7  # noqa: E402

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "LaLiga_Matches.csv")


def run_ex1():
    """Ejecuta el ejercicio 1"""
    print("\n" + "=" * 60)
    print("EJERCICIO 1")
    print("=" * 60)
    data = ex1.load_and_eda(DATA_FILE)
    ex1.plot_home_away_goals(data)
    print(f"\nGráfica del ejercicio 1 guardada en img/")
    return data


def run_ex2(data):
    """Ejecuta el ejercicio 2"""
    print("\n" + "=" * 60)
    print("EJERCICIO 2")
    print("=" * 60)
    matches_team_total = ex2.total_matches(data)
    print("Los 10 equipos con más partidos son:")
    print(matches_team_total.head(10))

    partidos_totales = matches_team_total["total_matches"].max()
    siempre_en_primera = matches_team_total[
        matches_team_total["total_matches"] == partidos_totales
    ]
    print(f"\nLos equipos que siempre han estado en primera división son:")
    print(siempre_en_primera)
    ex2.plot_matches_team_total(matches_team_total)
    print(f"Gráfica del ejercicio 2 guardada en img/")
    return matches_team_total


def run_ex3(data):
    """Ejecuta el ejercicio 3"""
    print("\n" + "=" * 60)
    print("EJERCICIO 3")
    print("=" * 60)
    distr_goals_home, distr_goals_away = ex3.goals_distribution(data)
    print("La distribución de goles del equipo local es:")
    print(distr_goals_home)
    print("\nLa distribución de goles del equipo visitante es:")
    print(distr_goals_away)
    ex3.plot_goals_ditribution(distr_goals_home, distr_goals_away)
    print(f"Gráfica del ejercicio 3 guardada en img/")


def run_ex4(data):
    """Ejecuta el ejercicio 4"""
    print("\n" + "=" * 60)
    print("EJERCICIO 4")
    print("=" * 60)
    ftr = ex4.FTR(data)
    print("Los resultados FTR son:")
    print(ftr)
    total = ftr["num_matches"].sum()
    casa_porciento = ftr.loc["H", "num_matches"] / total * 100
    print(f"\nPorcentaje de partidos ganados por el local: {casa_porciento:.2f}%")
    ex4.plot_FTR(ftr)
    print(f"Gráfica del ejercicio 4 guardada en img/")


def run_ex5(data):
    """Ejecuta el ejercicio 5"""
    print("\n" + "=" * 60)
    print("EJERCICIO 5")
    print("=" * 60)
    data_con_puntos = ex5.add_points(data)
    print("Dataset con puntos (primeros 10):")
    print(data_con_puntos.head(10))

    total_points_by_team, df_total_points = ex5.fun_total_points(data_con_puntos)
    print("\nTop 10 puntos totales acumulados:")
    print(total_points_by_team.head(10))

    ganador = ex5.alltime_winner(df_total_points)
    print(f"\nGanador histórico LaLiga 1995-2025: {ganador}")
    return data_con_puntos, total_points_by_team, df_total_points


def run_ex6(data, total_points_by_team):
    """Ejecuta el ejercicio 6"""
    print("\n" + "=" * 60)
    print("EJERCICIO 6")
    print("=" * 60)
    home_goals, away_goals, total_goals = ex6.fun_total_goals(data)
    print(f"Goles del local:     {home_goals}")
    print(f"Goles del visitante: {away_goals}")
    print(f"Goles totales:       {total_goals}")

    home_g_team, away_g_team, total_g_team = ex6.fun_total_goals_by_team(data)
    print("\nTop 10 goles totales por equipo:")
    print(total_g_team.head(10))

    summary = ex6.fun_summary_1996_2025(
        total_points_by_team, home_g_team, away_g_team, total_g_team
    )
    print("\nSummary 1995-2025 (primeros valores):")
    print(summary.head())

    ex6.podium(summary)
    print(f"\nGráfica del ejercicio 6 guardada en img/")
    return summary


def run_ex7(data, summary):
    """Ejecuta el ejercicio 7"""
    print("\n" + "=" * 60)
    print("EJERCICIO 7")
    print("=" * 60)
    selected_teams = summary.head(5).index.tolist()
    print("Los 5 equipos seleccionados son:")
    print(selected_teams)
    ex7.graf(data, selected_teams)
    print(f"Gráfica del ejercicio 7 guardada en img/")


def main():
    """Parsea los argumentos y ejecuta los ejercicios."""
    parser = argparse.ArgumentParser(
        description="PEC4 - Análisis de LaLiga 1995-2025 (Pau Martín Pérez)"
    )
    parser.add_argument(
        "-ex",
        type=int,
        default=7,
        help="Ejecuta los ejercicios del 1 al N (por defecto 7)",
    )
    args = parser.parse_args()
    n = args.ex

    os.chdir(os.path.dirname(__file__))

    data = run_ex1()
    if n < 2:
        return

    run_ex2(data)
    if n < 3:
        return

    run_ex3(data)
    if n < 4:
        return

    run_ex4(data)
    if n < 5:
        return

    _, total_points_by_team, _ = run_ex5(data)
    if n < 6:
        return

    summary = run_ex6(data, total_points_by_team)
    if n < 7:
        return

    run_ex7(data, summary)


if __name__ == "__main__":
    main()
