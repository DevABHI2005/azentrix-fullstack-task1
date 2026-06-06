from sqlalchemy import create_engine


def load_data(df):

    print("Starting data loading...")

    engine = create_engine(
        "sqlite:///database/population.db"
    )

    df.to_sql(
        "population_data",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded successfully into SQLite database")