import os
import json
import requests

json_dir = "D:/art/Public/output_json"
submit_url = "http://103.199.17.56:25001/submit_artwork"

for filename in os.listdir(json_dir):
    if filename.lower().endswith(".json"):
        json_path = os.path.join(json_dir, filename)
        print(f"Sending {json_path}...")
        with open(json_path, "r") as f:
            data = json.load(f)
        
        try:
            response = requests.post(submit_url, json=data)
            print(f"Response for {filename}: {response.status_code} - {response.json()}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending {filename}: {e}")

print("All JSON files processed.")
