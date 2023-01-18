![epicdb banner](https://github.com/hybridlca/epicdb/blob/main/epicdb_banner.png)

# epicdb

epicdb is a __python__ package which enables you to extract data from the [Environmental Performance in Construction (EPiC) Database](http://epicdatabase.com.au). epicdb uses Pandas and treats the EPiC Database as Pandas.DataFrame object. As such, all built-in methods of Pandas.DataFrames can be used. This means that data can be extracted by querying any attribute and can be exported in a single line to a variety of formats, including csv, xlsx, sql, json, feather, etc.

The concept of epicdb is to provide developers with easy access to the EPiC Database as a python package, ensuring the consistency of results, and the access to the latest data by using the latest release.

epicdb uses a static version of the EPiC Database, built-in within the package. We opted for that choice for simplicity and to avoid having to host the EPiC Database on a server and to access it through the API. Future versions of the EPiC Database will be packaged as new versions of the __python__ package. Migrating to a server-based data distrubution with a python package that fetches data from the cloud will be investigated for future versions, and based on user demand.

## Getting Started

### Prerequisites

You will need __python__ to run this package as well as the following python package:
1. [pandas](https://pandas.pydata.org/)

### Installing
Download and install the package from pip
```pip install epicdb```

### Structure of the database

The EPiC Database in the epicdb package comes with 14 fields. These are described one by one below:

1. uuid: a unique identifier for each material and variation. This is used as the index of the Pandas.DataFrame object and can be used to access individual materials directly
2. name: the material name, as reported in the EPiC Database. Note: minor differences might occur.
3. category: the material category, as reported in the EPiC Database, e.g. Metals.
4. type: the material type, as reported in the EPiC Database, e.g. Stainless Steel.
5. functional_unit: the functional unit of the material, i.e. kg, m², m³, no., or m.
6. energy: the hybrid embodied energy coefficient of the material, in MJ
7. water: the hybrid embodied water coefficient of the material, in kL
8. ghg: the hybrid embodied greenhouse gas emissions coefficient of the material, in kgCO<sub>2</sub>e
9. doi: the digital object identifier of the material, linking to its fact sheet and metadata file on figshare
10. density: the density of the material, in kg/m³
11. specific_hear: the specific heat of the material, in kJ/(kg·K)
12. process_proportion_energy: the percentage of process data representing the hybrid embodied energy coefficient of the material, as fraction of 1
13. process_proportion_water: the percentage of process data representing the hybrid embodied water coefficient of the material, as fraction of 1
14. process_proportion_ghg: the percentage of process data representing the hybrid embodied greenhouse gas emissions coefficient of the material, as fraction of 1


## How epicdb works

First you need to import the epicdb package as follows:

```import epicdb as epic```

The epic database is now loaded and ready to be used.

To get a list of all fields of the database

```fields = epic.get_fields()```

To retrieve the entire EPiC Database as a Pandas.DataFrame instance:

```epic_df = epic.get_all_db()```

To get a compact version of the EPiC Database:

```epic_df_c = epic.get_all_db(compact=True)```

To export the entire EPiC Database to csv:

```epic.to_csv(path=your_csv_file_path, compact=True/False)```

To query the EPiC Database for one or more materials, you can query the material name, the material category and/or the material type:

Some examples:

```
concrete_mats = epic.get(name='concrete')
insulation_mats = epic.get(category='insulation')
aluminium_mats = epic.get(type='aluminium')

20_mpa_concrete = epic.get(name='20 mpa concrete')
timber_hardwood_mats = epic.get(category='timber', type='hardwood')

```

Notice that all of the above return Pandas.DataFrame instances so you can call all built-in methods on them, e.g. exporting the concrete materials to csv:

```concrete_mats.to_csv('concrete_mats.csv')```

Once you have queried a subset of the EPiC Database, you can access the coefficients through the columns 'energy', 'water' and 'ghg'. For instance:

```concrete_mats[['energy']]```

returns all the embodied energy coefficients for all concrete materials in the EPiC Database.

Pandas.Dataframes are very powerul data structures. Click [here](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) to explore their built-in methods.


## Built with:

+ [pycharm](https://www.jetbrains.com/pycharm/)
+ Belgian beers and coffee from High Five in Louvain-la-Neuve, Belgium

## Authors and contributors

### Author
[André Stephan](https://github.com/andrestephan1) - _overall design, implementation, testing and debugging_ - [ORCID](https://orcid.org/0000-0001-9538-3830)

### Collaborator
[Robert H Crawford](https://github.com/rhcr) - _brainstorming and project leader of the original EPiC Database_ - [ORCID](https://orcid.org/0000-0002-0189-3221)

## License
This project is shared under a GNU General Public License v3.0. See the [LICENSE](https://github.com/hybridlca/epicdb/blob/main/LICENSE) file for more information.

## Acknowledgments

This python package was funded by the __Belgian Fund for Scientific Research (F.R.S. - FNRS) MIS project F.4547.21, titled [Nested Phoenix](http://nestedphoenix.com)__ at the [Université Catholique de Louvain](https://uclouvain.be/), Belgium. As such, we are endebted to Belgian taxpayers for making this work possible and to the Université Catholique de Louvain for providing the facilities and intellectual space to conduct this research.
