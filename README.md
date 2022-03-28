# __Microservice template using FastAPI for ML engine & related workflow__

## __Modelling Data I/O__

* __upload:__ a user will upload a data
* __api:__ we will fetch data from some api
* __db:__ we will read data from a DB
* __read from blob:__ a user will give some parameter, using data we will read data from a blob
* __read from file share:__ a user will give some parameter, using data we will read data from a attached file share
* __file system:__ a user will give some parameter, using data we will read data from local file system

## __Data processing__

* validate
  * expected columns are present
  * expected data types are matching
  * no NA is present in certain columns
  * certain columns needs to be positive or non-negative
  * date formats are matching
  * date granularity is matching
* process
  * change date granularity
  * change column names
  * select few columns
  * rename few columns
  * filter columns
  * aggregate columns for given parameters
  * impute certain columns
* reshape
  * long to wide
  * wide to long
* validate
  * after all the things above validate the data is in the expect format before storing the processed data
* data type optimize
  * before storing the processed data optimize the data type.

## __Utils:__

* Upload csv/xlsx or any other flat file.

upload file > see head of data frame > confirm columns are looking fine > select some of the columns > rename columns > change data type if required > save.

### __How to consume data in analytical application layer__

__Reference:__

* https://github.com/rednafi/fastapi-nano#
* https://fastapi-crudrouter.awtkns.com/


```python
{
    "data_frame_id": "",                    # hash: derived, string
    "data_frame_cols": [],                  # list of columns: information present in the file
    "data_frame_data_types": {},            # data type dict: information present in the file
    "data_frame_name": "",                  # default name of data frame either by source or user input
    "data_frame_source": "",                # default values from historical information. string. later this can be updated by a user.
    "data_frame_period": "",                #
    "data_frame_granularity": "",           #
    "data_frame_date_col": "",              #
    "data_frame_date_format": ""            #
    "data_frame_location":"",               #
    "data_frame":""                         #
    "uploaded_at":"",                       #
    "uploaded_by":""                        #
}
```

A user will upload a csv file. After uploading we need to derive data id, cols, initial data types. We will provide a basic data frame name, source, period, granularity, date col, format from past information available. will store data frame in dataframe if possible otherwise will write null. if we are not saving dataframe in db we can write it in file share/blob or file system and write the location.

After writing stuff, we will update the following information,


```python
{
    "data_frame_id": "",                 # hash
    "data_frame_cols": [],               # list of columns
    "data_frame_data_types": {},         # data type dict
    "data_frame_name": "",               # default name of data frame either by source or user input
    "data_frame_source": "",             # 
    "data_frame_period": "",             #
    "data_frame_granularity": "",        #
    "data_frame_date_col": "",           #
    "data_frame_date_format": ""         #
    "data_frame_location":"",            #
    "data_frame":"",                     #
    "updated_data_frame_name":"",        #
    "updated_data_frame_source":"",      #
    "updated_data_frame_period":"",      #
    "updated_data_frame_granularity":"", #
    "updated_data_frame_date_col":"",    #
    "updated_data_frame_date_format":"", #
    "select_data_frame_cols":"",         #
    "updated_cols_name":{},              #
    "updated_data_types":{},             #
    "updated_data_hash": "",             #
    "uploaded_at":"",                    #
    "uploaded_by":"",                    #
    "updated_at":"",                     #
    "updated_by":""                      #
}


```
