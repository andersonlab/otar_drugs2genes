#!/usr/bin/env python


__author__ = 'Leland Taylor'
__date__ = '2021-06-23'
__version__ = '0.0.1'

import argparse
import pandas as pd
import glob
from distutils.version import LooseVersion

# Get compression opts for pandas
compression_opts = 'gzip'
if LooseVersion(pd.__version__) > '1.0.0':
    compression_opts = dict(method='gzip', compresslevel=9)

def main():
    """Run CLI."""
    parser = argparse.ArgumentParser(
        description="""
            Json file
            """
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s {version}'.format(version=__version__)
    )

    parser.add_argument(
        '-d', '--directory',
        action='store',
        dest='directory',
        required=True,
        help='Directory with json files.'
    )

    parser.add_argument(
        '-of', '--output_file',
        action='store',
        dest='output_file',
        default='out_df',
        help='Basename of output file. \
            (default: %(default)s)'
    )

    options = parser.parse_args()

    # Get the parameters
    directory = options.directory
    output_file = options.output_file

    # read the files
    files = glob.glob("{}/*json".format(directory))
    df_list = []
    for f in files:
        # Read the json file
        df_json_tmp = pd.read_json(f, lines=True)
        df_list.append(df_json_tmp)

    df = pd.concat(df_list, ignore_index=True)

    # Save the dataframe
    df.to_csv(
        output_file,
        sep='\t',
        compression=compression_opts,
        index=False,
        header=True
    )


if __name__ == '__main__':
    main()
