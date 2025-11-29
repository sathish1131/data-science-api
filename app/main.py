from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.file_upload import router as file_upload_router
from app.routers.data_clean import router as data_clean_router


app = FastAPI(title="Data Science API")

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"]
)

app.include_router(file_upload_router)
app.include_router(data_clean_router)