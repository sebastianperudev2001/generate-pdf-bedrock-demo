import requests

def call_api():
    url = "https://qe0nvuo011.execute-api.us-east-1.amazonaws.com/dev"
    params = {
        "prompt": "Hello what is your name?"  # Replace with your prompt value
    }

    try:
        response = requests.post(url, params=params)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful

        # Process the response data here
        data = response.json()
        print(data)

    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

call_api()