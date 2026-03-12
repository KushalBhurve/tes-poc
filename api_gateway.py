from database_connector import get_user_data

def process_request(request):
    user_id = request.get("user_id")
    data = get_user_data(user_id)

    return {"status": 200, "payload": data}
