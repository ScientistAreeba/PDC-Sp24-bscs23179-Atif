import requests
import time

BASE_URL = "http://127.0.0.1:8000"

for i in range(1, 8):

    print(f"\nRequest #{i}")

    try:
        response = requests.get(
            f"{BASE_URL}/generate",
            params={"prompt": "Explain Distributed Systems"}
        )

        print("Status Code:", response.status_code)

        # SAFE JSON handling (IMPORTANT FIX)
        try:
            data = response.json()
        except Exception:
            data = response.text

        print("Response:", data)

        print("X-Student-ID Header:",
              response.headers.get("X-Student-ID"))

    except Exception as e:
        print("Error:", e)

    time.sleep(1)