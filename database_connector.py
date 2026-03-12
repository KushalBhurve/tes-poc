import time
import random

def get_user_data(user_id):
    # SIMULATED BUG: Connection pooling is not handled. 
    # If a user_id is above 500, it triggers a recursive loop or a long sleep.
    if int(user_id) > 500:
        print("DEBUG: Connection pool exhausted, retrying...")
        time.sleep(30) # This causes the API Gateway to timeout
    return {"id": user_id, "name": "Corporate User", "status": "Active"}