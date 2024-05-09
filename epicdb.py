import glob

import pandas as pd

"""
The Environmental Performance in Construction (EPiC) database python package is a simple api that enables developpers to
seemlessl access data within EPiC. The python package uses Pandas to provide the EPiC database as pandas.DataFrame instance
with all built-in methods for slicing and exporting. We implement three basic methods to query the EPiC db, get all the
database as a pandas.DataFrame instance, or export the database to a csv file (using the built-in method in pandas).

The EPiC database contains hybrid embodied energy, water and greenhouse gas emissions Australia data for more than 200 
different construction materials and elements, alongside metadata.
"""

__author__ = 'André Stephan (ORCID: https://orcid.org/0000-0001-9538-3830)'
__version__ = '1.3'

for filepath in glob.glob('**/*.feather', recursive=True):
    if filepath.endswith('.feather'):
        __EPIC_DB = pd.read_feather(filepath)
        __EPIC_DB = __EPIC_DB.set_index('uuid')
        break
else:
    raise FileNotFoundError('The EPiC Database feather file could not be found. Please reinstall the epicdb package')

_ENERGY_UNIT = 'MJ'
_WATER_UNIT = 'kL'
_GHG_UNIT = 'kgCO2e'
_DENSITY_UNIT = 'kg/m³'
_SPECIFIC_HEAT_UNIT = 'kJ/(kg·K)'


def get_fields() -> list:
    """
    Retrieves the names of all columns of the EPiC database
    :return: a list of strings
    """
    return list(__EPIC_DB.columns)


def get(name: str = None, category: str = None, type: str = None) -> pd.DataFrame:
    """
    Extracts data from the EPiC database. Looks for records in name, category
    This function ignores the case of the query and of the records
    :param query: a string to search for or a list of strings
    :param look_in: a list of the columns of the dataframe to look into
    :return: a pandas DataFrame
    """
    result = __EPIC_DB.copy(deep=True)
    for col, arg in zip(['name', 'category', 'type'], [name, category, type]):
        if arg:
            if isinstance(arg, str):
                result = result.loc[result[col].str.lower().str.contains(arg.lower())]
            else:
                raise TypeError('The arguments "name", "category", and "type" must be strings or None')

    return result


def get_all_db(compact=False) -> pd.DataFrame:
    """
    Returns the the epic_db as a dataframe. Use pd.DataFrame export methods to convert to dictionary, json, or other format
    :param compact: a Boolean flag that specifies if the Database should be streamlined by removing certain columns
    :return: the epic database as a pd.DataFrame
    """
    if compact:
        return __EPIC_DB[['name', 'category', 'type', 'functional_unit', 'energy', 'water', 'ghg']].copy(deep=True)
    else:
        return __EPIC_DB.copy(deep=True)


def to_csv(path: str, compact=False):
    """
    Exports the EPiC database to the csv format
    :param path: the path of the file to use
    :param compact: a Boolean flag that specifies if the Database should be streamlined by removing certain columns
    """
    if not path.endswith('.csv'):
        print('The file path you specified does not end with "csv", we have added the extension for you')
        path += '.csv'
    else:
        pass
    if not compact:
        __EPIC_DB.to_csv(path)
        addendum = ''
    else:
        get_all_db(compact=True).to_csv(path)
        addendum = 'in a compact format.'
    print('Successfully exported the EPiC database to the path', path, addendum)
