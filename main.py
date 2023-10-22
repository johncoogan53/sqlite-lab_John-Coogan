"""
ETL-Query script
"""
import time
import fire
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def main(query_string):
    start_time = time.time()
    # Extract
    print("Extracting data...")
    extract()

    # Transform and load
    print("Transforming data...")
    load()

    # Query
    print("Querying data...")
    query(query_string)

    end_time = time.time()
    print("Total time taken: {}".format(end_time - start_time))


if __name__ == "__main__":
    fire.Fire(main)
