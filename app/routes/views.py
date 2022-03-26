from __future__ import annotations
import pandas as pd
import os
import io, base64
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


@router.post('/uploadfile/', tags=["utils"]
async def create_data_file(
        experiment: str = Form(...),
        file_type: str = Form(...),
        file_id: str = Form(...),
        data_file: UploadFile = File(...),
        ):
    pd.read_csv(StringIO(str(data_file.file.read(), 'utf-16')), encoding='utf-16')
    return {'filename': data_file.filename, 
            'experiment':experiment, 
            'file_type': file_type, 
            'file_id': file_id}