

from fastapi.responses import JSONResponse


def api_response(session_id, data, status="success"):
	return JSONResponse(content={
		"session_id": session_id,
		"status": status,
		"data": data
	})