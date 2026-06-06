import pandas as pd
from datetime import datetime


def transform_data(df):

    print("Starting data transformation...")

    # Remove rows where population is null
    df = df.dropna(subset=["population"])

    # Convert year column to integer
    df["year"] = df["year"].astype(int)

    # Convert population column to integer
    df["population"] = df["population"].astype(int)

    # Create new column: population in millions
    df["population_millions"] = (df["population"] / 1000000).round(2)

    # Create new column: population category
    df["population_category"] = df["population"].apply(categorize_population)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Sort values
    df = df.sort_values(by="population", ascending=False)

    # Reset index
    df = df.reset_index(drop=True)

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Save processed file
    processed_file_path = f"data/processed/processed_population_{timestamp}.csv"

    df.to_csv(processed_file_path, index=False)

    print(f"Processed data saved at: {processed_file_path}")

    return df


def categorize_population(population):

    if population >= 100000000:
        return "High Population"

    elif population >= 10000000:
        return "Medium Population"

    else:
        return "Low Population"