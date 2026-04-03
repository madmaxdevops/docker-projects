import requests
import time

backend_url = "http://backend-container:5000"

while True:
    try:
        response = requests.get(backend_url)

        if response.status_code == 200:
            print("Frontend received the following response from the backend:")
            print(response.text)
        else:
            print("Backend responded with status:", response.status_code)

    except Exception as e:
        print("Failed to communicate with the backend:", e)

    # wait for 10 seconds before next request
    time.sleep(10)