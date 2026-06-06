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

<img width="537" height="301" alt="architecture" src="https://github.com/user-attachments/assets/71f645ce-8c16-4dbe-9b20-a2be45969ce4" />



## API Response

<img width="1763" height="940" alt="api_response" src="https://github.com/user-attachments/assets/203235f6-92d9-495f-91cc-52b918236997" />


## Processed Data

<img width="1777" height="1056" alt="processed_data" src="https://github.com/user-attachments/assets/fd4e6721-451d-4aa2-9bc9-79e4e4e840fd" />


## SQLite

<img width="1421" height="973" alt="sqlite_table" src="https://github.com/user-attachments/assets/db88ffcf-3af8-4e7f-82df-87033aa75acb" />


## Logs

<img width="1918" height="1025" alt="logs" src="https://github.com/user-attachments/assets/aa4c64df-5d7b-45ff-af2a-9189693d018f" />


---

## 📌 Future Improvements

- PostgreSQL
- Docker
- Airflow
- Data Validation
- Cloud Deployment
