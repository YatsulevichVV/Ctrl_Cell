import json
import networkx as nx
import matplotlib.pyplot as plt
import argparse


def construct_graph(file_name: str) -> nx.DiGraph:
    """
    file_name - name of file which contains entities and relations in JSON format
    return graph where vertex are entities and edges are relations
    """
    with open(f'../responses/{file_name}', "r") as f:
        data = json.load(f)
    G = nx.DiGraph()
    for entity in data["entities"]:
        G.add_node(
            entity["id"],
            label=entity["normalized_name"],
            type=entity["type"]
        )
    for relation in data["relations"]:
        G.add_edge(
            relation["source"],
            relation["target"],
            label=relation["type"]
        )
    return G


def plot_graph(G: nx.DiGraph, file_name: str):
    """
    G - graph of entities and relations of medicine recommendation
    file_name - name of file where plot of graph will be saved
    """
    with open(f'../src/colors.json', "r") as f:
        colors = json.load(f)
    color_map = []
    for node in G.nodes(data=True):
        node_type = node[1]["type"]
        color_map.append(colors[node_type])
    pos = nx.spring_layout(G, k=2.0, seed=42) 
    nx.draw_networkx_nodes(G, pos, node_color=color_map, node_size=100)
    nx.draw_networkx_edges(G, pos, arrowstyle='-', arrowsize=20)
    nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, 'label'), font_size=7)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black', font_size=7)
    plt.axis("off")
    plt.savefig(f'../responses/{file_name}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ent_rel', type=str, help='File name with entities and relations')
    parser.add_argument('plot_graph', type=str, help='File name with pdf plot of graph')
    args = parser.parse_args()
    G = construct_graph(args.ent_rel)
    plot_graph(G, args.plot_graph)


if __name__ == '__main__':
    main()