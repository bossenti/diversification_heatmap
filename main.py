import json

from bokeh.io import show, output_file
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, HoverTool, BoxZoomTool
from bokeh.palettes import brewer
from bokeh.plotting import figure

from utils import get_country_shapes, get_diversification_data

"""
https://towardsdatascience.com/a-complete-guide-to-an-interactive-geographical-map-using-python-f4c5197e23e0
"""

PATH_INPUT = r'data/20210207_Geografische_Diversifikation.csv'
output_file("diversification.html")

# load country shapes and diversification data
gdf_shapes = get_country_shapes()
df_diversification = get_diversification_data(PATH_INPUT)

# merge both dataframes and use country code as key
gdf_merged = gdf_shapes.merge(df_diversification, on='country_code', how='left')

# convert gdf to json
json_merged = json.loads(gdf_merged.to_json())
json_merged = json.dumps(json_merged)

# preparation for plotting
geosource = GeoJSONDataSource(geojson=json_merged)
palette = brewer['BuGn'][8]
palette = palette[::-1]

# maps numbers in range into a sequence of colors
color_mapper = LinearColorMapper(palette=palette, low=0, high=40)
# define custom tick labels for color bar
tick_labels = {'0': '0%', '0.5': '0.5%', '2.5': '2.5%', '5': '5%', '10': '10%', '20': '20%', '30': '30%',
               '40': '40%'}
# create color bar
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=500, height=20, border_line_color=None,
                     location=(0, 0), orientation='horizontal', major_label_overrides=tick_labels)

# create figure object
fig = figure(title='World Heatmap of Diversification', plot_height=600, plot_width=950, toolbar_location='above')
fig.xgrid.grid_line_color = None
fig.ygrid.grid_line_color = None

tooltips = [('country', '@country_name_x'),
            ('percentage', '@percentage{00.0}')]

# add patch renderer
fig.patches('xs', 'ys', source=geosource, fill_color={'field': 'percentage', 'transform': color_mapper},
            line_color='black', line_width=0.25, fill_alpha=1)

fig.add_layout(color_bar, 'below')
fig.add_tools(HoverTool(tooltips=tooltips))
fig.add_tools(BoxZoomTool())

show(fig)
