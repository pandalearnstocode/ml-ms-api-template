# Data I/O

## Options

* __upload:__ a user will upload a data
* __api:__ we will fetch data from some api
* __db:__ we will read data from a DB
* __read from blob:__ a user will give some parameter, using data we will read data from a blob
* __read from file share:__ a user will give some parameter, using data we will read data from a attached file share
* __file system:__ a user will give some parameter, using data we will read data from local file system

___________________________________________________________________________Data IO using file upload________________________________________________________________

## UI

* A drop down showing all possible data hooks. If `upload` has been selected and a user click next, the following stuff should happen.
* A page with file selector. This should have a validation in place. It should be able to upload certain type of files. if possible we need to put a validation regarding the file name as well. if the file name is not from a list it should throw an warning.
* A drop down to select an element from a list. this will be used as `data_frame_name`. one option in this is list unknown.
* A drop down to select an element from a list. this will be used as `data_frame_source`. one option in this is list unknown.
* Check if `uploaded_by` info is present, if send as part of payload.
* A `next` button.


## Backend

* read the data as dataframe
* extract columns `data_frame_cols`
* extract data type `data_frame_data_types`
* get dataset it `data_frame_id`
* derive `uploaded_at` and write it in db
* if `uploaded_by` is present write it in db
* check the data size, take a call it should be stored in a db or a file system. store and update the info in db.
* store available info in db and send this information to UI


## UI

* a multi-select to select some of the columns with all as an option.
* for selected columns provide an option to rename the columns. apply validation what all can be a valid value for column name.
* provide an option to change the data types of the columns.
* provide an option to choose date format for the date columns in the data.
* provide an option to choose date frequency of the date columns in the data.
* select hierarchical key columns of the data.
* choose imputation for numerical columns
* choose if aggregation needs to be applied or not. if the for aggregation function for all the columns.
* parse all the above information and send it to the backend.


## Backend


## UI

* show head with the applied changes.
* show a button to save file in DB.
* one click of a button save updated information in DB.


___________________________________________________________________________End of Data IO using file upload________________________________________________________________

https://github.com/pandalearnstocode/analytical-app-template-ui-app
https://github.com/pandalearnstocode/analytical-app-template-be-api