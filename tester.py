import pandas as pd
import os.path
import numpy as np
import columns

json_files = os.path.join('./', 'data', 'locations', 'listed_locations4.json')

# main_df = pd.DataFrame()

for file_ in json_files:
    df = pd.read_json(file_)
    df = df.drop(columns == ['info1', 'info2'])

    # regions = np.array(df['region'].tolist()).flatten()
    # regions_df = pd.DataFrame(regions.tolist())
    #
    # regions_df['date'] = file_
    # main_df = pd.concat([main_df, regions_df])

    # df2 = pd.DataFrame(colums=['name', 'date'])
    # name = []
    # dates = []

    # for x in df['region']:
    #     for name in x:
    #         name.append(name['name'])
    #         dates.append(file_)

# df2['name'] = names
# df2['date'] = dates
