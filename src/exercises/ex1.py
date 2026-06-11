import pandas as pd
import matplotlib.pyplot as plt
import config


def load_and_eda(file: str) -> pd.DataFrame:
    data = pd.read_csv(file)
    data = data.drop(columns=["HTHG", "HTAG", "HTR"])
    print("Los primeros valores son:")
    print(data.head())
    print("\nLos últimos valores son:")
    print(data.tail())
    print("\nLa información del dataset es:")
    print(data.info())
    print("\nLas estadísticas descriptivas son:")
    print(data.describe())
    return data


def plot_home_away_goals(data: pd.DataFrame) -> None:
    """Boxplot con la distribución de goles de local y visitante."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].boxplot(data["FTHG"].dropna())
    axes[0].set_title("Goles del local")
    axes[0].set_ylabel("Número de goles")
    axes[1].boxplot(data["FTAG"].dropna())
    axes[1].set_title("Goles del visitante")
    axes[1].set_ylabel("Número de goles")
    fig.suptitle("Distribución de goles")
    plt.tight_layout()
    plt.savefig(
        f"img/grafica_ex1_{config.nom_alumne}_{config.date_time}.png"
    )
    plt.close()
