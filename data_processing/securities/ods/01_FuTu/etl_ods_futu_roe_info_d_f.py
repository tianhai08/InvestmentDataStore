import requests
import pandas as pd

def fetch_securities_data(api_key):
    url = "https://api.broker.com/securities_data"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df.to_csv('data_processing/securities/ods/securities_data.csv', index=False)
        print("Securities data fetched successfully.")
    else:
        print("Failed to fetch securities data.")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    fetch_securities_data(api_key)
