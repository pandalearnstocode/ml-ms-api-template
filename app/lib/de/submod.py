# This a dummy module
# This gets called in the module_main.py file

from __future__ import annotations

import random


def rand_gen(num: int) -> dict[str, int]:
    num = int(num)
    d = {
        "seed": num,
        "random_first": random.randint(0, num),
        "random_second": random.randint(0, num),
    }
    return d

# %%

import pandas as pd
import joblib
from loguru import logger

### Validate dataframe columns

def _register_dataframe():
    # read data
    # read init columns
    # read init data types
    # get other meta data: name of data, source of data, period of data, date granularity present, date column in data, date format
    # register dataframe in db

    pass

def _get_datatypes_dict(df):
    return df.dtypes.apply(lambda x: x.name).to_dict()

def _list_to_string(list_of_strings):
    return ', '.join(map(str, list_of_strings))

def _get_dataframe_id(df):
    return joblib.hash(df)

def _get_dataframe(dataframe_id):
    data_path = "/home/abinbev/work/commercial_analytics/Shared/mt_api_template/sample_data/names_dataset.csv"
    sample_data = pd.read_csv(data_path)
    return sample_data

def _get_dataframe_headers(dataframe_id):
    pass

def _get_dataframe_datatype(dataframe_id):
    pass

def _get_dataframe_metadata(dataframe_id):
    pass


def _validate_df_cols(dataframe_id, dataframe_req_cols):
    if dataframe_req_cols:
        try:
            df = _get_dataframe(dataframe_id)
            logger.info("Successfully read dataframe")
        except Exception as e:
            logger.info(f"Error reading dataframe: {e}")
            raise e
        df_cols_list = sorted(list(df.columns))
        intersection_values = sorted(list(set(dataframe_req_cols).intersection(df_cols_list)))
        if intersection_values == df_cols_list:
            logger.info("All columns are present.")
            return True
        else:
            df_cols_list = sorted(list(df.columns))
            not_present_cols = list(set(df_cols_list).difference(set(dataframe_req_cols)))
            logger.info(f"Columns not present: {_list_to_string(not_present_cols)}.")
            return False
    else:
        raise Exception("Empty list of required columns for validation.")



data_path = "/home/abinbev/work/commercial_analytics/Shared/mt_api_template/sample_data/names_dataset.csv"
sample_data = pd.read_csv(data_path)
dataframe_req_cols = list(sample_data.columns)
dataframe_req_cols.remove("names")
dataframe_id = ""

_validate_df_cols(dataframe_id, dataframe_req_cols)




# %%

# %%

{
    "data_frame_id": "",
    "data_frame_cols": [],
    "data_frame_dtypes": {},
    "data_frame_metadata": {
        "data_frame_name": "",
        "data_frame_source": "",
        "data_frame_period": "",
        "data_frame_granularity": "",
        "data_frame_date_col": "",
        "data_frame_date_format": ""
    }
}

# %%
import sqlite3
import os.path



def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(empId, name, photo, resumeFile):
    try:
        # BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        # db_path = os.path.join(BASE_DIR, "SQLite_Python.db")
        sqliteConnection = sqlite3.connect("/home/abinbev/work/commercial_analytics/Shared/mt_api_template/app/lib/de/SQLite_Python.db")
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        # init_table = """CREATE TABLE new_employee ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL, resume BLOB NOT NULL);"""
        # cursor.execute(init_table)
        sqlite_insert_blob_query = """INSERT INTO new_employee
                                  (id, name, photo, resume) VALUES (?, ?, ?, ?)"""

        empPhoto = convertToBinaryData(photo)
        resume = convertToBinaryData(resumeFile)
        print("here")
        # Convert data into tuple format
        data_tuple = (empId, name, empPhoto, resume)
        print("here too")
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

insertBLOB(2, "Smith", "/home/abinbev/work/commercial_analytics/Shared/mt_api_template/sample_data/names_dataset.csv", "/home/abinbev/work/commercial_analytics/Shared/mt_api_template/sample_data/names_dataset.csv")
insertBLOB(3, "David", "/home/abinbev/work/commercial_analytics/Shared/mt_api_template/sample_data/names_dataset.csv", "/home/abinbev/work/commercial_analytics/Shared/mt_api_template/sample_data/names_dataset.csv")
# %%

convertToBinaryData("/home/abinbev/work/commercial_analytics/Shared/mt_api_template/sample_data/names_dataset.csv")
# %%
# https://pynative.com/python-sqlite-blob-insert-and-retrieve-digital-data/