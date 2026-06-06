# Automated ETL Pipeline using World Bank API

## 📌 Project Overview

This project implements an Automated ETL Pipeline that extracts population data from the World Bank REST API, transforms and cleans the data using Pandas, loads the processed data into SQLite, logs execution details, and schedules automatic execution using APScheduler.

---

## 📌 ETL Architecture

World Bank API
        │
        ▼
   Extract Data
        │
        ▼
 Transform Data
        │
        ▼
   Load to SQLite
        │
        ▼
 Logging & Monitoring
        ▲
        │
 APScheduler (24 Hours)

---

## 📌 Features

- Extract data from World Bank API
- Store raw data
- Clean and transform data
- Handle null values
- Remove duplicates
- Create derived columns
- Load data into SQLite
- Log pipeline execution
- Automatic scheduling

---

## 📌 Tech Stack

- Python
- Pandas
- Requests
- SQLite
- SQLAlchemy
- APScheduler

---

## 📌 Project Structure

(Your folder structure here)

---

## 📌 Installation

pip install -r requirements.txt

---

## 📌 Run

python src/main.py

---

## 📌 Scheduler

python src/scheduler.py

---

## 📌 Screenshots

## Architecture

![Architecture](screenshots/architecture.png)

## API Response

![API](screenshots/api_response.png)

## Processed Data

![Processed](screenshots/processed_data.png)

## SQLite

![SQLite](screenshots/sqlite_table.png)

## Logs

![Logs](screenshots/logs.png)

---

## 📌 Future Improvements

- PostgreSQL
- Docker
- Airflow
- Data Validation
- Cloud Deployment