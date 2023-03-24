import matplotlib.pyplot as plt
import networkx as nx
from random import randint


def graph_drawing(nodes, edges, nodelists, alg):
    G = nx.complete_graph(len(nodes))

    fig, axe = plt.subplots()
    axe.set_title(alg, loc='right')

    pos = nx.circular_layout(G)

    options = {"edgecolors": "tab:gray", "node_size": 700, "alpha": 0.9}
    nx.draw_networkx_nodes(G, pos, nodelist=nodes, **options)
    kolory = ['#B2ABF2', '#DB2B39', '#F3A712', '#89043D',
              '#F0CEA0', '#534D41', '#18F2B2', '#9B489B', '#124e78',
              '#009ffd', '#232528', '#ff006e', '#8338ec', '#eef36a', '#23ce6b',
              '#FBFF12']

    if len(nodelists) > len(kolory):

        # generate random colors if there is shortage of them
        while len(nodelists) > len(kolory):
            kolor = "#" + str(hex(randint(0, int("ff", base=16))))[2:].zfill(2)
            kolor += str(hex(randint(0, int("ff", base=16))))[2:].zfill(2)
            kolor += str(hex(randint(0, int("ff", base=16))))[2:].zfill(2)

            kolory.append(kolor)

    for i in range(len(nodelists)):
        nx.draw_networkx_nodes(G, pos, ax=axe, nodelist=list(nodelists[i]), node_color=kolory[i], **options)

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=edges,
        width=1,
        alpha=0.5,
    )

    wierzcholki_labels = {}

    for w in range(len(nodes)):
        wierzcholki_labels[w] = w

    nx.draw_networkx_labels(G, pos, wierzcholki_labels, font_size=22, font_color="whitesmoke")

    plt.tight_layout()
    plt.axis("off")
    plt.show()
