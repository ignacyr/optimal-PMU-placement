import networkx as nx

from bokeh.plotting import figure, show, from_networkx, save, curdoc
from bokeh.models import Circle, ColumnDataSource, LabelSet
from bokeh.palettes import Spectral4, Blues4, Spectral8, Blues8


def solution_plot(number_of_buses, G, GA_solution):
    scale_of_graph = number_of_buses ** 3 / 4
    size_of_node = int(25 * (1 / 1.008) ** (number_of_buses - 3))

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
               tools="pan, wheel_zoom, save, reset",
               active_scroll='wheel_zoom',
               tooltips=HOVER_TOOLTIPS,
               plot_width=1000,
               plot_height=700)

    g = from_networkx(G, nx.spring_layout, scale=scale_of_graph, center=(0, 0))  # graph renderer

    g.node_renderer.glyph = Circle(size=size_of_node, fill_color=color_by_this_attribute)

    p.renderers.append(g)

    show(p)
    # save(p, filename=f"graph.html")

    g.node_renderer.glyph.update(fill_color=Spectral8[0])