from database_connector import get_user_data

def process_request(request):
    user_id = request.get("user_id")
    # This call will hang if user_id > 500, causing a "504 Gateway Timeout"
    data = get_user_data(user_id)
    return {"status": 200, "payload": data}