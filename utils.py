import geopandas as gpd
import pandas as pd

country_code_mapping = {
    'DE': 'DEU', 'AT': 'AUT', 'US': 'USA', 'AU': 'AUS', 'BR': 'BRA', 'CA': 'CAN', 'CN': 'CHN',
    'CH': 'CHE', 'CZ': 'CZE', 'CR': 'CRI', 'DK': 'DNK', 'ES': 'ESP', 'FI': 'FIN', 'FR': 'FRA',
    'GB': 'GBR', 'HK': 'HKG', 'IE': 'IRL', 'IL': 'ISR', 'IN': 'IND', 'IT': 'ITA', 'JP': 'JPN',
    'KE': 'KEN', 'KR': 'KOR', 'KY': 'CYM', 'LU': 'LUX', 'MO': 'MAC', 'MX': 'MEX', 'BE': 'BEL',
    'NL': 'NLD', 'NO': 'NOR', 'PH': 'PHL', 'PT': 'PRT', 'RU': 'RUS', 'SA': 'SAU', 'SE': 'SWE',
    'SG': 'SGP', 'TH': 'THA', 'TW': 'TWN', 'ZA': 'ZAF'

}


def get_country_shapes():
    # read shapefile using geopandas
    gdf_shapes = gpd.read_file('data/countryShapes/ne_110m_admin_0_countries.shp')[['ADMIN', 'ADM0_A3', 'geometry']]
    gdf_shapes.columns = ['country_name', 'country_code', 'geometry']

    # drop Antarctica
    gdf_shapes.drop(gdf_shapes.index[159], inplace=True)

    return gdf_shapes


def get_diversification_data(input_path):
    data = pd.read_csv(input_path, sep=';')
    data = data[data["Ebenen 1"] == 'Geografische Diversifikation']
    data = data[['Ebenen 2', 'IST %']]
    data.columns = ['country_code', 'percentage']
    data = data[data['country_code'] != 'nan']
    data = data.iloc[1:, :]
    data.drop_duplicates(['country_code'], keep='first', inplace=True)
    data['country_name'] = data.country_code.apply(lambda x: x[6:])
    data.country_code = data.country_code.apply(lambda x: x[1:4])
    data.percentage = data.percentage.apply(lambda x: float(x.replace(',', '.')))
    data = data[data.percentage > 0.0]

    return data
