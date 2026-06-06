import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read API URL from .env
API_URL = os.getenv("API_URL")


def extract_data():

    print("Starting data extraction...")

    response = requests.get(API_URL)

    # Check API status
    if response.status_code != 200:
        raise Exception("API request failed")

    # Convert JSON response
    data = response.json()

    # Actual records are inside index 1
    records = data[1]

    extracted_data = []

    for item in records:

        extracted_data.append({
            "country": item["country"]["value"],
            "country_id": item["country"]["id"],
            "year": item["date"],
            "population": item["value"]
        })

    # Create DataFrame
    df = pd.DataFrame(extracted_data)

    # Create timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Save raw file
    raw_file_path = f"data/raw/raw_population_{timestamp}.csv"

    df.to_csv(raw_file_path, index=False)

    print(f"Raw data saved at: {raw_file_path}")

    return df


if __name__ == "__main__":
    extract_data()