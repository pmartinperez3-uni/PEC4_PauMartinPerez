from typing import List
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import config


def graf(data: pd.DataFrame, selected_teams: List[str]) -> None:
    """Dibuja un grafo de conexiones entre los equipos seleccionados."""
    filtrado = data[
        data["HomeTeam"].isin(selected_teams)
        & data["AwayTeam"].isin(selected_teams)
    ]

    grafo = nx.Graph()
    grafo.add_nodes_from(selected_teams)

    edge_counts: dict = {}
    for _, row in filtrado.iterrows():
        par = tuple(sorted([row["HomeTeam"], row["AwayTeam"]]))
        edge_counts[par] = edge_counts.get(par, 0) + 1

    for (u, v), weight in edge_counts.items():
        grafo.add_edge(u, v, weight=weight)

    posicion = nx.circular_layout(grafo)
    edge_labels = {(u, v): d["weight"] for u, v, d in grafo.edges(data=True)}

    fig, ax = plt.subplots(figsize=(10, 8))
    nx.draw_networkx_nodes(grafo, posicion, node_size=1500,
                           node_color="lightblue", ax=ax)
    nx.draw_networkx_labels(grafo, posicion, font_size=9, ax=ax)
    nx.draw_networkx_edges(grafo, posicion, ax=ax)
    nx.draw_networkx_edge_labels(grafo, posicion, edge_labels=edge_labels,
                                 font_size=8, ax=ax)
    ax.set_title("Grafo de conexiones entre los 5 mejores equipos")
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(
        f"img/grafica_ex7_{config.nom_alumne}_{config.date_time}.png"
    )
    plt.close()
