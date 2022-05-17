import networkx as nx

from bokeh.plotting import figure, show, from_networkx, save, curdoc
from bokeh.models import Circle, ColumnDataSource, LabelSet
from bokeh.palettes import Spectral4, Blues4, Spectral8, Blues8


def solution_plot(number_of_buses, G, GA_solution):
    range_of_figure = number_of_buses ** 3 / 4  # 2.5 for 10 buses
    scale_of_graph = 0.8 * range_of_figure  # 2.0 for 10 buses and 2.5 range
    size_of_node = int(25 * (1 / 1.008) ** (number_of_buses - 3))  # for 3 buses = 25
    size_of_node_label = f"{int(15 * (1 / 1.008) ** (number_of_buses - 3))}px"

    # Colors
    modularity_class = {}
    modularity_color = {}
    for i in range(number_of_buses):
        if (i + 1) in GA_solution:
            modularity_color[i + 1] = Spectral8[2]
            modularity_class[i + 1] = 'yes'
        else:
            modularity_color[i + 1] = Spectral8[6]
            modularity_class[i + 1] = 'no'

    nx.set_node_attributes(G, modularity_color, 'modularity_color')
    nx.set_node_attributes(G, modularity_class, 'modularity_class')
    color_by_this_attribute = 'modularity_color'

    HOVER_TOOLTIPS = [
        ("Bus index", "@index"),
        ("Has PMU", "@modularity_class"),
    ]

    p = figure(title="Power grid electrical buses",
               x_range=(-range_of_figure, range_of_figure),
               y_range=(-range_of_figure, range_of_figure),
               tools="pan, wheel_zoom, save, reset",
               active_scroll='wheel_zoom',
               tooltips=HOVER_TOOLTIPS)

    g = from_networkx(G, nx.spring_layout, scale=scale_of_graph, center=(0, 0))  # graph renderer

    g.node_renderer.glyph = Circle(size=size_of_node, fill_color=color_by_this_attribute)

    p.renderers.append(g)

    show(p)
    # save(p, filename=f"graph.html")

    g.node_renderer.glyph.update(fill_color=Spectral8[0])

    # Add Labels
    """node_labels = list(G.nodes())
    x, y = zip(*g.layout_provider.graph_layout.values())
    source = ColumnDataSource({'x': x, 'y': y, 'index': [str(node_labels[i]) for i in range(len(x))]})
    labels = LabelSet(x='x', y='y', text='index', source=source, text_font_size=size_of_node_label)
    p.renderers.append(labels)"""