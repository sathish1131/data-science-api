

def api_response(session_id, data, status="success"):
	return {
		"session_id": session_id,
		"status": status,
		"data": data
	}