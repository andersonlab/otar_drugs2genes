#!/usr/bin/env python


__author__ = 'Leland Taylor'
__date__ = '2021-06-23'
__version__ = '0.0.1'

import pandas as pd
from ast import literal_eval
from distutils.version import LooseVersion

# Get compression opts for pandas
compression_opts = 'gzip'
if LooseVersion(pd.__version__) > '1.0.0':
    compression_opts = dict(method='gzip', compresslevel=9)


def main():
    # Read in the core dataset
    df_core = pd.read_csv('molecule.tsv.gz', sep='\t')

    # Add in moa data
    df_moa = pd.read_csv('mechanismOfAction.tsv.gz', sep='\t')
    for i in ['targets', 'chemblIds']:
        df_moa[i] = df_moa[i].fillna('[]')
        df_moa[i] = df_moa[i].apply(literal_eval)  # convert to list type
        df_moa = df_moa.explode(i)
    df_moa = df_moa.rename({'chemblIds': 'id'}, axis='columns')

    # Combine the data
    df = df_core.merge(
        df_moa,
        how='left',
        on='id'
    )

    # Save the dataframe
    df.to_csv(
        'molecule_moa.tsv.gz',
        sep='\t',
        compression=compression_opts,
        index=False,
        header=True
    )


if __name__ == '__main__':
    main()
