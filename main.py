import pandas as pd
import matplotlib.pyplot as plt

"""
https://towardsdatascience.com/a-complete-guide-to-an-interactive-geographical-map-using-python-f4c5197e23e0
"""

data = pd.read_csv(r'C:\Users\Tim Bo\Desktop\Geografische_Diversifikation.csv', sep=';')
data = data[data["Ebenen 1"] == 'Geografische Diversifikation']
data = data[['Ebenen 2', 'IST %']]
data.columns = ['country_code', 'percentage']
data = data[data['country_code'] != 'nan']
data = data.iloc[1:, :]
data.drop_duplicates(['country_code'], keep='first', inplace=True)
data['country_name'] = data.country_code.apply(lambda x: x.split(',')[1])
data.country_code = data.country_code.apply(lambda x: x.split(',')[0])


country_mapping = {
    'DE': 'DEU', 'AT': 'AUT', 'US': 'USA', 'AU': 'AUS', 'BR': 'BRA', 'CA': 'CAN', 'CN': 'CHN',
    'CH': 'CHE', 'CZ': 'CZE', 'CR': 'CRI', 'DK': 'DNK', 'ES': 'ESP', 'FI': 'FIN', 'FR': 'FRA',
    'GB': 'GBR', 'HK': 'HKG', 'IE': 'IRL', 'IL': 'ISR', 'IN': 'IND', 'IT': 'ITA', 'JP': 'JPN',
    'KE': 'KEN', 'KR': 'KOR', 'KY': 'CYM', 'LU': 'LUX', 'MO': 'MAC', 'MX': 'MEX', 'BE': 'BEL',
    'NL': 'NLD', 'NO': 'NOR', 'PH': 'PHL', 'PT': 'PRT', 'RU': 'RUS', 'SA': 'SAU', 'SE': 'SWE',
    'SG': 'SGP', 'TH': 'THA', 'TW': 'TWN', 'ZA': 'ZAF'

}

cmap = plt.get_cmap('plasma')

shape_name = 'admin_0_countries'
countries_shp = sh
