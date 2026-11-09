import os
import requests

base = os.environ["PARTNER_API_BASE"]
print(requests.get(base + "/availability", timeout=10).status_code)
