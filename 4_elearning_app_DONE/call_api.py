import requests

def call_api():
    url = "https://yrj0xmfygj.execute-api.us-east-1.amazonaws.com/dev"  # Replace with your API endpoint URL
    params = {
        "prompt": "Qué modelos de nube ofrece Azure?"  # Replace with your prompt value
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful

        # Process the response data here
        data = response.json()
        print(data)

    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

call_api()