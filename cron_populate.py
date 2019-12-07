import requests
import traceback

try:
    l = requests.get("http://localhost:8000/populate/")
    print("successful")
except Exception:
    traceback.print_exc()