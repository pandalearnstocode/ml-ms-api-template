# Microservice template using FastAPI for ML engine & related workflow

## __Modelling Data I/O__

* upload: a user will upload a data
* api: we will fetch data from some api
* db: we will read data from a DB
* read from blob: a user will give some parameter, using data we will read data from a blob
* read from file share: a user will give some parameter, using data we will read data from a attached file share
* file system: : a user will give some parameter, using data we will read data from local file system

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
  * after all the things above validate the data is in the expect format before storing the processed ata
* data type optimize
  * before storing the processed data optimize the data type.


__Reference:__

* https://github.com/rednafi/fastapi-nano#
* https://fastapi-crudrouter.awtkns.com/
