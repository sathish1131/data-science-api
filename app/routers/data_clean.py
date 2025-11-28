from fastapi import APIRouter, HTTPException
import pandas as pd
from io import BytesIO
from app.routers.api_response import api_response


router = APIRouter()

@router.post("/data-clean")
def data_clean():
	pass