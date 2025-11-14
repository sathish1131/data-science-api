from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO

router = APIRouter()

@router.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):
	try:
		filename = file.filename.lower()
		if not (filename.endswith(".csv") or filename.endswith(".xlsx")):
			raise HTTPException(status_code=400, detail="Only CSV or XLSX file are allowed")
		content = await file.read()

		if filename.endswith(".csv"):
			df = pd.read_csv(BytesIO(content))
		elif filename.endswith(".xlsx"):
			df = pd.read_excel(BytesIO(content))

		json_df = df.to_dict(orient="records")

		return {
			"status": "success",
			"rows": len(json_df),
			"columns": list(df.columns),
			"data": json_df
		}
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))
