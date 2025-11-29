from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO
from app.routers.api_response import api_response

router = APIRouter()

@router.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):
	try:
		filename = str(file.filename).lower()
		if not (filename.endswith(".csv") or filename.endswith(".xlsx")):
			raise HTTPException(status_code=400, detail="Only CSV or XLSX file are allowed")
		content = await file.read()

		df = None
		if filename.endswith(".csv"):
			df = pd.read_csv(BytesIO(content))
		elif filename.endswith(".xlsx"):
			df = pd.read_excel(BytesIO(content))

		if df is not None:
			df_json = df.to_dict(orient="records")
			df_head = df.head(20).to_dict(orient="records")
			preview = [dict(row) for row in df_head]
			data = {
				"row_count": len(df_json),
				"columns": list(df.columns),
				"preview": preview
			}
			return api_response("", data)
		else:
			raise Exception("File should be csv or xlsx")

		
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))
