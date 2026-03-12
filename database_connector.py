import time
import random

def get_user_data(user_id):
    
    if int(user_id) > 500:
        print("DEBUG: Connection pool exhausted, retrying...")
        time.sleep(30) 

    return {"id": user_id, "name": "Corporate User", "status": "Active"}
