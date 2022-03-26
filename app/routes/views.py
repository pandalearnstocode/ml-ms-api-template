from __future__ import annotations
import pandas as pd
from io import StringIO
from fastapi import APIRouter, Depends, File, UploadFile, Form
from app.lib.ml.mainmod import main_func as main_func_a
from app.lib.de.mainmod import main_func as main_func_b
from app.core.auth import get_current_user

router = APIRouter()


@router.get("/")
async def index() -> dict[str, str]:
    return {
        "info": "This is the index page of fastapi-nano. "
        "You probably want to go to 'http://<hostname:port>/docs'.",
    }


@router.get("/ml/{num}", tags=["ml"])
async def view_a(
    num: int, auth: Depends = Depends(get_current_user),
) -> dict[str, int]:
    return main_func_a(num)


@router.get("/de/{num}", tags=["de"])
async def view_b(
    num: int, auth: Depends = Depends(get_current_user),
) -> dict[str, int]:
    return main_func_b(num)


@router.post('/uploadfile/', tags=["utils"])
async def create_data_file(
        experiment: str = Form(...),
        file_type: str = Form(...),
        file_id: str = Form(...),
        data_file: UploadFile = File(...),
        ):
    upload_df = pd.read_csv(StringIO(str(data_file.file.read(), 'utf-8')), encoding='utf-8')
    df_cols_list = list(upload_df.columns)
    df_dtypes_dict = upload_df.dtypes.apply(lambda x: x.name).to_dict()
    
    return {'filename': data_file.filename, 
            'experiment':experiment, 
            'file_type': file_type, 
            'file_id': file_id,
            'df_cols_list': df_cols_list,
            'df_dtypes': df_dtypes_dict}
